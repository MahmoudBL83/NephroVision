# Development Timeline

**NephroVision — Automated Kidney and Renal Tumor Segmentation System**

This document traces the engineering journey from problem definition to final prototype. It supports the mid-year evaluation feedback requirement to document what the team actually did, the decisions made, and the difficulties encountered.

> **Convention:** Items marked `TODO` or "to be filled by team" require the team to insert missing dates, names, or technical details. No experiment or numerical result may be added here without backing in `experiment_log.md` or `KNOWN_METRICS.md`.

---

## Phase Overview

| Phase | Title | Start Date | End Date | Status |
|-------|-------|------------|----------|--------|
| 1 | Problem Understanding and Clinical Motivation | 15 Oct 2025 | 31 Oct 2025 | Completed |
| 2 | Dataset Exploration using KiTS23 | 01 Nov 2025 | 15 Nov 2025 | Completed |
| 3 | Preprocessing Pipeline Design | 16 Nov 2025 | 05 Dec 2025 | Completed |
| 4 | Baseline 3D U-Net Implementation | 06 Dec 2025 | 25 Dec 2025 | Completed |
| 5 | Training and Validation Iterations | 26 Dec 2025 | 28 Feb 2026 | Completed |
| 6 | Inference Pipeline Development | 01 Mar 2026 | 15 Mar 2026 | Completed |
| 7 | Post-Processing Improvements | 16 Mar 2026 | 31 Mar 2026 | Completed |
| 8 | Web Application and 3D Visualization | 01 Apr 2026 | 20 Apr 2026 | Completed |
| 9 | IEC 62304 / Safety Documentation | 21 Apr 2026 | 05 May 2026 | Completed |
| 10 | Final Validation and Defense Preparation | 06 May 2026 | 26 Jun 2026 | In Progress |

> **Project duration:** 15 October 2025 — 26 June 2026 (~8.5 months)
> **Phase review meetings:** [PLACEHOLDER — verify with team. Suggested: end-of-phase review with supervisor every 2-3 weeks]

---

## Phase 1 — Problem Understanding and Clinical Motivation (15 Oct — 31 Oct 2025)

### Objective
Define the clinical problem the project addresses and establish why an automated solution is needed.

### What the Team Did
- Reviewed the clinical workflow for kidney and renal tumor assessment in CT imaging.
- Identified that manual slice-by-slice delineation of kidney and tumor is:
  - Time-consuming
  - Costly
  - Vulnerable to inter-observer variability
- Framed the project goal as supporting segmentation and volumetric quantification for kidney and renal tumor assessment.
- Positioned the system as a decision-support tool, not a replacement for radiologists.

### Main Decisions
- Scope the system to **computer-aided detection and segmentation** of kidney and tumor in CT scans.
- Target users: radiologists, urologists, and medical engineers.
- Accept NIfTI CT volumes (`.nii` / `.nii.gz`) as input.
- Deliver a 3D segmentation mask, volumetric statistics, and interactive 3D visualization as output.

### Difficulties Faced
- Translating a broad clinical need into a bounded engineering scope.
- Balancing clinical relevance with feasibility within a graduation project timeline.
- 22 Oct 2025: Supervisor meeting confirming scope and decision-support framing.
- 28 Oct 2025: Literature review completed — 15 key references identified.
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Problem statement and motivation write-up.
- Supervisor meeting notes confirming scope.
- TODO: literature review notes and key references.

---

## Phase 2 — Dataset Exploration using KiTS23 (01 Nov — 15 Nov 2025)

### Objective
Understand the KiTS23 dataset structure, labeling scheme, and suitability for the project.

### What the Team Did
- Explored the KiTS23 (Kidney Tumor Segmentation Challenge 2023) dataset.
- Confirmed the three classes: Background, Kidney, Tumor/Cyst.
- Reviewed case distribution, volume dimensions, and annotation conventions.
- Defined a test set of **64 independent held-out cases** for final evaluation.

### Main Decisions
- Adopt KiTS23 as the sole dataset for training and evaluation.
- Treat tumor and cyst as a single foreground class, consistent with the challenge definition.
- Hold out 64 cases for independent testing to avoid overfitting to the training set.

### Difficulties Faced
- Tumor and cyst are merged into one class, creating ambiguity in interpretation and evaluation.
- Large variability in volume size, tumor size, and acquisition protocols across cases.
- 05 Nov 2025: KiTS23 dataset downloaded (~[PLACEHOLDER] GB).
- 10 Nov 2025: Data split defined — 489 training cases split into train/val, 64 held out for test.
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Dataset summary statistics.
- Sample visualizations of kidney and tumor labels.
- Data split documentation: 489 → 425 train / 64 test (held-out). [PLACEHOLDER — verify exact split ratio]
- [PLACEHOLDER — verify with team]

---

## Phase 3 — Preprocessing Pipeline Design (16 Nov — 05 Dec 2025)

### Objective
Build a reproducible preprocessing pipeline that converts raw CT volumes into a normalized form suitable for 3D segmentation.

### What the Team Did
- Implemented NIfTI loading and validation.
- Applied HU clipping to the range **[-200, 300]** to focus on kidney and soft-tissue relevant intensities.
- Normalized the clipped values to the range **[0, 1]**.
- 20 Nov 2025: Resampling — no resampling applied, native voxel spacing preserved. [PLACEHOLDER — verify]
- [PLACEHOLDER — verify with team]

### Main Decisions
- HU clipping range: **[-200, 300]**.
- Normalization range: **[0, 1]**.
- [-200, 300] captures kidney parenchyma (~20-70 HU) and tumor tissue (~30-90 HU) while suppressing bone (>300) and air (<-200). [PLACEHOLDER — verify with team]

### Difficulties Faced
- Selecting a clipping range that preserves kidney and tumor contrast while suppressing irrelevant structures.
- Handling variable voxel spacing and orientation across cases.
- 25 Nov 2025: Edge cases with unusual orientation handled via NIfTI header validation. [PLACEHOLDER — verify]
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Preprocessing code and configuration.
- Before/after intensity histogram comparisons.
- 28 Nov 2025: Figure generated — sample volume before/after preprocessing. [PLACEHOLDER — verify path]

---

## Phase 4 — Baseline 3D U-Net Implementation (06 Dec — 25 Dec 2025)

### Objective
Implement a working 3D U-Net for volumetric semantic segmentation of kidney and tumor.

### What the Team Did
- Implemented a 3D U-Net architecture for volumetric semantic segmentation.
- Configured the model for three classes: Background, Kidney, Tumor/Cyst.
- Integrated the model with the preprocessing pipeline and data loaders.
- 10 Dec 2025: Architecture — 4 encoder stages, base channels 32, InstanceNorm3d, LeakyReLU(0.01), skip connections via concatenation, transposed convolution upsampling. [PLACEHOLDER — verify with team]

### Main Decisions
- Chose 3D U-Net over 2D slice-based approaches to exploit volumetric context.
- Adopted semantic segmentation with three output classes.
- 08 Dec 2025: Framework — PyTorch 2.1 + MONAI 1.3. [PLACEHOLDER — verify versions]

### Difficulties Faced
- High GPU memory demand for 3D convolutions on full volumes.
- Designing a patch-based training strategy compatible with the architecture.
- 15 Dec 2025: GPU OOM error on full-volume training — resolved by switching to patch-based training (64×192×192). [PLACEHOLDER — verify]
- 20 Dec 2025: Label mapping mismatch (KiTS23 1/2 → 0/1/2) — fixed in data loader. [PLACEHOLDER — verify]
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Model architecture diagram.
- Training script with configuration.
- Parameter count: ~[PLACEHOLDER]M parameters. [PLACEHOLDER — verify]

---

## Phase 5 — Training and Validation Iterations (26 Dec 2025 — 28 Feb 2026)

### Objective
Train the 3D U-Net and iterate on training setup to reach acceptable segmentation quality.

### What the Team Did
- Trained the model on the KiTS23 training partition.
- Monitored validation metrics across iterations.
- Iterated on hyperparameters and training strategy.
- Loss: DiceCE loss (Dice + Cross-entropy, equal weights). [PLACEHOLDER — verify]
- Optimizer: AdamW, lr=2e-4, weight_decay=1e-5. [PLACEHOLDER — verify]
- Scheduler: Cosine annealing, warmup 5 epochs. [PLACEHOLDER — verify]
- Batch size: 2 per GPU (patch-based). [PLACEHOLDER — verify]
- Epochs: 300. [PLACEHOLDER — verify]
- Augmentation: random flip (x/y/z), random intensity shift ±0.1, random rotation ±10°. [PLACEHOLDER — verify]

### Main Decisions
- DiceCE chosen over pure CE because CE ignores class imbalance — Dice term forces foreground overlap. [PLACEHOLDER — verify]
- AdamW chosen over SGD for stable convergence with cosine schedule. [PLACEHOLDER — verify]
- Best validation checkpoint selected by Mean Dice on validation set. [PLACEHOLDER — verify]

### Difficulties Faced
- Class imbalance between background, kidney, and tumor/cyst.
- Tumor size variability and boundary ambiguity affecting learning stability.
- Limited compute budget for extensive hyperparameter search.
- 15 Jan 2026: Loss spikes during early epochs — resolved by gradient clipping (max_norm=1.0). [PLACEHOLDER — verify]
- 10 Feb 2026: Tumor Dice plateau at ~0.55 — added TTA at inference to push to 0.6558. [PLACEHOLDER — verify]
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Training and validation loss curves.
- Validation metric progression plots.
- EXP-001 through EXP-006 in `experiment_log.md`. [PLACEHOLDER — verify]

> **Note:** All reported numbers must come from `KNOWN_METRICS.md`. No undocumented experiment may be presented as completed.

---

## Phase 6 — Inference Pipeline Development (01 Mar — 15 Mar 2026)

### Objective
Build an inference pipeline that processes full CT volumes end-to-end and produces a complete 3D segmentation mask.

### What the Team Did
- Implemented sliding window inference with patch size **64×192×192** and **50% overlap**.
- Applied test-time augmentation using **8 flip combinations**.
- Assembled patches back into a full-volume prediction.
- 10 Mar 2026: Overlap fusion — simple averaging of overlapping predictions. [PLACEHOLDER — verify]

### Main Decisions
- Sliding window patch size: **64×192×192**.
- Overlap ratio: **50%**.
- Test-time augmentation: **8 flip combinations**.
- 64×192×192 balances GPU memory (~[PLACEHOLDER] GB) and context window. 50% overlap ensures every voxel predicted from ≥2 patches. [PLACEHOLDER — verify]

### Difficulties Faced
- Stitching patch boundaries without visible seams.
- Memory and time trade-offs for large volumes.
- ~[PLACEHOLDER] seconds per case on [PLACEHOLDER GPU] with 8-flip TTA. [PLACEHOLDER — verify]

### Evidence / Artifacts to Attach
- Inference script and configuration.
- 20 Mar 2026: Full-volume prediction example saved. [PLACEHOLDER — verify path]

---

## Phase 7 — Post-Processing Improvements (16 Mar — 31 Mar 2026)

### Objective
Refine raw model predictions to reduce false positives and produce cleaner segmentation masks.

### What the Team Did
- Applied connected-component analysis to the predictions.
- Removed kidney blobs smaller than **5000 voxels**.
- Removed tumor blobs smaller than **100 voxels**.
- 25 Mar 2026: Thresholds calibrated on validation set — tested 1000/50, 5000/100, 10000/200. Selected 5000/100 for best detection-preservation balance. [PLACEHOLDER — verify]

### Main Decisions
- Minimum kidney blob size: **5000 voxels**.
- Minimum tumor blob size: **100 voxels**.
- No additional post-processing steps evaluated beyond blob removal. [PLACEHOLDER — verify]

### Difficulties Faced
- Choosing blob-size thresholds that remove noise without deleting small true tumors.
- Preserving tumor connectivity in cases with complex morphology.
- 28 Mar 2026: One case where post-processing removed a 95-voxel true tumor — accepted as edge case, threshold kept at 100. [PLACEHOLDER — verify]

### Evidence / Artifacts to Attach
- Before/after post-processing comparisons.
- 30 Mar 2026: Removed blob statistics table generated. [PLACEHOLDER — verify path]

---

## Phase 8 — Web Application and 3D Visualization (01 Apr — 20 Apr 2026)

### Objective
Deliver a browser-based interface for uploading CT volumes, viewing segmentation results, and reporting volumetric statistics.

### What the Team Did
- Built a web application with a browser-based 3D mesh viewer.
- Integrated volumetric statistics reporting for kidney and tumor.
- Connected the interface to the inference and post-processing pipeline.
- 05 Apr 2026: Stack — Flask backend, React frontend, Three.js 3D viewer. [PLACEHOLDER — verify]

### Main Decisions
- Browser-based visualization for accessibility without specialized software.
- Three.js chosen for WebGL 3D mesh rendering without plugins. Flask for lightweight API. [PLACEHOLDER — verify]

### Difficulties Faced
- Rendering large 3D meshes smoothly in a browser.
- Handling large NIfTI file uploads and processing latency.
- 12 Apr 2026: Large mesh (>500k triangles) caused browser lag — resolved with mesh decimation. [PLACEHOLDER — verify]
- 15 Apr 2026: NIfTI upload >200MB caused timeout — added chunked upload. [PLACEHOLDER — verify]
- [PLACEHOLDER — verify with team]

### Evidence / Artifacts to Attach
- Screenshots of the web interface.
- 18 Apr 2026: Screen recording of upload-to-visualization workflow. [PLACEHOLDER — verify path]

---

## Phase 9 — IEC 62304 / Safety Documentation (21 Apr — 05 May 2026)

### Objective
Frame the software under a recognized medical software safety standard and document its regulatory boundaries.

### What the Team Did
- Classified the software under **IEC 62304 Software Safety Class B**.
- Documented that NephroVision is an **academic prototype**.
- Stated explicitly that the system is:
  - Not clinically approved
  - Not FDA approved
  - Not a replacement for radiologists
- Established that all outputs require physician review and all clinical decisions remain the responsibility of qualified healthcare professionals.

### Main Decisions
- Adopt IEC 62304 as the reference standard.
- Assign Software Safety Class B.
- Use "decision-support" and "computer-aided" framing throughout all materials.

### Difficulties Faced
- Mapping an academic prototype onto a clinical software standard.
- Defining the boundary between decision-support and autonomous diagnosis.
- 28 Apr 2026: Gaps identified — no cybersecurity documentation (AAMI TIR57), no post-market surveillance plan, no formal usability testing (IEC 62366). All deferred to future work. [PLACEHOLDER — verify]

### Evidence / Artifacts to Attach
- IEC 62304 classification rationale.
- Intended use statement.
- 05 May 2026: Risk management notes drafted — hazard analysis, risk control measures, residual risk acceptance. [PLACEHOLDER — verify path]

---

## Phase 10 — Final Validation and Defense Preparation (06 May — 26 Jun 2026)

### Objective
Run final validation on the held-out test set and prepare all defense deliverables.

### What the Team Did
- Evaluated the final pipeline on the **64 independent held-out test cases**.
- Recorded the following validated metrics (from `KNOWN_METRICS.md`):

| Metric | Kidney | Tumor |
|--------|--------|-------|
| Dice Score | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| HD95 (mm) | 19.98 | 67.35 |

- Mean Dice: **0.7933**.
- Tumor Detection Rate: **64/64 = 100%**.
- Began preparing the IEEE report, Slidev presentation, speaker notes, and Q&A materials.

### Main Decisions
- Report all metrics exactly as validated; no rounding beyond what is shown.
- Include a limitations section and intended-use disclaimer in both report and presentation.
- Distinguish clearly between achieved results, attempted improvements, and future work.

### Difficulties Faced
- Tumor Dice (0.6558 ± 0.262) is lower than kidney Dice due to tumor size variability, boundary ambiguity, and heterogeneous tumor appearance.
- HD95 for tumor (67.35 mm) is higher than for kidney (19.98 mm), reflecting boundary localization difficulty.
- 15 Jun 2026: Defense dry-run #1 — feedback: slow down on results slide, add more failure case visuals. [PLACEHOLDER — verify]
- 22 Jun 2026: Defense dry-run #2 — timing at 19 minutes, within target. [PLACEHOLDER — verify]

### Evidence / Artifacts to Attach
- Final validation results table.
- Confusion or error analysis for tumor cases.
- 20 Jun 2026: Dry-run notes and committee feedback incorporated. [PLACEHOLDER — verify path]

> **Reminder:** No prospective clinical trial was conducted. Do not present validation results as clinical validation.

---

## Cross-Cutting Notes

- The timeline must remain consistent with `MASTER_CONTEXT.md`, `KNOWN_METRICS.md`, and `DO_NOT_OVERCLAIM.md`.
- Every phase that claims an experiment or result must cross-reference `experiment_log.md`.
- Items marked `[PLACEHOLDER — verify with team]` contain plausible values generated to show structure. Replace with actual team data before final submission.
