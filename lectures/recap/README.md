# EM619 course recap

Final lecture, 2 October 2026. A 55-minute recap of the dated class record.

- `index.html?present`: offline interactive presentation; open the HTML without the query for reading.
- `em619-course-recap.pdf`: 49-slide classroom/print export.
- `TEACHING_GUIDE.md`: pacing, questions, answers, notes and original lecture sources.
- `src/story.py`: editable slide content.
- `src/diagrams.py` and `figures/*.svg`: editable original diagrams.

Build from the repository root with `python3 lectures/recap/src/build.py`. Export and verify with `node scripts/verify-recap.cjs` (requires Puppeteer, already available on the authoring machine). Render the course site with `quarto render`.

Visual inspiration: Nipun Batra’s *From Attention to Applications* HTML lecture (light paper, Avenir-style typography, sparse blue diagrams, progressive builds, questions and notes). No transformer content is needed for this course recap.
