# Challenges and Solutions

**NephroVision — Automated Kidney and Renal Tumor Segmentation System**

> This document records the real engineering and research challenges encountered during the project and the mitigations applied. It supports the defense Q&A, the report limitations section, and the mid-year evaluation feedback requirement to document what went wrong and what was done about it.
>
> **Honesty rule:** No challenge is presented as fully solved unless the final metrics and validation scope unambiguously support that claim. Where exact details of attempted solutions are unknown, the team must fill them in; do not invent experiments.

---

## 1. Overview

NephroVision addresses kidney and tumor/cyst volumetric segmentation from abdominal CT using a 3D U-Net trained on KiTS23. The project spans data preparation, model training, inference engineering, post-processing, web visualization, and regulatory documentation. Challenges emerged at every stage. The most persistent difficulty is tumor/cyst segmentation, where lesions are small, variable, and boundary-ambiguous. Kidney segmentation is comparatively robust (Dice 0.9307 ± 0.064), while tumor segmentation remains moderate (Dice 0.6558 ± 0.262) despite perfect detection (100%, 64/64).

---

## 2. Data-Related Challenges

### 2.1 Dataset Size and Diversity

**Challenge description:** KiTS23 provides a defined set of CT volumes with consistent labeling, but the collection represents a limited population and scanner protocol.

**Why it matters:** A model trained on a single dataset may not generalize to other institutions, acquisition protocols, or patient demographics. This is a well-known domain shift risk in medical imaging.

**What the team tried:** All development and evaluation used the KiTS23 dataset exclusively. Data augmentations were applied during training (details to be added by team).

**Current mitigation:** Acknowledged as a limitation. The system is presented as evaluated on KiTS23 only. External validation is listed as future work.

**Remaining limitation:** No multi-center data was used. Performance on non-KiTS23 CT protocols is unknown.

**Future improvement:** External multi-center validation study with data from different scanners and institutions.

---

### 2.2 Class Imbalance

**Challenge description:** Background voxels dominate CT volumes. Tumor/cyst voxels are extremely rare. This imbalance biases the model toward the majority classes.

**Why it matters:** A model that predicts "background everywhere" would achieve high background accuracy but fail clinically.

**What the team tried:** The team explored class weighting, specialized loss functions, and patch-based sampling. **Team to add exact experiment details.**

**Current mitigation:** Post-processing removes small false-positive blobs (kidney < 5000 voxels, tumor < 100 voxels), reducing spurious predictions while preserving small true lesions.

**Remaining limitation:** Class imbalance still affects tumor boundary quality, contributing to lower tumor Dice.

**Future improvement:** Evaluate loss functions designed for severe class imbalance (e.g., Focal loss, boundary-aware losses) and compare against nnU-Net's built-in handling.

---

### 2.3 Tumor/Cyst as a Single Class

**Challenge description:** KiTS23 merges tumors and cysts into one foreground class. The model cannot distinguish a malignant tumor from a benign cyst.

**Why it matters:** Clinical workflows require distinction between tumor and cyst. A segmentation mask that merges both limits the clinical utility of the output.

**What the team tried:** The team accepted the merged-class convention from the challenge design and focused on the segmentation problem as defined.

**Current mitigation:** The limitation is explicitly stated in the report and presentation. The output class is referred to as "Tumor/Cyst" to avoid implying diagnostic capability.

**Remaining limitation:** No separation between tumor and cyst is performed.

**Future improvement:** Investigate two-stage approaches: first detect and segment all lesions, then classify tumor vs. cyst using texture or enhancement features.

---

## 3. Preprocessing Challenges

### 3.1 HU Clipping Range Selection

**Challenge description:** CT intensities span a wide Hounsfield Unit range (typically [-1000, +3000]), but only a narrow band is relevant for kidney and soft-tissue segmentation. Choosing too wide a range includes irrelevant structures; too narrow a range clips useful information.

**Why it matters:** The clipping range directly affects what the model sees. A suboptimal range degrades segmentation quality for both kidney and tumor.

**What the team tried:** Multiple clipping ranges were evaluated. **Team to add exact experiment details and the ranges tested.**

**Current mitigation:** The final clipping range [-200, 300] was selected and is applied consistently to all inputs before normalization to [0, 1].

**Remaining limitation:** The fixed range may not be optimal for all cases, especially those with unusual contrast enhancement or pathology.

**Future improvement:** Evaluate adaptive clipping based on per-volume intensity statistics.

---

### 3.2 Variable Voxel Spacing and Orientation

**Challenge description:** CT volumes in KiTS23 vary in voxel spacing, volume dimensions, and anatomical orientation.

**Why it matters:** A segmentation model expects consistent input geometry. Mismatched spacing can distort anatomical structures and degrade performance.

**What the team tried:** The team applied standard preprocessing to handle orientation and spacing. **Team to add exact experiment details (resampling strategy, target spacing).**

**Current mitigation:** Preprocessing pipeline includes orientation standardization and resampling (details to be confirmed by team).

**Remaining limitation:** Extreme variation in volume dimensions may require cropping or padding strategies that could truncate relevant anatomy.

**Future improvement:** Document and validate the resampling strategy across the full KiTS23 distribution.

---

## 4. Model Training Challenges

### 4.1 GPU Memory Constraints

**Challenge description:** Full 3D CT volumes are too large to fit into GPU memory at once. Naive full-volume training is impossible on typical academic hardware.

**Why it matters:** Without a memory-efficient strategy, the model cannot be trained at all or must sacrifice spatial context by using 2D slices.

**What the team tried:** Patch-based training was adopted to fit within GPU memory. **Team to add exact experiment details (patch size used during training, memory consumption).**

**Current mitigation:** Training was conducted on patches rather than full volumes. Inference uses a sliding-window approach with 50% overlap to reconstruct full-volume predictions.

**Remaining limitation:** Patch-based training may miss long-range anatomical context that full-volume processing would capture.

**Future improvement:** Evaluate gradient accumulation, mixed-precision training, and larger-patch strategies to increase effective context.

---

### 4.2 Hyperparameter Sensitivity

**Challenge description:** 3D U-Net training is sensitive to hyperparameter choices including learning rate, batch size, optimizer, and augmentation strength.

**Why it matters:** Suboptimal hyperparameters can prevent convergence, cause overfitting, or produce inconsistent validation results.

**What the team tried:** Multiple training runs with different configurations were conducted. **Team to add exact experiment details from experiment_log.md.**

**Current mitigation:** A validated configuration achieved the reported metrics. The exact hyperparameters must be documented by the team in `model_training_documentation.md`.

**Remaining limitation:** Without a systematic hyperparameter search (e.g., grid or Bayesian), it is unknown whether the current configuration is near-optimal.

**Future improvement:** Conduct a structured hyperparameter search and document the full optimization trajectory.

---

## 5. Tumor/Cyst Segmentation Challenges

### 5.1 Size Variability

**Challenge description:** Tumors and cysts in the KiTS23 dataset range from a few voxels to large masses occupying a significant fraction of the kidney. Small lesions are easily missed or mislabeled.

**Why it matters:** Missing a small tumor is a critical clinical failure. The model must detect lesions regardless of size.

**What the team tried:** Post-processing with a conservative minimum blob size (100 voxels for tumor) preserves small predictions while filtering noise. **Team to add exact size analysis on the test set.**

**Current mitigation:** Tumor detection rate is 100% (64/64) on the test set, indicating that the model finds all tumors. Dice is lower (0.6558) primarily due to boundary inaccuracy on small and medium-sized lesions.

**Remaining limitation:** Very small lesions near the detection threshold remain at risk. No per-lesion size-stratified analysis has been performed yet.

**Future improvement:** Conduct per-lesion analysis stratified by size. Evaluate size-aware loss functions or multi-scale architectures.

---

### 5.2 Boundary Ambiguity

**Challenge description:** Tumor boundaries are often unclear in CT. Lesions may infiltrate the renal parenchyma or abut the kidney boundary with no clear separation.

**Why it matters:** Boundary errors dominate the Dice penalty, especially for small lesions where even a few voxels of misalignment significantly reduce the score.

**What the team tried:** The model was trained with an appropriate loss function. **Team to add exact experiment details (loss function choice and how it addresses boundaries).**

**Current mitigation:** TTA (8 flip combinations) and sliding-window inference reduce boundary noise. The HD95 metric (Kidney 19.98 mm, Tumor 67.35 mm) quantifies boundary performance.

**Remaining limitation:** HD95 for tumor (67.35 mm) is high, confirming significant boundary uncertainty. The model may produce a reasonable Dice but miss precise margins.

**Future improvement:** Evaluate boundary-aware losses (e.g., Boundary loss, Hausdorff loss). Investigate uncertainty estimation to flag cases with high boundary ambiguity.

---

### 5.3 Heterogeneous Appearance

**Challenge description:** Tumors and cysts appear with widely varying intensity, texture, and enhancement patterns depending on pathology, contrast phase, and patient factors.

**Why it matters:** The model must generalize across this appearance variability within the KiTS23 distribution.

**What the team tried:** Training augmentations were applied to improve robustness to appearance variation. **Team to add exact experiment details.**

**Current mitigation:** The model achieves 100% detection across the 64 test cases, indicating robustness to appearance variation within KiTS23. Dice variation (std 0.262 for tumor) reflects the remaining appearance-driven uncertainty.

**Remaining limitation:** Performance on unseen appearance patterns (e.g., non-contrast CT, different contrast phases) is unknown.

**Future improvement:** Evaluate domain adaptation techniques. Test on multi-phase CT or non-contrast acquisitions if data becomes available.

---

### 5.4 Cyst vs. Tumor Confusion

**Challenge description:** In CT, cysts and tumors can appear visually similar (both can be hypodense or heterogeneous). Even human readers may disagree without clinical context or follow-up imaging.

**Why it matters:** The KiTS23 merged class means the model does not need to distinguish them, but the output mask may be misinterpreted as a "tumor mask" when it actually includes cysts.

**What the team tried:** The model does not attempt to separate cysts from tumors. This is a design choice consistent with the challenge task but must be communicated clearly.

**Current mitigation:** The output class is labeled "Tumor/Cyst" in all materials. The report and presentation explicitly note that the mask includes both and does not differentiate.

**Remaining limitation:** Users unfamiliar with KiTS23 conventions may misinterpret the output.

**Future improvement:** Investigate classification of segmented lesions into tumor vs. cyst categories using additional features or a separate classifier.

---

## 6. Inference and Memory Challenges

### 6.1 Sliding-Window Boundary Artifacts

**Challenge description:** When reconstructing a full-volume prediction from overlapping patches, boundaries between patches can produce visible seams or inconsistent predictions.

**Why it matters:** Seam artifacts degrade segmentation quality and produce visually implausible masks that undermine trust.

**What the team tried:** A 50% overlap was used to smooth transitions. A fusion method was applied at overlapping regions. **Team to add exact experiment details (averaging vs. Gaussian weighting).**

**Current mitigation:** The overlap and fusion strategy reduces visible seams. TTA further averages out inconsistencies across patch boundaries.

**Remaining limitation:** Subtle stitching artifacts may persist at patch boundaries in some volumes.

**Future improvement:** Evaluate larger patch sizes or full-volume inference if hardware permits. Investigate patching-free architectures.

---

### 6.2 Inference Time

**Challenge description:** Processing a full CT volume through sliding-window inference with 8-flip TTA is computationally intensive and time-consuming.

**Why it matters:** If a radiologist must wait for results, the system is less practical for clinical workflows.

**What the team tried:** The inference pipeline processes one case at a time. **Team to add exact inference time per case.**

**Current mitigation:** TTA is accepted as a necessary trade-off for accuracy. Inference time is not claimed to be real-time.

**Remaining limitation:** No latency optimization has been performed beyond the current pipeline.

**Future improvement:** Profile the inference pipeline and optimize bottlenecks. Evaluate reduced TTA (e.g., 4 flips). Consider model pruning, quantization, or ONNX/TensorRT export.

---

## 7. Post-Processing Challenges

### 7.1 Blob Removal Threshold Calibration

**Challenge description:** Setting blob size thresholds involves a trade-off: thresholds that are too high risk removing small true tumors; thresholds that are too low leave noise in the output.

**Why it matters:** False negatives (removed true tumors) are clinically more dangerous than false positives (retained noise).

**What the team tried:** Thresholds were calibrated on the validation set. **Team to add exact experiment details (how thresholds were chosen, sensitivity analysis).**

**Current mitigation:** Conservative thresholds: kidney blobs < 5000 voxels removed; tumor blobs < 100 voxels removed. These preserve the 100% tumor detection rate while reducing false positives.

**Remaining limitation:** A tumor smaller than 100 voxels (in the resampled space) would be removed, even if real. No per-case validation of this risk has been performed.

**Future improvement:** Evaluate per-case adaptive thresholding or learning-based false-positive suppression.

---

## 8. Evaluation Challenges

### 8.1 Interpreting Tumor Dice

**Challenge description:** The tumor Dice of 0.6558 ± 0.262 appears low compared to state-of-the-art organ segmentation. This risks being misinterpreted as poor performance by reviewers unfamiliar with the challenge.

**Why it matters:** Defense committee members may question whether the model is adequate. The team must contextualize the number.

**What the team tried:** The team documented the reasons for the lower tumor Dice: size variability, boundary ambiguity, and heterogeneous appearance. The perfect detection rate (100%) is presented alongside Dice to show the model finds all lesions.

**Current mitigation:** Report metrics exactly, include standard deviations, explain limitations, and compare to KiTS23 challenge baselines where available. Reference `KNOWN_METRICS.md`.

**Remaining limitation:** Without a formal statistical comparison to KiTS23 challenge leaderboard results, the contextual positioning is qualitative.

**Future improvement:** Benchmark against published KiTS23 challenge results. Include per-case metric distributions.

---

### 8.2 Single-Dataset Evaluation

**Challenge description:** All evaluation is on the KiTS23 test set. No independent clinical dataset was used.

**Why it matters:** Results may not generalize. This is the most significant limitation from a clinical validation perspective.

**What the team tried:** Evaluation on 64 independent held-out test cases with a fixed, pre-defined split.

**Current mitigation:** The limitation is explicitly stated. The system is described as "evaluated on KiTS23 held-out test cases," not "clinically validated."

**Remaining limitation:** No prospective clinical trial was conducted. Generalizability is unproven.

**Future improvement:** External multi-center validation study. Prepare formal clinical validation protocol.

---

## 9. Web Visualization Challenges

### 9.1 Large Mesh Rendering in Browser

**Challenge description:** Kidney and tumor 3D meshes derived from segmentation masks can be large, causing slow rendering in standard web browsers.

**Why it matters:** A laggy visualization undermines the user experience and the perceived quality of the system.

**What the team tried:** Mesh decimation, level-of-detail strategies, or efficient rendering libraries were considered. **Team to add exact experiment details.**

**Current mitigation:** A browser-based 3D viewer was implemented that renders segmentations interactively.

**Remaining limitation:** Performance on low-end hardware or very large volumes may still be suboptimal.

**Future improvement:** Profile rendering performance. Evaluate WebGL optimizations or server-side rendering as fallback.

---

### 9.2 Large NIfTI File Upload

**Challenge description:** CT volumes can be hundreds of megabytes. Uploading and processing large files through a web interface introduces latency and timeout risks.

**Why it matters:** Users may abandon the interface if upload or processing takes too long.

**What the team tried:** The web application handles file upload and triggers backend processing. **Team to add exact experiment details (tech stack, timeout handling, progress indicators).**

**Current mitigation:** A working end-to-end pipeline from upload to visualization was achieved.

**Remaining limitation:** No load testing or performance benchmarks have been conducted.

**Future improvement:** Implement asynchronous processing with progress indicators. Add file size limits and compression.

---

## 10. Regulatory and Safety Documentation Challenges

### 10.1 Mapping Academic Prototype to IEC 62304

**Challenge description:** IEC 62304 is designed for commercial medical device software. Mapping an academic graduation project onto this framework requires judgment and careful scoping.

**Why it matters:** The defense requires demonstrating regulatory awareness even if full compliance is beyond scope.

**What the team tried:** The system was classified as Software Safety Class B under IEC 62304. Documentation identified known gaps (cybersecurity, post-market surveillance) as future work.

**Current mitigation:** The report and presentation acknowledge the academic prototype status. Safety documentation defines the regulatory boundary without overclaiming.

**Remaining limitation:** Full IEC 62304 compliance documentation (software development plan, risk management file, traceability matrix) is not complete.

**Future improvement:** Develop a risk management file. Document software lifecycle processes. Prepare a gap analysis for clinical translation.

---

### 10.2 Defining Decision-Support Boundaries

**Challenge description:** The line between "decision-support" and "autonomous diagnosis" must be drawn clearly in all materials.

**Why it matters:** Any ambiguity could be interpreted as claiming diagnostic capability, which is both inaccurate and ethically problematic.

**What the team tried:** The system is consistently described as "computer-aided detection and segmentation" and "decision-support only." All outputs require physician review.

**Current mitigation:** Safety wording is enforced by `PROJECT_RULES.md` and `DO_NOT_OVERCLAIM.md`. Every document, slide, and speaker note must use safe phrasing.

**Remaining limitation:** The web interface itself must communicate these disclaimers to the end user. Review whether the current UI language is adequate.

**Future improvement:** Add an explicit disclaimer panel to the web interface. Include intended-use statement and limitations directly in the application.

---

## 11. Lessons Learned

| Area | Lesson |
|------|--------|
| **Tumor segmentation** | Detection is easier than precise delineation. A high detection rate with moderate Dice is a realistic outcome that must be explained clearly. |
| **Preprocessing** | Simple, reproducible preprocessing (HU clipping, normalization) provides a solid foundation. Document the rationale for every threshold. |
| **Evaluation** | Report metrics per class, with uncertainty, and never inflate. Contextualize numbers against dataset difficulty. |
| **Documentation** | Maintain an experiment log from day one. Defense requires evidence of the process, not just the final result. |
| **Safety wording** | Establish safe language early and enforce it across all materials. Overclaiming is easy to do unintentionally. |
| **Web visualization** | Browser-based 3D rendering is feasible but requires performance optimization. Test on representative hardware. |
| **Regulatory framing** | Even as an academic prototype, IEC 62304 classification adds credibility. Define the boundary honestly. |

> **Team to add:** Additional lessons from the development experience, including teamwork insights, supervisor feedback points, and advice for future projects.

---

**All entries must remain consistent with `MASTER_CONTEXT.md`, `KNOWN_METRICS.md`, `DO_NOT_OVERCLAIM.md`, and `experiment_log.md`.**
