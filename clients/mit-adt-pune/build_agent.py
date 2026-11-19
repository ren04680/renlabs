#!/usr/bin/env python3
"""Build the MIT ADT University voice agent definition for dograh.

Agent name: Rehan. General demo - not personalised to any individual.

Behaviour (behavior.py) and knowledge (knowledge.py) are separate and composed here,
so facts can be corrected without touching behaviour.

Refuses to emit a JSON while any knowledge section is still a TODO placeholder.

Run:  python3 clients/mit-adt-pune/build_agent.py
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

import behavior as B  # noqa: E402
import knowledge as K  # noqa: E402

OUT = HERE / "mit-adt-agent.json"

FACTS_HEADER = (
    "\n\n# ---------------------------------------------------------------\n"
    "# FACTUAL REFERENCE - maintained in knowledge.py, not here.\n"
    "# Use ONLY these facts. Respect every VERIFIED / HISTORICAL / CONFLICT /\n"
    "# UNKNOWN label. Never read these labels or this header aloud.\n"
    "# ---------------------------------------------------------------\n\n"
)

REQUIRED = ["LOCATION", "ABOUT", "STRENGTHS", "COURSES", "STRUCTURE",
            "ADMISSIONS", "CONFLICTS", "CONTACTS"]

unfilled = [n for n in REQUIRED if getattr(K, n).strip().startswith("TODO")]
if unfilled:
    print("REFUSING TO BUILD - knowledge.py still has placeholder sections:\n")
    for n in unfilled:
        print(f"  - {n}")
    print("\nFill these from the researched knowledge base, then re-run.")
    print("An agent built on placeholders would state invented facts to a real "
          "university.")
    sys.exit(1)


def compose(behavior_text, knowledge_text=None):
    if not knowledge_text:
        return behavior_text.strip()
    return behavior_text.strip() + FACTS_HEADER + knowledge_text.strip()


def node(node_id, ntype, name, prompt, x, y, **extra):
    data = {"name": name, "prompt": prompt}
    data.update(extra)
    if ntype == "startCall":
        data["is_start"] = True
    if ntype == "endCall":
        data["is_end"] = True
    return {"id": node_id, "type": ntype, "position": {"x": x, "y": y}, "data": data,
            "measured": {"width": 300, "height": 100},
            "selected": False, "dragging": False}


def edge(src, tgt, label, condition):
    return {"id": f"xy-edge__{src}-{tgt}", "source": src, "target": tgt,
            "type": "custom", "animated": True, "selected": False,
            "data": {"label": label, "condition": condition}}


GLOBAL, START, ROUTER = "3001", "3002", "3003"
LOC, ABOUT, WHY = "3010", "3011", "3012"
COURSES, STRUCT, ADMIT, DEMO = "3013", "3014", "3015", "3016"
ENQUIRY, END_INFO, END_EARLY = "3020", "3090", "3091"

INFO_TOPICS = [LOC, ABOUT, WHY, COURSES, STRUCT, ADMIT, DEMO]
TOPIC_Y = 540
TOPIC_X = {n: -800 + i * 360 for i, n in enumerate(INFO_TOPICS + [ENQUIRY])}

EXTRACTION_VARIABLES = [
    {"name": "caller_name", "type": "string",
     "prompt": "The caller's name, only if they volunteered it."},
    {"name": "caller_contact", "type": "string",
     "prompt": "Phone or email, ONLY if they explicitly opted in to being contacted."},
    {"name": "programme_interest", "type": "string",
     "prompt": "Programme or field they asked about."},
    {"name": "education_level", "type": "string",
     "prompt": "Their current education level, e.g. Class 12, graduate."},
    {"name": "target_intake", "type": "string",
     "prompt": "The intake year they are aiming for."},
    {"name": "city", "type": "string",
     "prompt": "Where they are based, if mentioned."},
    {"name": "questions_asked", "type": "string",
     "prompt": "Concise note of what they asked about and what mattered to them."},
    {"name": "corrections_or_feedback", "type": "string",
     "prompt": "Anything the caller said was wrong, outdated or missing."},
    {"name": "consent_to_contact", "type": "boolean",
     "prompt": "True ONLY if they explicitly agreed to be contacted."},
]

ROUTES = [
    (LOC, "location", "The caller asks where the university is, how to reach it, the "
     "campus itself, hostels, facilities, or visiting."),
    (ABOUT, "about", "The caller asks what MIT ADT is, its history, founder, schools, "
     "size, accreditation, recognition or leadership."),
    (WHY, "strengths", "The caller asks what is good about the university, why choose "
     "it, its reputation, rankings, placements or alumni."),
    (COURSES, "courses", "The caller asks what programmes are offered, eligibility, "
     "entrance exams, seats or fees."),
    (STRUCT, "course structure", "The caller asks what is actually studied in a "
     "programme - the year-wise or semester structure, subjects, specialisations, "
     "electives, internships or projects."),
    (ADMIT, "admissions", "The caller asks how to apply, the application steps, "
     "documents, deadlines or application status."),
    (DEMO, "about the demo", "The caller asks about this assistant itself, how it was "
     "built, whether it is official, who Renlabs is, or anything commercial."),
    (ENQUIRY, "next steps", "The caller wants a follow-up, offers their contact "
     "details, or the conversation moves to what happens next."),
]

nodes = [
    node(GLOBAL, "globalNode", "Global Rules",
         compose(B.GLOBAL, K.CONTACTS), -1200, 160),
    node(START, "startCall", "Start Call", compose(B.GREETING), 600, -80,
         allow_interrupt=False),
    node(ROUTER, "agentNode", "Intent Router", compose(B.ROUTER), 600, 220,
         allow_interrupt=True),
    node(LOC, "agentNode", "Location & Campus",
         compose(B.LOCATION, K.LOCATION), TOPIC_X[LOC], TOPIC_Y, allow_interrupt=True),
    node(ABOUT, "agentNode", "About the University",
         compose(B.ABOUT, K.ABOUT), TOPIC_X[ABOUT], TOPIC_Y, allow_interrupt=True),
    node(WHY, "agentNode", "Strengths & Outcomes",
         compose(B.STRENGTHS, K.STRENGTHS), TOPIC_X[WHY], TOPIC_Y, allow_interrupt=True),
    node(COURSES, "agentNode", "Courses & Eligibility",
         compose(B.COURSES, K.COURSES), TOPIC_X[COURSES], TOPIC_Y, allow_interrupt=True),
    node(STRUCT, "agentNode", "Course Structure",
         compose(B.STRUCTURE, K.STRUCTURE), TOPIC_X[STRUCT], TOPIC_Y,
         allow_interrupt=True),
    node(ADMIT, "agentNode", "Admissions",
         compose(B.ADMISSIONS, K.ADMISSIONS), TOPIC_X[ADMIT], TOPIC_Y,
         allow_interrupt=True),
    node(DEMO, "agentNode", "About This Demo",
         compose(B.DEMO, K.RENLABS), TOPIC_X[DEMO], TOPIC_Y, allow_interrupt=True),
    node(ENQUIRY, "agentNode", "Enquiry Summary",
         compose(B.ENQUIRY), TOPIC_X[ENQUIRY], TOPIC_Y, allow_interrupt=True,
         extraction_enabled=True,
         extraction_prompt=("Extract only what was actually said. Leave a field empty "
                            "rather than guessing. consent_to_contact must be true ONLY "
                            "on an explicit yes."),
         extraction_variables=EXTRACTION_VARIABLES),
    node(END_INFO, "endCall", "End - Informed", compose(B.END_INFO), 460, 900),
    node(END_EARLY, "endCall", "End - Early Exit", compose(B.END_EARLY), 1200, 900),
]

edges = [edge(START, ROUTER, "begin", "Always take this route.")]
for target, label, condition in ROUTES:
    edges.append(edge(ROUTER, target, label, condition))
edges.append(edge(ROUTER, END_EARLY, "caller leaving",
                  "The caller says goodbye or wants to stop before any topic has been "
                  "discussed."))

for topic in INFO_TOPICS:
    edges.append(edge(topic, ROUTER, "new topic",
                      "The caller moves to a different subject from the one being "
                      "discussed here."))
    edges.append(edge(topic, ENQUIRY, "next steps",
                      "The caller wants a follow-up, offers contact details, or the "
                      "conversation moves to what happens next."))
    edges.append(edge(topic, END_INFO, "finished",
                      "The caller has no further questions or ends the conversation."))

edges.append(edge(ENQUIRY, ROUTER, "more questions",
                  "The caller has another question about the university."))
edges.append(edge(ENQUIRY, END_INFO, "finished",
                  "The conversation has reached its natural end."))

workflow = {
    "name": "MIT ADT University - Rehan (Renlabs Demo)",
    "workflow_definition": {"nodes": nodes, "edges": edges,
                            "viewport": {"x": 0, "y": 0, "zoom": 1}},
}

OUT.write_text(json.dumps(workflow, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {OUT.name}  ({len(nodes)} nodes, {len(edges)} edges)")
