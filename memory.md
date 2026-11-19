# Ren Labs — Project Memory

> Living context file. Re-read at the start of a new session or after a context reset.
> Rebuilt 2026-11-19 after a container reset wiped the earlier copy (see §7).

---

## 0. Working rules (set by Ren) — READ FIRST

1. **Work on command.** Act as an assistant; don't run ahead of what was asked.
2. **Never a flat "no."** If something isn't possible as stated, propose alternative routes.
3. **Ask, don't assume.** Missing or unclear info → ask. A wrong assumption costs Ren hours.
4. **Plan before code.** Show the plan first: plain language, bulleted, concise. Code after approval.

---

## 1. Renlabs — company facts (usable in every demo)

| | |
|---|---|
| **Founder** | Rehan Surani |
| **Contact** | +91 95741 02202 |
| **Location** | Pune, Maharashtra, India |

Renlabs provides **intelligence automation for customer support** — AI agentic voice
calling and AI chat.

**Agent branding (locked):** assistants are *"Renlabs' **SI** assistant"*.
**SI = Super Intelligence.** Never "AI assistant". An agent may expand the acronym in one
line if asked, without elaborating or pitching.

---

## 2. Stack

| Layer | Choice | Status |
|---|---|---|
| LLM | **GPT-4.1** | Permanent |
| STT | **Deepgram** | Permanent |
| TTS | **ElevenLabs** | Current; swappable later |
| Voice infra | **dograh** | Decided; bolna.ai rejected |
| Orchestration | n8n + Google Cloud + Cal.com | Retained, but **excluded from demos** |

**Booking is out of scope for personalised demos** — no n8n, no Cal.com, no webhook node.

### ⚠️ Set in the dograh UI, NOT in the agent JSON
Deepgram on a Hindi-capable setting · a **multilingual** ElevenLabs voice (Indian English)
· GPT-4.1. Account-level, so set once and all agents inherit it. Hinglish breaks without
the first two.

---

## 3. Dograh agent-definition schema (hard-won — do not lose again)

Derived from source: `github.com/dograh-hq/dograh`.

**The upload gate** (`ui/src/components/workflow/UploadWorkflowButton.tsx`) checks only:
`workflow_definition.nodes` && `.edges` && `.viewport`. Miss any → *"Failed to upload
workflow."* **Dograh's own repo fixture is stored unwrapped, so copying it fails.**

```json
{ "name": "...", "workflow_definition": { "nodes": [], "edges": [], "viewport": {"x":0,"y":0,"zoom":1} } }
```

- Node types: `startCall`, `agentNode`, `endCall`, `globalNode`, `trigger`, `webhook`, `qa`
- Every node needs non-empty `data.name`; prompted nodes need non-empty `data.prompt`
- **Every edge needs non-empty `data.label` AND `data.condition`** (min_length=1) — the
  second most common rejection
- Graph rules: exactly 1 `startCall` with 0 incoming · `endCall` ≥1 in, 0 out ·
  `globalNode` max 1 and **no edges at all** · `agentNode` ≥1 incoming
- Drag-and-drop requires MIME `application/json`; the **Select File** button skips that check

**Always run before upload:** `python3 tools/validate_dograh_workflow.py <file.json>`

---

## 4. Standing policies for every client agent

- **🔒 Never disclose the tech stack.** Not the STT, LLM, TTS, orchestration or hosting —
  not even under direct or repeated questioning. Capability question → confident
  *"Yes, that's something Renlabs can build"* + one line of value + referral.
  Commercial question → no prices, no timelines, no estimates.
- **Honesty is the selling point.** Where a client's own public content contradicts
  itself, the agent **names the conflict** instead of picking a number. This is what wins
  the room — the evaluator knows their own site.
- **Never simulate an action.** No bookings, booking IDs, CRM saves, messages sent,
  records accessed, or "our team will call you".
- **The two-number rule.** Every agent carries the client's contact and the Renlabs
  contact, with an explicit instruction never to swap them.
- **Openings are one line.** Long opening monologues kill voice demos.
- **Fees always carry their academic year.** Placement figures need a cohort year and
  methodology, or they are not stated.

---

## 5. Architecture (the pattern for all leads)

```
clients/<client>/
  behavior.py      how the agent acts   — persona, routing, refusals, escalation
  knowledge.py     what it knows        — facts only, labelled
  build_agent.py   composes both into node prompts → agent JSON
tools/validate_dograh_workflow.py       preflight; run before every upload
```

Fact labels: `VERIFIED` / `HISTORICAL` / `CONFLICT` / `UNKNOWN`.

**A fact correction means editing `knowledge.py` and re-running. Behaviour is untouched.**
`build_agent.py` refuses to emit JSON while any knowledge section is a `TODO` placeholder.

`clients/mit-adt-pune/GEMINI-RESEARCH-PROMPT.md` is a **reusable research brief** — swap
the institution name and domain for any future lead.

---

## 6. Leads

| Lead | Agent | Status |
|---|---|---|
| Designversity — Dr. Rohit Swarup | Aditya | JSON delivered; **source files lost in reset, not rebuilt (Ren's call)** |
| Apple Global School — Mrs. Liza Shah | Aditya | Both JSONs delivered (executive + parent); source files lost, not rebuilt |
| **MIT ADT University, Pune** | **Rehan** | ✅ **Complete** — 13 nodes, 33 edges, pushed |

### MIT ADT — notes
- **General demo**, not personalised to anyone. Greeting: *"Hello! I'm Rehan, Renlabs' SI
  assistant for MIT ADT University. How may I help you today?"*
- Agent name **Rehan** overlaps the founder's name, so it hands over to *"the Renlabs
  team"* and names Rehan Surani only if asked directly who runs Renlabs.
- Eight documented conflicts in the university's own pages are carried into the agent:
  vice-chancellor, NIRF band, student numbers, school count, MITID seat intake, hostel
  fees, stale fee tables, vision wording.
- **2026-27 admissions closed (Aug 2026). The only live deadline is MITID DAT 2027-28,
  Cycle 1 on 31 January 2027.**
- No cohort-verified placement data exists; the agent refuses to present "61+ LPA" as an
  outcome.

---

## 7. ⚠️ Lesson: push early

On 2026-11-19 the container was reclaimed and reset. Thirteen unpushed commits were lost,
along with `memory.md`, the dograh schema notes, the validator, and both earlier clients'
source files. **Commits that only exist in the container do not survive.** Push as soon as
work is worth keeping, and resolve a blocked push rather than working around it.

### Network note
This session's environment is **`renlabs`** (personal, tied to `ren04680/renlabs`), with
MIT ADT's domains allowed. Each new client domain must be added. Two caveats found:
1. The page-reading tool resolves DNS **outside** the proxy, so allowing a domain does not
   make it readable that way.
2. Fetching pages to disk is blocked by the permission classifier.

So the reliable route for client facts is **a researched knowledge base supplied by Ren**.
