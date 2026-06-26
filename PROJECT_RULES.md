# Project Rules

Rules for writing, formatting, and presenting NephroVision materials.

---

## Writing Tone

- Use formal academic English.
- Prefer active voice in methods and system description.
- Keep sentences concise and precise.
- Avoid hype, marketing language, and superlatives.
- Define every acronym on first use.
- Use "we" for the team's work; use passive voice only when the actor is irrelevant.

## Formatting Conventions

- Headings: Sentence case for section titles.
- Numbers: Report metric values exactly as listed in `KNOWN_METRICS.md`.
- Units: Include units with every measurement (e.g., mm, voxels).
- Tables: Use `booktabs` style in LaTeX; keep slide tables readable.
- Figures: Vector-first (PDF/SVG), then high-resolution PNG; label axes and include legends.
- Captions: Placed below figures, above tables.

## Naming Conventions

### Files

- Report figures: `fig_<section>_<number>_<topic>.<ext>`
- Report tables: `tab_<section>_<number>_<topic>.tex`
- Presentation images: `slide_<number>_<topic>.<ext>`
- Sections: `<number>_<name>.tex`

### Terms

- Use **NephroVision** as the project name.
- Use **kidney** and **tumor/cyst** as class names.
- Use **3D U-Net** for the model.
- Use **KiTS23** for the dataset.
- Use **Software as a Medical Device (SaMD)** academic prototype for regulatory framing.

## Report and Slide Rules

### Report

- Follow IEEE two-column conference format.
- Include abstract, introduction, methodology, results, discussion, conclusion, and references.
- Cite every non-obvious claim.
- Include a limitations section.
- Add the intended-use disclaimer in the discussion or conclusion.

### Slides

- One idea per slide.
- Use visuals over bullet lists where possible.
- Keep text large enough for projection.
- Include a limitations and disclaimer slide.
- Reuse exact numbers from `KNOWN_METRICS.md`; do not round unless explicitly stated.

## Safety Wording Rules

- Always describe NephroVision as **decision-support** or **computer-aided**.
- Always state that outputs require **physician review**.
- Never state that the system diagnoses, treats, or replaces clinicians.
- Never claim regulatory or clinical approval.
- Use "evaluated on" rather than "validated for" when describing dataset results.
- Use "future work" or "required" for gaps such as external validation, cybersecurity, and clinical trials.

## Citation Placeholder Rules

- Use `[REF]` as a placeholder when a source is required but not yet inserted.
- Every `[REF]` must be resolved before submission.
- Use `refs.bib` for all BibTeX entries.
- Follow IEEE citation style in the report.
- Prefer peer-reviewed sources: journal articles, conference papers, official challenge documentation.
