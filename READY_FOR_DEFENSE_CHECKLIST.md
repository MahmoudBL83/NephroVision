# Ready for Defense Checklist

> Master checklist for NephroVision final defense preparation. Tick items as they are completed.

---

## PRESENTATION (03_final_presentation/slidev/)

### Structure & Content
- [x] 28 slides created with complete content
- [x] Section numbers added (01-10) to all relevant slides
- [x] Speaker notes written for every slide
- [x] Safety badges and decision-support framing throughout
- [x] All metrics match KNOWN_METRICS.md exactly
- [x] No overclaiming language (no "diagnosis", "FDA approved", etc.)

### Visual Design
- [x] Academic gravitas theme (white bg, Inter + Crimson Text)
- [x] Color palette: deep navy #1e3a5f, forest green #2d6a4f, terracotta #bc4b31, crimson #9b2c2c
- [x] 8 SVG diagrams created and referenced
- [x] Arrow icons added to pipeline slides
- [x] Numbered step circles on key slides

### Compilation
- [x] `npm install` succeeds for dev mode
- [x] Dev server runs without errors (`npm run dev`)
- [ ] PPTX export tested (blocked by disk space — needs Chrome/Playwright)
- [ ] Final run-through with timer (recommended: 18-20 minutes)

### Placeholders to Replace
- [ ] Slide 2: Fill [TODO] clinical statistics (minutes per case, inter-observer Dice)
- [ ] Slide 4: Fill [TODO] typical slice count
- [ ] Slide 5: Fill [TODO] total cases, training/validation split, multi-center count
- [ ] Slide 5: Generate dataset distribution chart
- [ ] Slide 7: Replace pipeline SVG if needed
- [ ] Slide 10: Replace architecture diagram placeholder with actual 3D U-Net diagram
- [ ] Slide 14: Replace web app screenshot placeholder with actual screenshot
- [ ] Slide 16: Generate results bar chart (Kidney vs Tumor Dice/HD95)
- [ ] Slide 21+: Add actual dates to development timeline SVG

---

## IEEE REPORT (02_ieee_report/)

### Structure
- [x] main.tex with all 16 sections
- [x] refs.bib with 29 entries (10 verified, 19 placeholders)
- [x] All 26 citation keys used in sections have bib entries
- [x] README_compile.md with compile instructions
- [ ] **Compile test:** Run `pdflatex -> bibtex -> pdflatex -> pdflatex` and verify zero errors
- [ ] Fix any compilation warnings (overfull/underfull boxes, etc.)

### Content Verification
- [x] No nested abstract/keywords in main.tex
- [x] 6 hardcoded section references fixed
- [x] UTF-8 inputenc added
- [ ] Verify all figures are included and referenced correctly
- [ ] Verify all tables compile correctly
- [ ] Cross-check: do section contents match presentation narrative?

### Placeholders to Replace
- [ ] refs.bib: Replace 19 TODO placeholder citations with verified IEEE entries
- [ ] Section 4 (Related Work): Fill TODO [cite KiTS23 leaderboard]
- [ ] Section 10 (Results): Add per-case metric distributions

---

## IEEE CONDENSED PAPER (02_ieee_report_condensed/)

- [x] 4-page paper with 7 sections
- [x] Tables for preprocessing, architecture, results, acceptance criteria
- [ ] Compile and verify no errors
- [ ] Ensure consistency with full report

---

## DEVELOPMENT DOCUMENTATION (07_development_documentation/)

### Documents Created
- [x] `experiment_log.md` — 6 EXP entries with template structure
- [x] `failure_cases_analysis.md` — 7 failure categories + 3 concrete cases (FC-001/002/003)
- [x] `development_timeline.md` — 10 phases with decisions and difficulties
- [x] `model_training_documentation.md` — Full training record template
- [x] `preprocessing_decisions.md` — **NEW** — HU clipping rationale, normalization, standardization
- [x] `engineering_decisions.md` — **NEW** — 3D vs 2D, sliding window, TTA, post-processing, web app
- [x] `ablation_or_iteration_summary.md` — **NEW** — 6 iterations + failed experiments template
- [x] `reproducibility_notes.md` — **NEW** — environment, seeds, commands, checkpoints
- [x] `lessons_learned.md` — **NEW** — what worked, what was hard, advice for future teams
- [x] `challenges_and_solutions.md`
- [x] `cyst_and_tumor_detection_challenges.md`

### Team TODOs (Require Actual Data)
- [ ] **experiment_log.md**: Fill EXP-001 through EXP-006 with actual hyperparameters, dates, metrics
- [ ] **model_training_documentation.md**: Fill architecture details, loss, optimizer, LR, batch, epochs, hardware
- [ ] **preprocessing_decisions.md**: Fill actual tested HU ranges with validation results
- [ ] **engineering_decisions.md**: Fill actual technology stack for web app
- [ ] **ablation_or_iteration_summary.md**: Fill actual validation metrics per iteration + 1-2 failed experiments
- [ ] **reproducibility_notes.md**: Fill hardware specs, software versions, random seeds, exact commands
- [ ] **lessons_learned.md**: Fill skills developed with team member names
- [ ] **failure_cases_analysis.md**: Fill FC-001/002/003 with real anonymized case data and figures
- [ ] **development_timeline.md**: Add project start/end dates and phase review dates

---

## Q&A PREPARATION (04_defense_qna/)

- [x] 42 expected questions with model answers
- [ ] Practice answering top 10 most likely questions aloud
- [ ] Prepare 1-minute "elevator pitch" version of answers for tough questions

---

## PROJECT BRIEF (01_project_brief/)

- [x] defense_storyline.md
- [x] mid_year_feedback_response.md
- [ ] Review all brief documents for consistency with final materials

---

## CONTROL FILES

- [x] `MASTER_CONTEXT.md` — Single source of truth, KiTS23 vs project split clarified
- [x] `KNOWN_METRICS.md` — Locked validated numbers
- [x] `DO_NOT_OVERCLAIM.md` — 11 non-negotiable rules
- [x] `README.md` — Project overview

---

## CRITICAL RULES (Do Not Break)

1. [x] Never claim FDA/regulatory approval
2. [x] Never claim autonomous diagnosis
3. [x] Never claim solved tumor/cyst segmentation
4. [x] Never present 64-case subset as official KiTS23 test set
5. [x] Never claim official leaderboard ranking
6. [x] Always distinguish official dataset from project-specific evaluation
7. [x] All metrics match KNOWN_METRICS.md exactly
8. [x] Max 4 bullets per presentation slide
9. [x] Decision-support framing enforced throughout
10. [x] Use TODO markers for unknown details
11. [x] No invented hyperparameters or experiments

---

## PRE-DEFENSE REHEARSAL CHECKLIST

### 1 Week Before
- [ ] Replace all [TODO] and PLACEHOLDER items in slides
- [ ] Generate all final figures (architecture, screenshot, results chart)
- [ ] Compile IEEE report successfully (zero errors)
- [ ] Test PPTX export (install Chrome if needed, or use PDF fallback)
- [ ] Print/export speaker notes for reference

### 2 Days Before
- [ ] Full dry-run with timer (target: 18-20 minutes for 28 slides)
- [ ] Practice Q&A with team members playing committee roles
- [ ] Verify all laptops, adapters, and presentation files are ready
- [ ] Prepare backup: PDF export + USB drive with all files

### Day Of
- [ ] Arrive early to test projector resolution
- [ ] Verify slide aspect ratio matches projector (16:9)
- [ ] Have MASTER_CONTEXT.md and KNOWN_METRICS.md printed for reference
- [ ] Bring printed speaker notes

---

## DISK SPACE ISSUE

**Problem:** PPTX export requires Playwright Chromium (~183 MB). C: drive has ~994 MB free but download fails.

**Workarounds:**
1. Free up disk space (clean temp files, uninstall unused programs)
2. Install Chrome/Chromium separately and configure Playwright to use it
3. Use PDF export as fallback (if acceptable to committee)
4. Export on a different machine with more disk space

---

Last updated: [TODO: Add date]
