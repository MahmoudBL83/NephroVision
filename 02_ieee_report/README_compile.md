# IEEE Report --- Compilation Instructions

## File Structure

```
02_ieee_report/
├── main.tex                    % Root document
├── refs.bib                    % BibTeX bibliography (verified + placeholder entries)
├── sections/                   % Per-section .tex files
│   ├── 01_abstract.tex
│   ├── 02_introduction.tex
│   ├── 03_clinical_background.tex
│   ├── 04_related_work.tex
│   ├── 05_dataset_exploration.tex
│   ├── 06_development_process.tex
│   ├── 07_methodology.tex
│   ├── 08_training_and_inference.tex
│   ├── 09_software_system_design.tex
│   ├── 10_evaluation_results.tex
│   ├── 11_challenges_failure_analysis.tex
│   ├── 12_safety_regulatory.tex
│   ├── 13_discussion.tex
│   ├── 14_limitations.tex
│   ├── 15_future_work.tex
│   └── 16_conclusion.tex
├── tables/                     % Standalone table .tex files
│   ├── dataset_configuration.tex        % (new) dataset and system config
│   ├── performance_metrics.tex          % (new) final test metrics
│   ├── acceptance_criteria.tex          % (new) targets vs achieved
│   ├── development_artifacts.tex        % (new) documentation artifacts
│   ├── risk_mitigation_summary.tex      % (new) risk and mitigation
│   ├── tab_dataset_config.tex           % (legacy) old dataset config
│   ├── tab_performance_metrics.tex      % (legacy) old performance table
│   ├── tab_acceptance_criteria.tex      % (legacy) old acceptance table
│   ├── tab_dev_artifacts.tex            % (legacy) old artifacts table
│   └── tab_risk_mitigation.tex          % (legacy) old risk table
├── figures/                    % Figure source files (optional)
│   ├── fig_pipeline.pdf        % System pipeline diagram (optional)
│   ├── fig_architecture.pdf    % 3D U-Net architecture (optional)
│   ├── fig_inference.pdf       % Inference workflow (optional)
│   ├── fig_webapp.pdf          % Web application screenshot (optional)
│   └── fig_results.pdf         % Results summary (optional)
└── build/                      % Compiled output
```

> **Note:** New table files (without `tab_` prefix) are referenced from the section files. Legacy `tab_` prefixed files are retained for backward compatibility but are not currently input.

## Compile Steps

### Option 1: Command Line (recommended)

```bash
# Step 1: Compile main document (generates .aux, may show undefined references)
pdflatex main.tex

# Step 2: Process bibliography (resolves citation keys from refs.bib)
bibtex main

# Step 3: Resolve cross-references (run twice to stabilize labels and citations)
pdflatex main.tex
pdflatex main.tex
```

### Option 2: latexmk (auto-resolve)

```bash
latexmk -pdf main.tex
```

### Option 3: Overleaf

Upload the entire `02_ieee_report/` folder to Overleaf. Set `main.tex` as the main document. Overleaf compiles automatically.

## Placeholder Figures

All `\includegraphics` lines for figures are commented out by default so the document compiles even when figure files are missing. Placeholder `\fbox{\parbox{...}}` boxes render instead. To enable a figure:

1. Place the PDF/PNG file in `figures/`
2. Uncomment the `\includegraphics` line in the relevant section
3. Remove or keep the `\fbox` placeholder as needed

## Placeholder Tables

All tables are in `tables/*.tex` and are `\input{}` from the relevant sections. Fill the table cells with actual data before submission.

## Known Compile Warnings

- `Citation XXX undefined` --- expected for placeholder citations marked TODO in `refs.bib`. Replace with verified entries before submission.
- `Reference XXX undefined` --- expected on first compile; resolved after `bibtex` + second `pdflatex`
- `Float too large for page` --- may occur with placeholder boxes; will resolve when real figures are inserted
- `There were undefined references` --- expected before second `pdflatex` pass; resolved after full compile cycle

## Critical Fixes Applied

1. **Nested abstract/keywords removed from `main.tex`:** `01_abstract.tex` contains its own `\begin{abstract}` and `\begin{IEEEkeywords}` environments. `main.tex` no longer wraps them, preventing nested-environment errors.
2. **Section references corrected:** Hardcoded Roman-numeral section references (`Section~XI`, `Section~XII`, `Section~XIV`) were corrected to match actual section ordering.
3. **Placeholder bib entries added:** All citation keys used in the text now have placeholder entries in `refs.bib` to prevent undefined-citation errors.
4. **`\usepackage[utf8]{inputenc}` added to `main.tex`:** Ensures UTF-8 special characters in `refs.bib` compile correctly.

## Final Checklist Before Submission

- [ ] All TODO placeholder citations in `refs.bib` replaced with verified entries
- [ ] All TODO comments in section files addressed or removed
- [ ] All placeholder figures replaced with final versions (optional for draft)
- [ ] All tables filled with verified data
- [ ] Metrics match `KNOWN_METRICS.md` exactly
- [ ] Abstract length: 150--250 words
- [ ] Paper length: 6--8 pages for IEEE conference format
- [ ] Compile completes without errors (warnings acceptable)
