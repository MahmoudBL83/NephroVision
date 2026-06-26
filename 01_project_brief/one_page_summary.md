# NephroVision: Automated Kidney and Renal Tumor Segmentation System

## Project Overview

**Team:** Rashed Mamdouh, Mohamed Walid, Mahmoud BahaaAldeen, Mahmoud Mohammed, Youssef Mohammed  
**Department:** Medical Engineering Department, Graduation Project  
**Supervisor:** Hisham Abdeltawab, Ph.D.

---

## Clinical Problem

Manual slice-by-slice delineation of kidney and renal tumors in CT scans is time-consuming, costly, and subject to inter-observer variability. Radiologists and urologists require accurate volumetric assessment for surgical planning, treatment monitoring, and longitudinal follow-up. Automated segmentation support can reduce workload and improve consistency, but such systems must be positioned as decision-support tools requiring physician review.

---

## Project Objective

Develop NephroVision, an academic decision-support prototype for automated kidney and renal tumor/cyst segmentation from abdominal CT scans. The system provides volumetric quantification and interactive 3D visualization to assist medical professionals in renal assessment.

---

## Dataset and System Scope

**Dataset:** KiTS23 (Kidney Tumor Segmentation Challenge 2023)  
**Classes:** Background, Kidney, Tumor/Cyst (merged per challenge convention)  
**Test Set:** 64 independent held-out cases  
**Input:** NIfTI CT volumes (`.nii` / `.nii.gz`)  
**Output:** 3D segmentation mask, kidney/tumor volumetric statistics, browser-based 3D visualization

---

## Technical Pipeline

1. **Preprocessing:** NIfTI loading and validation, HU clipping [-200, 300], normalization [0, 1]
2. **Model:** 3D U-Net for volumetric semantic segmentation
3. **Inference:** Sliding window 64×192×192 with 50% overlap
4. **Test-Time Augmentation:** 8 flip combinations to reduce boundary noise
5. **Post-Processing:** Remove kidney blobs < 5000 voxels, tumor blobs < 100 voxels
6. **Visualization:** Web-based 3D mesh viewer with volumetric statistics

---

## Development Process

The project followed a structured, iterative development process documented across ten phases: problem understanding, dataset exploration, preprocessing design, baseline 3D U-Net implementation, training iterations, inference pipeline development, post-processing improvements, web application development, IEC 62304 safety documentation, and final validation. Each phase involved experiments recorded in the project experiment log, with decisions documented for reproducibility and defense transparency.

---

## Main Challenges

**Tumor/Cyst Segmentation Difficulty:** Tumors and cysts are smaller, more variable in shape, and have less clear boundaries than the kidney. The KiTS23 dataset merges cysts and tumors into a single class, preventing distinction between benign and malignant lesions. Tumor Dice is lower than kidney Dice due to tumor size variability, boundary ambiguity, and heterogeneous appearance.

**Detection vs. Boundary Precision:** Tumor detection and tumor boundary segmentation are different tasks. The system achieves 100% tumor detection (64/64 cases), but boundary-level segmentation remains more challenging, as reflected by the tumor Dice score. This is consistent with the inherent difficulty of the task and published KiTS23 challenge baselines.

---

## Final Validation Results

Evaluated on 64 independent held-out test cases from KiTS23:

| Metric | Kidney | Tumor |
|--------|--------|-------|
| **Dice Score** | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| **HD95 (mm)** | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

Kidney segmentation is robust. Tumor detection is reliable. Tumor boundary precision is moderate, reflecting the difficulty of the task rather than a fundamental model failure.

---

## Safety and Regulatory Positioning

**IEC 62304 Classification:** Class B  
**Device Type:** Software as a Medical Device (SaMD) academic prototype  
**Status:** Not clinically approved. Not FDA approved.  
**Intended Use:** Decision-support only. All outputs require physician review. All clinical decisions remain the responsibility of qualified healthcare professionals.

---

## Final Takeaway

NephroVision demonstrates that automated kidney and renal tumor segmentation is feasible within an academic prototype framework. The system achieves robust kidney segmentation (Dice 0.9307) and reliable tumor detection (100%), with moderate tumor boundary precision (Dice 0.6558) that reflects the inherent difficulty of the task. The development process was documented systematically, challenges were addressed honestly, and limitations are clearly stated. NephroVision is positioned as decision-support requiring physician review, not as an autonomous diagnostic system.

---

**This summary is consistent with MASTER_CONTEXT.md and the full development documentation.**
