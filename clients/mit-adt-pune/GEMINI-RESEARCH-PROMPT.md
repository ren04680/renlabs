# Research prompt for Gemini — MIT ADT University, Pune

Paste everything inside the fence into Gemini (with web browsing enabled).
Give the output back as a single `.md` file.

---

```
You are a research analyst. Produce a factual knowledge base about MIT ADT University,
Pune (MIT Art, Design and Technology University), to be used as the retrieval layer for
an AI voice assistant that will answer prospective students' and parents' questions.

The assistant will be demonstrated to the university's own leadership, who know their
institution intimately. A single invented or outdated fact destroys its credibility.
Accuracy matters far more than completeness.

## SOURCE RULES — THIS IS THE MOST IMPORTANT SECTION

1. The ONLY authoritative source is the university's own domain: mituniversity.ac.in
   (including subdomains such as naac.mituniversity.ac.in) and its linked official PDFs
   — brochures, the admission handbook, NAAC and UGC filings.
2. mitid.edu.in may be used for the MIT Institute of Design specifically.
3. Do NOT treat collegedunia, careers360, shiksha, collegedekho, entrancezone, admistay,
   propelld, or any similar aggregator as fact. If you cite one at all, label it clearly
   as an unverified third-party claim.
4. Never fill a gap from your own training knowledge. If the official site does not say
   it, the answer is UNKNOWN.
5. Give the URL for every single fact.
6. State the date you did this research at the top.

## LABEL EVERY FACT

Mark each fact with exactly one of:
- VERIFIED — appears on an official university page or official linked document
- HISTORICAL — was true for a stated older year; give that year explicitly
- CONFLICT — two official sources disagree; give BOTH versions and BOTH URLs
- UNKNOWN — not published, or you could not confirm it

## WHAT I NEED — produce these sections in this order

### 1. Identity and location
Full official name and abbreviation. Founding year, founder, parent trust or group.
Exact campus address with area, city and PIN code. Campus name and acreage if published.
Nearest landmark and distance from Pune railway station and airport, ONLY if officially
published. Official phone numbers, emails, website. Separate admissions contact if there
is one. Office hours.

### 2. About the university
Vision, mission and tagline, worded exactly as published. The number of constituent
schools or institutes AND their exact names. Student and faculty numbers, clearly marked
as the university's own claim. Accreditations worded exactly: UGC status, NAAC grade with
the year awarded, NIRF rank with its exact category and year, any others. Named
leadership: Chancellor, Vice Chancellor, Pro-VC, Registrar, Deans, Head of Admissions.

### 3. Strengths — "the best things about the university"
Be especially careful here. Report what the university itself publishes as its strengths:
labs, studios, industry partnerships, incubator, international collaborations, notable
alumni, flagship events.

For PLACEMENTS, I need the cohort year, the reporting methodology, and whether each
figure is median, average or highest package. A bare "100% placement" or a headline
package number with no cohort is useless — mark it UNKNOWN instead.

For RANKINGS, I need the exact rank, exact category, exact year and issuing body. A rank
without all four is UNKNOWN.

### 4. Schools and programme list
Every programme the university offers, as a table:
exact programme name as published | level (UG/PG/PhD/Diploma) | duration | school or
institute that runs it | eligibility | entrance exams accepted | intake or seats if
published | fees WITH the exact academic year those fees apply to.

Never give a fee without its academic year. If only an older year is published, label it
HISTORICAL and give that year.

### 5. Course structure
For the main programmes — B.Tech, B.Des, BBA, the film and media degrees, and the main
PG programmes — give the year-by-year or semester-by-semester structure as published.
Specialisations and electives, and at which stage a student chooses them. Internships,
industry projects and capstone requirements. Credit system if published.

### 6. Admissions
The application steps in order. Documents required. Application dates WITH the academic
year they apply to — and flag clearly any date that has already passed. Entrance exam
details. Campus visit policy. Scholarship schemes, with eligibility, only if officially
published.

### 7. Campus and facilities
Hostels, labs, studios, library, sports, transport, dining, medical, accessibility.
Mark anything not officially published as UNKNOWN.

### 8. CONFLICTS AND CAUTIONS — do not skip this section
This section is the most valuable thing you can produce. List, as a table:
- Any figure that appears differently on two official pages, with both URLs
- Any official page that is visibly out of date — 2023 or 2024 content still live
- Anything a prospective student would obviously ask that is simply not published
- Any claim that is marketing language rather than a verifiable fact
- Any programme listed in one place but missing from another

### 9. Voice-ready answers
Write 50 to 60 question-and-answer pairs covering what prospective students and parents
actually ask, spread across: location and getting there, what the university is, its
strengths, each major programme, course structure, eligibility, entrance exams, fees,
admissions process, hostels and campus life, placements.

Rules for the answers:
- Each answer is SPOKEN ALOUD, so: one to three sentences, 15 to 35 words. Natural
  spoken English, not written prose.
- No bullet points, no markdown, no URLs read as code, no emoji inside answers.
- Where a fact is uncertain, the answer must say so naturally and point to the
  admissions office — for example "I'd rather the admissions team confirm the current
  figure than quote you an outdated one."
- Where sources conflict, the answer must name the conflict rather than pick a side.
- Include at least 5 answers in natural Hinglish, the way an Indian admissions
  counsellor actually speaks — Roman script, Hindi mixed with English, course names and
  numbers kept in English.
- Never promise admission, a seat, a scholarship, a placement or a specific salary.

### 10. Source directory
Every URL you used, numbered, grouped by official pages first and linked official PDFs
second. Note the date each page was accessed.

## OUTPUT FORMAT
One Markdown document. Start with a header block giving: institution name, the exact
scope of what you researched, the research date, and a clear statement that this is
public-source research and not a university-approved document.

If you cannot verify something, write UNKNOWN. Do not guess, do not estimate, and do not
smooth over a gap with plausible-sounding text. An honest UNKNOWN is worth more to me
than a confident wrong answer.
```
