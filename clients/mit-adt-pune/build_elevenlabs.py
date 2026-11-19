#!/usr/bin/env python3
"""Flatten the MIT ADT agent into a single system prompt for ElevenLabs Agents.

Same two source modules as the dograh build - behavior.py and knowledge.py - so the two
deliverables never drift. Dograh takes a node graph; ElevenLabs Agents takes one system
prompt, so this collapses the per-node behaviour into topic sections.

Run:  python3 clients/mit-adt-pune/build_elevenlabs.py
Out:  elevenlabs-system-prompt.md   (paste into the agent's System Prompt field)
      elevenlabs-first-message.txt  (paste into the First Message field)
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

import behavior as B  # noqa: E402
import knowledge as K  # noqa: E402

FIRST_MESSAGE = "Hello, Rehan this side, calling from MIT ADT. How may I help you?"

TOPICS = [
    ("LOCATION, CAMPUS AND FACILITIES", B.LOCATION, K.LOCATION),
    ("ABOUT THE UNIVERSITY", B.ABOUT, K.ABOUT),
    ("STRENGTHS, RANKINGS AND PLACEMENTS", B.STRENGTHS, K.STRENGTHS),
    ("COURSES, ELIGIBILITY AND FEES", B.COURSES, K.COURSES),
    ("COURSE STRUCTURE", B.STRUCTURE, K.STRUCTURE),
    ("ADMISSIONS", B.ADMISSIONS, K.ADMISSIONS),
    ("ABOUT THIS ASSISTANT AND RENLABS", B.DEMO, K.RENLABS),
    ("TAKING AN ENQUIRY", B.ENQUIRY, None),
]


def section(title, body):
    return f"\n\n{'=' * 70}\n# {title}\n{'=' * 70}\n\n{body.strip()}"


parts = [
    "# ROLE AND CORE RULES",
    "",
    B.GLOBAL.strip(),
    section("CONTACT DETAILS", K.CONTACTS),
    section("HOW TO OPEN THE CALL", B.GREETING),
    section("DECIDING WHAT THE CALLER WANTS", B.ROUTER),
]

for title, behaviour, facts in TOPICS:
    body = behaviour.strip()
    if facts:
        body += (
            "\n\n--- FACTS YOU MAY USE FOR THIS TOPIC "
            "(respect every VERIFIED / HISTORICAL / CONFLICT / UNKNOWN label; "
            "never read a label aloud) ---\n\n" + facts.strip()
        )
    parts.append(section(title, body))

parts.append(section("KNOWN PROBLEMS WITH THE PUBLISHED INFORMATION", K.CONFLICTS))
parts.append(section("CLOSING THE CALL", B.END_INFO.strip() +
                     "\n\n--- IF THEY WANT TO STOP EARLY ---\n\n" + B.END_EARLY.strip()))

prompt = "\n".join(parts).strip() + "\n"

(HERE / "elevenlabs-system-prompt.md").write_text(prompt)
(HERE / "elevenlabs-first-message.txt").write_text(FIRST_MESSAGE + "\n")

print(f"wrote elevenlabs-system-prompt.md   ({len(prompt):,} chars, "
      f"~{len(prompt)//4:,} tokens)")
print(f"wrote elevenlabs-first-message.txt  ({FIRST_MESSAGE!r})")
