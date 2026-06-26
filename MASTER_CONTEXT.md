# NephroVision — Master Context

**Single source of truth for all report, presentation, speaker notes, and Q&A generation.**

---

## Project Identity

- **Project Name:** NephroVision
- **Full Title:** Automated Kidney and Renal Tumor Segmentation System
- **Field:** Biomedical / Medical Engineering
- **Department:** Medical Engineering Department, Graduation Project
- **Supervisor:** Hisham Abdeltawab, Ph.D.
- **Team Members:**
  - Rashed Mamdouh
  - Mohamed Walid
  - Mahmoud BahaaAldeen
  - Mahmoud Mohammed
  - Youssef Mohammed

---

## Problem Statement

Manual slice-by-slice kidney and tumor delineation in CT scans is:

- Time-consuming
- Costly
- Vulnerable to inter-observer variability

**Project Goal:** Support segmentation and volumetric quantification for kidney and renal tumor assessment.

---

## System Overview

- **Device Type:** Software as a Medical Device (SaMD) academic prototype
- **Intended Use:** Computer-aided detection and segmentation of kidney and tumor in CT scans
- **Intended Users:** Radiologists, urologists, and medical engineers
- **Input:** NIfTI CT volumes (`.nii` / `.nii.gz`)
- **Output:**
  - 3D segmentation mask
  - Kidney/tumor volumetric statistics
  - Interactive 3D visualization
- **Classification:** Decision-support only. All outputs require physician review.

---

## Dataset

- **Dataset:** KiTS23 (Kidney Tumor Segmentation Challenge 2023)
- **Classes:**
  - Background
  - Kidney
  - Tumor/Cyst
- **Test Set:** 64 independent held-out cases

---

## Official KiTS23 Dataset vs NephroVision Evaluation Split

- **KiTS23** is the 2023 Kidney and Kidney Tumor Segmentation Challenge.
- It is a public benchmark for semantic segmentation of kidneys, renal tumors, and renal cysts.
- It is the third KiTS challenge iteration after 2019 and 2021.
- The official KiTS23 challenge describes an expanded training set of **489 cases** and an official fresh test set of **110 cases**.
- The official repository provides dataset download tools and reference metric implementations.
- **NephroVision did not report official leaderboard performance unless explicitly documented.**
- NephroVision's final reported metrics are based on a **project-defined held-out evaluation subset of 64 independent cases**.
- All metrics in the report and presentation must refer to the **64-case project evaluation subset**.
- **Do not mix** official KiTS23 challenge split numbers with NephroVision's internal/project split.

---

## Pipeline

1. **NIfTI Loading and Validation**
2. **HU Clipping:** [-200, 300]
3. **Normalization:** [0, 1]
4. **Model:** 3D U-Net volumetric semantic segmentation
5. **Inference:** Sliding window 64×192×192 with 50% overlap
6. **Test-Time Augmentation:** 8 flip combinations
7. **Post-Processing:**
   - Remove kidney blobs < 5000 voxels
   - Remove tumor blobs < 100 voxels
8. **Web Visualization:** Browser-based 3D mesh viewer and volumetric statistics

---

## Validation Metrics

| Metric | Kidney | Tumor |
|--------|--------|-------|
| **Dice Score** | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| **HD95 (mm)** | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

---

## Safety and Regulatory

- **IEC 62304 Software Safety Class:** Class B
- **Status:** Academic prototype
- **Clinical Approval:** None. Not clinically approved.
- **FDA Approval:** None. Not FDA approved.
- **Role:** Does not replace radiologists. All clinical decisions remain the responsibility of qualified healthcare professionals.

---

## Known Limitations

- Tumor Dice is lower than kidney Dice due to:
  - Tumor size variability
  - Boundary ambiguity
  - Heterogeneous tumor appearance
- No prospective clinical trial was conducted
- Domain shift may occur on non-KiTS23 scanner protocols
- Cybersecurity and post-market surveillance are future regulatory gaps
- External clinical validation is future work

---

## Future Work

- Improve tumor boundary accuracy
- Evaluate nnU-Net or stronger self-configuring segmentation frameworks
- Add external multi-center validation
- Improve cybersecurity documentation
- Prepare formal clinical validation protocol
- Improve user testing and usability evaluation

---

## Mid-Year Feedback Response

The team received feedback that the project work should be documented more thoroughly. The final documentation must show the development process, not only the final results.

**Required documentation includes:**

1. Dataset preparation
2. Preprocessing decisions
3. Model training setup
4. Experiment iterations
5. Inference and post-processing decisions
6. Challenges such as cyst/tumor segmentation
7. Failure modes
8. Limitations and future work

**Delivery requirement:** The final report and presentation must include explicit sections or slides showing what was done, what was difficult, and how risks were mitigated.

**Rule for unknown details:** Unknown details must be marked as `TODO` and completed by the team with actual data. Do not invent values, hyperparameters, or undocumented experiments.

---

## Non-Negotiable Rules

1. **Never change validated metrics.** All numbers must match the validation results above.
2. **Never invent clinical validation.** No claims of clinical trials or patient outcomes beyond the dataset.
3. **Never claim regulatory approval.** The system is an academic prototype, not FDA or CE approved.
4. **Never describe the system as autonomous diagnosis.** It is decision-support only.
5. **Always present it as decision-support requiring physician review.** All outputs must be reviewed by qualified healthcare professionals before clinical use.
6. **Do not present undocumented experiments as completed.** Every claimed experiment must have a corresponding entry in the experiment log.
7. **Do not invent hyperparameters.** Exact optimizer settings, learning rates, and batch sizes must come from the experiment log, not fabricated.
8. **Distinguish between implemented work, observed challenges, and planned future work.** Do not present future plans as already achieved.
9. **Never present the 64-case project evaluation as the official KiTS23 challenge test set** unless it was actually submitted and verified.
10. **Never claim official KiTS23 leaderboard ranking** unless documented.
11. **Always distinguish official dataset information from project-specific evaluation setup.**

---

**This file is the authoritative reference for all NephroVision documentation.**
