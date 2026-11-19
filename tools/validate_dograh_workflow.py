#!/usr/bin/env python3
"""Preflight-validate a dograh agent definition before uploading it.

Rules derived from the dograh source (github.com/dograh-hq/dograh):
  ui/src/components/workflow/UploadWorkflowButton.tsx  - client-side upload gate
  api/services/workflow/dto.py                         - backend DTO + graph constraints
  api/services/workflow/node_data.py                   - shared base node fields

Usage:  python3 tools/validate_dograh_workflow.py <file.json>
Exit 0 = safe to upload, 1 = would be rejected.
"""

import json
import sys

PROMPTED = {"startCall", "agentNode", "endCall", "globalNode"}
KNOWN_TYPES = {"startCall", "endCall", "agentNode", "globalNode",
               "trigger", "webhook", "qa"}


def validate(doc):
    errors, warnings = [], []

    if not isinstance(doc, dict):
        return ["Top level must be a JSON object."], []
    if "workflow_definition" not in doc:
        return ["Missing 'workflow_definition' wrapper. The uploader reads "
                "workflow_definition.nodes / .edges / .viewport and rejects the file "
                "without it."], []

    wd = doc["workflow_definition"]
    for key in ("nodes", "edges", "viewport"):
        if not wd.get(key) and wd.get(key) != []:
            errors.append(f"workflow_definition.{key} is missing or empty "
                          f"- the uploader rejects the file.")
    if errors:
        return errors, warnings

    nodes, edges = wd["nodes"], wd["edges"]
    if not doc.get("name"):
        warnings.append("No top-level 'name' - dograh will auto-name it WF-<random>.")

    ids, counts = set(), {}
    for i, n in enumerate(nodes):
        nid, ntype = n.get("id"), n.get("type")
        where = f"node[{i}] (id={nid!r})"
        if not isinstance(nid, str) or not nid:
            errors.append(f"{where}: 'id' must be a non-empty string.")
        elif nid in ids:
            errors.append(f"{where}: duplicate node id.")
        ids.add(nid)

        if ntype not in KNOWN_TYPES:
            errors.append(f"{where}: unknown type {ntype!r}.")
        counts[ntype] = counts.get(ntype, 0) + 1

        pos = n.get("position")
        if not isinstance(pos, dict) or "x" not in pos or "y" not in pos:
            errors.append(f"{where}: 'position' must be an object with x and y.")

        data = n.get("data")
        if not isinstance(data, dict):
            errors.append(f"{where}: 'data' must be an object.")
            continue
        if not str(data.get("name") or "").strip():
            errors.append(f"{where}: data.name is required and must be non-empty.")
        if ntype in PROMPTED and not str(data.get("prompt") or "").strip():
            errors.append(f"{where}: data.prompt is required for type {ntype!r}.")

    incoming = {i: 0 for i in ids}
    outgoing = {i: 0 for i in ids}
    edge_ids = set()
    for i, e in enumerate(edges):
        eid = e.get("id")
        where = f"edge[{i}] (id={eid!r})"
        if not isinstance(eid, str) or not eid:
            errors.append(f"{where}: 'id' must be a non-empty string.")
        elif eid in edge_ids:
            errors.append(f"{where}: duplicate edge id.")
        edge_ids.add(eid)

        src, tgt = e.get("source"), e.get("target")
        for role, endpoint in (("source", src), ("target", tgt)):
            if endpoint not in ids:
                errors.append(f"{where}: {role} {endpoint!r} matches no node id.")
        if src in outgoing:
            outgoing[src] += 1
        if tgt in incoming:
            incoming[tgt] += 1

        d = e.get("data")
        if not isinstance(d, dict):
            errors.append(f"{where}: 'data' must be an object with label and condition.")
            continue
        for key in ("label", "condition"):
            if not str(d.get(key) or "").strip():
                errors.append(f"{where}: data.{key} is required and non-empty "
                              f"(backend enforces min_length=1).")

    n_start = counts.get("startCall", 0)
    if n_start != 1:
        errors.append(f"Found {n_start} startCall nodes - exactly 1 is required.")
    if counts.get("globalNode", 0) > 1:
        errors.append("More than one globalNode - at most 1 is allowed.")

    for n in nodes:
        nid, ntype = n.get("id"), n.get("type")
        if nid not in ids:
            continue
        label = f"{ntype} {nid!r}"
        if ntype == "startCall" and incoming[nid]:
            errors.append(f"{label}: must have 0 incoming edges.")
        if ntype == "globalNode" and (incoming[nid] or outgoing[nid]):
            errors.append(f"{label}: must have no edges at all.")
        if ntype == "endCall":
            if incoming[nid] < 1:
                errors.append(f"{label}: needs at least 1 incoming edge.")
            if outgoing[nid]:
                errors.append(f"{label}: must have 0 outgoing edges.")
        if ntype == "agentNode":
            if incoming[nid] < 1:
                errors.append(f"{label}: needs at least 1 incoming edge.")
            if outgoing[nid] < 1:
                warnings.append(f"{label}: no outgoing edges - dead end.")

    if counts.get("endCall", 0) == 0:
        warnings.append("No endCall node - the agent cannot hang up.")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    try:
        with open(path) as fh:
            doc = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"FAIL  {path}\n  Not valid JSON: {exc}")
        return 1

    errors, warnings = validate(doc)
    wd = doc.get("workflow_definition") or {}
    print(f"{path}")
    print(f"  nodes: {len(wd.get('nodes') or [])}   edges: {len(wd.get('edges') or [])}")
    for w in warnings:
        print(f"  WARN  {w}")
    if errors:
        print(f"\nFAIL - {len(errors)} problem(s); dograh would reject this file:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\nPASS - safe to upload.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
