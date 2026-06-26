# NephroVision 4-Page IEEE Report

## Directory

```
02_ieee_report_4pages/
├── main.tex
├── refs.bib
├── sections/
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── materials_methods.tex
│   ├── development_doc.tex
│   ├── results_discussion.tex
│   ├── safety_limitations.tex
│   └── conclusion.tex
├── tables/
│   ├── table1.tex   % Pipeline and Evaluation Configuration
│   └── table2.tex   % Results and Acceptance Criteria
└── figures/
    └── (placeholder only)
```

## Compile

```bash
cd 02_ieee_report_4pages
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or use Overleaf: upload entire folder, set compiler to pdfLaTeX.

## Design Choices for 4-Page Limit

- **Sections merged from 16 to 7** (Abstract, Introduction, Materials and Methods, Development Documentation Summary, Results and Discussion, Safety/Limitations/Future Work, Conclusion).
- **Subsections minimized** to 4 in Materials and Methods, 1 in Results.
- **Tables reduced to 2** compact single-column-width tables.
- **Figures reduced to 1** placeholder pipeline diagram.
- **References limited to 8** entries; 5 are cited in text, 3 are supplementary.
- **Word budgets**: Abstract 150, Introduction 300, Materials/Methods 400, Development Doc 150, Results/Discussion 400, Safety/Limitations 250, Conclusion 120. Total ~1770 words.
- **No appendices**, no long clinical background, no long related work, no long regulatory discussion, no repeated safety disclaimers.
- Detailed documentation references moved to one sentence: "Detailed training logs, development timeline, failure analysis, and reproducibility notes are maintained as supplementary project documentation."

## Notes

- The `\fbox{\parbox{...}}` figure placeholder compiles without requiring an external image file. Replace with `\includegraphics` when the pipeline diagram is ready.
- Two `tab_` legacy table files from the full report are not used here; new compact `table1.tex` and `table2.tex` are used instead.
- No metrics were changed. All values match `KNOWN_METRICS.md`.
