# Contribution Statement

## NephroVision — Automated Kidney and Renal Tumor Segmentation System

This document defines the team's actual contributions to the NephroVision project. Each contribution is stated with what was done, why it matters, the evidence available in the workspace, and the boundaries of what should not be overclaimed.

---

## 1. Biomedical Problem Framing

**What was done:** We identified and framed the clinical problem of manual kidney and renal tumor segmentation in CT scans — a process that is time-consuming, costly, and subject to inter-observer variability. We defined the project scope as a decision-support prototype for automated segmentation and volumetric quantification, targeting radiologists, urologists, and medical engineers as intended users.

**Why it matters:** A well-defined problem framing ensures that the technical work addresses a real clinical need and that the system is positioned correctly as decision-support, not as an autonomous diagnostic tool. This framing guided every downstream design decision.

**Evidence/artifacts in the workspace:**
- `01_project_brief/problem_statement.md`
- `01_project_brief/one_page_summary.md`
- `MASTER_CONTEXT.md` — Problem Statement and System Overview sections
- `02_ieee_report/sections/02_introduction.tex`

**What should not be overclaimed:**
- We did not discover a new clinical condition.
- We did not conduct clinical research involving patients.
- We did not perform clinical validation with physicians.
- The problem framing is based on literature review and challenge context, not primary clinical research.

---

## 2. Dataset Preparation and Preprocessing

**What was done:** We explored the KiTS23 dataset, understood its structure, classes, and annotation conventions, and designed a reproducible preprocessing pipeline. We implemented NIfTI loading and validation, HU clipping to [-200, 300], and normalization to [0, 1]. We empirically evaluated preprocessing choices and documented the rationale for each parameter.

**Why it matters:** Preprocessing directly affects model performance. A consistent, well-documented preprocessing pipeline ensures reproducibility and provides a foundation for future external validation. The HU clipping range was selected to preserve kidney and tumor contrast while suppressing irrelevant structures.

**Evidence/artifacts in the workspace:**
- `07_development_documentation/preprocessing_decisions.md`
- `07_development_documentation/development_timeline.md` — Phase 3
- `02_ieee_report/sections/05_dataset_exploration.tex`
- `02_ieee_report/sections/06_development_process.tex` — Preprocessing Decisions subsection
- `MASTER_CONTEXT.md` — Dataset and Pipeline sections

**What should not be overclaimed:**
- We did not create, annotate, or modify the KiTS23 dataset.
- We did not collect clinical data.
- We did not design a novel preprocessing algorithm — we selected and documented standard techniques with task-specific parameters.
- The HU clipping range was validated empirically on KiTS23, not across multiple datasets.

---

## 3. Deep Learning Segmentation Pipeline

**What was done:** We implemented a 3D U-Net architecture for volumetric semantic segmentation of kidney and tumor/cyst from CT volumes. We configured the model for three classes (Background, Kidney, Tumor/Cyst), trained it on the KiTS23 training partition, and iterated on training configurations. We documented every experiment in the experiment log with hyperparameters, metrics, and decisions.

**Why it matters:** The 3D U-Net is the core of the segmentation system. Selecting 3D over 2D captures volumetric context across slices, which is essential for distinguishing tumors from adjacent structures. Documenting the training process ensures reproducibility and defense transparency.

**Evidence/artifacts in the workspace:**
- `07_development_documentation/model_training_documentation.md`
- `07_development_documentation/experiment_log.md` — EXP-001 through EXP-006
- `07_development_documentation/development_timeline.md` — Phases 4 and 5
- `02_ieee_report/sections/10_3d_unet_architecture.tex`
- `02_ieee_report/sections/08_training_and_inference.tex`
- `MASTER_CONTEXT.md` — Pipeline section

**What should not be overclaimed:**
- We did not invent the U-Net or 3D U-Net architecture.
- We did not invent a novel deep learning method.
- We did not conduct a systematic hyperparameter search (grid or Bayesian) — this is future work.
- Exact hyperparameters are documented in the experiment log; we do not present invented values.

---

## 4. Inference and Post-processing Pipeline

**What was done:** We designed and implemented a sliding-window inference pipeline with patch size 64×192×192 and 50% overlap to process full CT volumes within GPU memory constraints. We integrated test-time augmentation using 8 flip combinations to reduce boundary noise. We implemented connected-component post-processing to remove kidney blobs smaller than 5000 voxels and tumor blobs smaller than 100 voxels, with thresholds calibrated on the validation set.

**Why it matters:** The inference pipeline determines how the trained model is applied to new data. Sliding-window inference enables processing of arbitrarily large volumes. Post-processing reduces false positives while preserving small true lesions, which is critical for tumor detection sensitivity.

**Evidence/artifacts in the workspace:**
- `07_development_documentation/engineering_decisions.md`
- `07_development_documentation/experiment_log.md` — EXP-003, EXP-004, EXP-005
- `07_development_documentation/development_timeline.md` — Phases 6 and 7
- `02_ieee_report/sections/08_training_and_inference.tex` — Inference Configuration subsection
- `02_ieee_report/sections/12_post_processing.tex`
- `MASTER_CONTEXT.md` — Pipeline section

**What should not be overclaimed:**
- We did not invent sliding-window inference or test-time augmentation — these are established techniques.
- We did not prove that our post-processing thresholds are optimal — they were empirically selected on the validation set.
- We did not claim real-time inference — inference time is documented but not optimized.

---

## 5. Web Visualization System

**What was done:** We designed and implemented a browser-based web application that accepts NIfTI CT volume uploads, runs the full inference pipeline, and displays the 3D segmentation mesh alongside kidney and tumor volumetric statistics. The system provides interactive visualization without requiring specialized software.

**Why it matters:** A web-based interface makes the system accessible to medical professionals without specialized imaging software. The visualization supports physician review by allowing side-by-side comparison of the original CT and the predicted segmentation mask, which is essential for the decision-support workflow.

**Evidence/artifacts in the workspace:**
- `03_final_presentation/slidev/` — presentation includes web application slide
- `02_ieee_report/sections/09_software_system_design.tex`
- `07_development_documentation/development_timeline.md` — Phase 8
- `03_final_presentation/speaker_notes.md` — Slide 14 notes

**What should not be overclaimed:**
- We did not deploy the system in a clinical environment.
- We did not conduct formal usability testing with physicians — this is future work.
- We did not implement cybersecurity hardening for production deployment.
- The web application is an academic prototype, not a production-ready system.

---

## 6. Quantitative Evaluation

**What was done:** We evaluated the final pipeline on 64 independent held-out test cases from KiTS23. We computed Dice score, Hausdorff Distance (HD95), and tumor detection rate for kidney and tumor/cyst. We reported results with standard deviations and interpreted the performance gap between kidney and tumor segmentation honestly.

**Why it matters:** Quantitative evaluation on an independent test set provides an honest estimate of system performance within the KiTS23 distribution. Reporting both Dice and HD95 gives a complete picture of overlap accuracy and boundary error. Distinguishing detection rate from boundary precision prevents misinterpretation of the moderate tumor Dice.

**Evidence/artifacts in the workspace:**
- `KNOWN_METRICS.md` — all validated metrics
- `02_ieee_report/sections/10_evaluation_results.tex`
- `07_development_documentation/experiment_log.md` — EXP-006 and Final Validated Metrics
- `MASTER_CONTEXT.md` — Validation Metrics section
- `03_final_presentation/slidev/slides.md` — Results slide

**Verified results:**

| Metric | Kidney | Tumor |
|--------|--------|-------|
| Dice Score | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| HD95 (mm) | 19.98 | 67.35 |

- Mean Dice: 0.7933
- Tumor Detection Rate: 64/64 = 100%

**What should not be overclaimed:**
- We did not conduct external validation on non-KiTS23 data.
- We did not perform a prospective clinical trial.
- We did not compare our results against radiologist performance.
- We did not claim clinical adequacy — results are contextualized within KiTS23 difficulty.
- Tumor Dice of 0.6558 reflects boundary precision, not detection failure — detection is 100%.

---

## 7. Safety and IEC 62304 Documentation

**What was done:** We classified NephroVision under IEC 62304 Software Safety Class B and documented the intended use, intended users, and decision-support boundaries. We identified known regulatory gaps including cybersecurity, post-market surveillance, and clinical validation. We established safe wording rules enforced across all documentation, slides, and speaker notes.

**Why it matters:** Regulatory awareness demonstrates engineering maturity and patient safety consciousness. Even as an academic prototype, framing the system under a recognized standard ensures that limitations are documented and that no overclaiming occurs in defense materials.

**Evidence/artifacts in the workspace:**
- `DO_NOT_OVERCLAIM.md`
- `PROJECT_RULES.md` — Safety Wording Rules section
- `02_ieee_report/sections/12_safety_regulatory.tex`
- `MASTER_CONTEXT.md` — Safety and Regulatory section
- `04_defense_qna/expected_questions.md` — Safety-related Q&A entries

**What should not be overclaimed:**
- We did not achieve full IEC 62304 compliance — we adopted the classification and documented boundaries.
- We did not obtain regulatory approval of any kind.
- We did not complete a risk management file or full software lifecycle documentation.
- We did not conduct cybersecurity hardening or post-market surveillance planning beyond identification of gaps.

---

## 8. Development Documentation after Mid-Year Feedback

**What was done:** After receiving mid-year feedback requesting more thorough documentation, we created a structured development documentation package covering the full engineering journey. We documented the development timeline, experiment log, model training documentation, preprocessing decisions, engineering decisions, challenges and solutions, cyst and tumor detection challenges, failure cases analysis, ablation and iteration summary, reproducibility notes, and lessons learned. We established a rule that no undocumented experiment may be presented as completed.

**Why it matters:** This documentation directly addresses the mid-year feedback and demonstrates that the team can document an engineering process systematically, not just report final results. It provides the defense committee with evidence of iterative development, honest challenge assessment, and reproducibility commitment.

**Evidence/artifacts in the workspace:**
- `07_development_documentation/README.md`
- `07_development_documentation/development_timeline.md`
- `07_development_documentation/experiment_log.md`
- `07_development_documentation/model_training_documentation.md`
- `07_development_documentation/preprocessing_decisions.md`
- `07_development_documentation/challenges_and_solutions.md`
- `07_development_documentation/cyst_and_tumor_detection_challenges.md`
- `07_development_documentation/failure_cases_analysis.md`
- `07_development_documentation/engineering_decisions.md`
- `07_development_documentation/ablation_or_iteration_summary.md`
- `07_development_documentation/reproducibility_notes.md`
- `07_development_documentation/lessons_learned.md`
- `MASTER_CONTEXT.md` — Mid-Year Feedback Response section

**What should not be overclaimed:**
- We did not retroactively invent experiments — the log records what was actually done.
- We did not claim a systematic hyperparameter search was performed if it was not.
- Unknown details are marked as TODO and must be completed by the team with actual data.
- The documentation is comprehensive but not complete — some TODO placeholders remain.

---

## Short Presentation-Ready Version

### NephroVision — Team Contributions

1. **Problem framing:** We defined the clinical problem of manual kidney and tumor segmentation and scoped the project as a decision-support prototype.
2. **Preprocessing:** We designed and documented a reproducible pipeline with HU clipping [-200, 300] and normalization [0, 1].
3. **Segmentation model:** We implemented a 3D U-Net for volumetric segmentation and trained it on KiTS23 with documented experiments.
4. **Inference and post-processing:** We built a sliding-window inference pipeline with 8-flip TTA and conservative blob removal thresholds.
5. **Web visualization:** We developed a browser-based 3D viewer for segmentation display and volumetric reporting.
6. **Evaluation:** We evaluated on 64 held-out test cases — Kidney Dice 0.9307, Tumor Dice 0.6558, Detection 100%.
7. **Safety documentation:** We classified the system under IEC 62304 Class B and established decision-support boundaries.
8. **Development documentation:** We documented the full engineering process after mid-year feedback, including experiments, challenges, and failure analysis.

---

## One-Sentence Version (for Final Conclusion)

We implemented, evaluated, and documented a 3D U-Net-based decision-support prototype for automated kidney and renal tumor/cyst segmentation from CT volumes, achieving robust kidney segmentation (Dice 0.9307), reliable tumor detection (100%), and honest documentation of the development process, challenges, and limitations.

---

**This contribution statement is consistent with MASTER_CONTEXT.md, KNOWN_METRICS.md, DO_NOT_OVERCLAIM.md, and the development documentation in 07_development_documentation/.**
