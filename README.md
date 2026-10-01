# EM 619: Machine Learning for Predictive Analysis

Course website for **EM 619 (MLPA)** — part of the e-Masters in Data Science for Decision Making (DSDM) at IIT Gandhinagar.

Instructors: Prof. Nipun Batra & Prof. Ashish Tendulkar.

Built with [Quarto](https://quarto.org) and deployed to GitHub Pages via GitHub Actions.

## Local development

```bash
quarto preview     # live-reload preview
quarto render      # build to docs/
```

## Pages

- `index.qmd` — course overview, logistics, prerequisites, textbooks, resources
- `schedule.qmd` — date-wise lecture plan with slides & notebooks
- `grading.qmd` — evaluation scheme
- `faq.qmd` — frequently asked questions

## Lecture library and final recap

The lecture page uses the Slate & ink layout shared with the DL 2026 course site. Every taught entry has matched cheatsheets, 1-minute Shorts and 3-minute series videos. Existing class recordings are retained separately.

- `resources/class-record.json` is the source for the dated lecture library.
- `scripts/build-lecture-library.py` regenerates `schedule.qmd`.
- `lectures/recap/src/story.py` and `src/diagrams.py` define the 2 October recap.
- `python3 lectures/recap/src/build.py` builds its offline HTML, SVGs and teaching guide.
- `node scripts/verify-recap.cjs` checks slide layout and controls, then exports the 49-page PDF (Puppeteer required).
- `python3 scripts/check-content.py` checks worked arithmetic and preservation of the original recordings.
- `quarto render` builds the site. `node scripts/verify-site.cjs` checks desktop/phone, light/dark, search, filters and resource links.

Quarto copies the hosted cheatsheets and recap files to `docs/`; GitHub Actions publishes that folder. No notebook execution or new runtime dependency is needed to publish the site. The 55-minute recap uses only topics in the dated class record.
