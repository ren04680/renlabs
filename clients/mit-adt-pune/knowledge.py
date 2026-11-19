"""MIT ADT University, Pune - FACTUAL KNOWLEDGE ONLY.

⛔ NOT YET FILLED. Every section below is a placeholder.

Fill each section from the researched knowledge base, keeping the labels:
  VERIFIED   - appears on an official university page or official linked document
  HISTORICAL - was true for a stated older year; name that year
  CONFLICT   - two official sources disagree; give BOTH, never pick one
  UNKNOWN    - not published; the agent says it does not have it

build_agent.py refuses to emit a JSON while any section still starts with TODO, so a
factless agent cannot be shipped by accident.

Source to fill from: the Gemini research output (see GEMINI-RESEARCH-PROMPT.md).
Authoritative domain: mituniversity.ac.in
"""

LOCATION = """TODO - campus address, area, city, PIN. Campus name and acreage if
published. Nearest landmark. Distance from Pune station and airport ONLY if officially
published. Campus facilities: hostels, labs, studios, library, sports, dining, medical.
Campus visit policy."""

ABOUT = """TODO - full official name and abbreviation. Founding year, founder, parent
trust. Vision, mission, tagline as worded. Number and exact names of constituent schools.
Student and faculty numbers, marked as the university's own claim. Accreditations with
grade, body and year. Named leadership."""

STRENGTHS = """TODO - published strengths: labs, studios, industry partnerships,
incubator, international collaborations, flagship events, notable alumni.
PLACEMENTS: only with cohort year and methodology, else UNKNOWN.
RANKINGS: only with exact rank, category, year and issuing body, else UNKNOWN."""

COURSES = """TODO - full programme list: exact published name, level, duration, school,
eligibility, entrance exams accepted, intake/seats, fees WITH the academic year each
figure applies to."""

STRUCTURE = """TODO - year-by-year or semester structure for the main programmes.
Specialisations and electives, and when they are chosen. Internships, industry projects,
capstone. Credit system if published."""

ADMISSIONS = """TODO - application steps in order. Documents required. Application dates
WITH their academic year, flagging any that have passed. Entrance exam details.
Scholarships only if officially published."""

CONFLICTS = """TODO - this section is what makes the demo credible.
Figures that differ between two official pages (give both). Official pages visibly out of
date. Obvious questions the site simply does not answer. Marketing claims that are not
verifiable facts. Programmes listed in one place but missing elsewhere."""

CONTACTS = """TODO - university phone numbers, emails, website, admissions-specific
contact, office hours.

## RENLABS CONTACT
- Rehan Surani, Founder, Renlabs: +91 95741 02202

## NEVER CONFUSE THE TWO
University questions - courses, fees, admissions, campus - get the UNIVERSITY contact.
Anything about this assistant, what it could do, or Renlabs gets the RENLABS contact."""

RENLABS = """## RENLABS (shareable)
- Renlabs builds intelligence automation for customer support - AI voice agents that
  handle calls, and AI chat.
- Founder: Rehan Surani. Based in Pune, Maharashtra, India.
- Contact: +91 95741 02202.

## WHAT THIS DEMONSTRATION IS
An independent Renlabs demonstration built on MIT ADT University's PUBLIC information.
It is not an authorised or deployed university service.

## CAPABILITIES RENLABS COULD ADD (none are connected here)
Application tracking, campus-visit booking with a live calendar, CRM integration so
enquiries reach the admissions team, inbound and outbound phone calling, WhatsApp and
website chat, more languages, and call transcripts and lead summaries for the team."""
