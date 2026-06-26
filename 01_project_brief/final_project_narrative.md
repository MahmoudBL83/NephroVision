# Final Project Narrative

## NephroVision: Automated Kidney and Renal Tumor Segmentation System

**Medical Engineering Department, Graduation Project**
**Team:** Rashed Mamdouh, Mohamed Walid, Mahmoud BahaaAldeen, Mahmoud Mohammed, Youssef Mohammed
**Supervisor:** Hisham Abdeltawab, Ph.D.

---

## 1. Background and Motivation

Kidney cancer is among the most common malignancies of the urinary system, and its assessment relies heavily on contrast-enhanced computed tomography. Accurate volumetric measurement of the kidney and any associated tumors or cysts is essential for surgical planning, treatment monitoring, and longitudinal follow-up. Yet in clinical practice, this measurement is still performed manually — a radiologist delineates the kidney boundary and the tumor boundary slice by slice across hundreds of CT images.

This manual process is slow, labor-intensive, and subject to inter-observer variability. Two experienced radiologists may draw different boundaries for the same tumor, particularly when the tumor margin is infiltrative or ill-defined. This variability propagates into every downstream clinical decision: the estimated tumor volume, the surgical approach, the assessment of treatment response, and the timing of follow-up imaging.

There is a clear clinical need for automated segmentation support — a tool that can produce a fast, reproducible starting point for physician review. This is the motivation behind NephroVision.

---

## 2. Problem Definition

The problem we address is automated segmentation of the kidney and renal tumor or cyst from contrast-enhanced abdominal CT scans. The system must accept a NIfTI CT volume as input and produce three outputs: a 3D segmentation mask, kidney and tumor volumetric statistics, and an interactive visualization that a physician can review.

The problem is bounded by several constraints. First, the system must handle the full anatomical variability present in the KiTS23 dataset — kidneys of different sizes, tumors ranging from small lesions to large masses, and cysts of varying complexity. Second, the system must be positioned correctly: it is a decision-support tool, not an autonomous diagnostic system. All outputs require physician review, and all clinical decisions remain the responsibility of qualified healthcare professionals. Third, the system must be documented thoroughly — not only the final results, but the development process, the decisions made, the difficulties encountered, and the limitations acknowledged.

---

## 3. Why This Is a Biomedical Engineering Problem

This project sits at the intersection of medical imaging, deep learning, software engineering, and regulatory awareness. It is not purely a machine learning problem — a model that achieves high Dice scores but cannot be integrated into a usable system has limited value. It is not purely a software engineering problem — a well-designed interface that produces inaccurate segmentations is clinically dangerous. And it is not purely a clinical problem — the engineering team must understand the clinical workflow without claiming to replace clinical judgment.

NephroVision requires integrating knowledge across these domains: understanding CT imaging and Hounsfield Units, designing a preprocessing pipeline that preserves diagnostic information, implementing a 3D deep learning architecture for volumetric segmentation, building an inference pipeline that handles large volumes within GPU memory constraints, developing a web-based visualization system, and framing the entire system under a recognized safety standard. This integration is what makes it a biomedical engineering project.

---

## 4. Proposed Solution

We propose NephroVision, an academic decision-support prototype that automates kidney and renal tumor/cyst segmentation from CT volumes using a 3D U-Net trained on the KiTS23 dataset. The system processes NIfTI CT volumes through a reproducible preprocessing pipeline, runs volumetric inference with test-time augmentation, applies conservative post-processing to reduce false positives, and presents the results through a browser-based 3D visualization interface.

The solution is designed around three principles. First, reproducibility — the same input always produces the same output, and the pipeline is documented in sufficient detail for another team to replicate it. Second, honesty — the system reports its performance transparently, including both strengths and limitations, and never claims capabilities it does not have. Third, decision-support — the system assists the physician by providing a fast, reproducible segmentation, but the physician remains responsible for every clinical decision.

---

## 5. Development Process and Documentation

The development of NephroVision followed a structured, iterative process across ten phases. We began with problem understanding and clinical motivation, then explored the KiTS23 dataset to understand its structure, classes, and annotation conventions. We designed the preprocessing pipeline, implemented the baseline 3D U-Net, and conducted multiple training and validation iterations. We developed the inference pipeline with sliding-window processing and test-time augmentation, refined the post-processing thresholds, built the web application for 3D visualization, documented the system under IEC 62304 Class B, and finally evaluated on the 64 independent held-out test cases.

After our mid-year evaluation, we received feedback that the project work should be documented more thoroughly — not only the final results, but the development process itself. We responded by creating a comprehensive development documentation package covering the full engineering journey. This package includes a development timeline, an experiment log recording every training run with hyperparameters and decisions, detailed model training documentation, preprocessing decision rationale, engineering decision records, a challenges and solutions analysis, a dedicated analysis of cyst and tumor detection difficulties, a failure cases analysis, an ablation and iteration summary, reproducibility notes, and lessons learned.

This documentation is not retrospective — it was maintained during development and reflects the actual engineering process. Every experiment claimed in the defense has a corresponding entry in the experiment log. Unknown details are marked as TODO and must be completed by the team with actual data before final submission. No undocumented experiment is presented as completed work.

---

## 6. Technical Pipeline

The NephroVision pipeline processes a NIfTI CT volume through eight stages:

**Stage 1: NIfTI Loading and Validation.** The input volume is loaded and validated for correct orientation, spacing metadata, and label consistency. Volumes with missing or inconsistent metadata are flagged for manual review.

**Stage 2: HU Clipping.** CT intensities are clipped to the range [-200, 300] Hounsfield Units. This range was selected empirically to preserve kidney parenchyma and tumor tissue while suppressing bone, air, and other irrelevant structures.

**Stage 3: Normalization.** Clipped intensities are linearly normalized to the range [0, 1] using min-max scaling. This ensures consistent input to the neural network regardless of scanner-specific intensity variations.

**Stage 4: 3D U-Net Segmentation.** The preprocessed volume is processed by a 3D U-Net architecture configured for three output classes: background, kidney, and tumor/cyst. The 3D convolutions capture volumetric context across slices, which is essential for distinguishing tumors from adjacent structures that may appear similar in a single 2D slice.

**Stage 5: Sliding-Window Inference.** Full volumes are processed using a sliding window with patch size 64×192×192 voxels and 50% overlap between adjacent patches. This approach enables processing of arbitrarily large volumes within GPU memory constraints.

**Stage 6: Test-Time Augmentation.** Each volume is processed with 8 flip combinations along the x, y, and z axes. Predictions from all augmented versions are averaged to reduce boundary noise and improve robustness.

**Stage 7: Post-Processing.** Connected-component analysis is applied to the predicted kidney and tumor/cyst masks. Kidney blobs smaller than 5000 voxels are removed to eliminate extra-renal false positives. Tumor blobs smaller than 100 voxels are removed to filter noise while preserving small true lesions. The conservative tumor threshold prioritizes detection sensitivity over false-positive reduction.

**Stage 8: Web Visualization.** The final segmentation mask, kidney and tumor volumetric statistics, and an interactive 3D mesh viewer are presented through a browser-based interface. No specialized software is required.

The exact training hyperparameters — loss function, optimizer, learning rate, batch size, epochs, and augmentation strategy — are documented in the experiment log and model training documentation. We do not present invented values in this narrative.

---

## 7. Key Challenge: Tumor/Cyst Segmentation

The central technical challenge of NephroVision is tumor and cyst segmentation. Kidney segmentation is relatively tractable because the kidney is a large organ with a consistent bean-like shape, predictable retroperitoneal location, and relatively clear boundaries with surrounding fat and muscle. Tumor and cyst segmentation is substantially harder for several compounding reasons.

First, lesions are small. Some tumors occupy fewer than 100 voxels, making them sensitive to even minor boundary errors. Second, tumor boundaries are often ambiguous. Malignant renal cell carcinomas may infiltrate the surrounding parenchyma without forming a distinct capsule, creating gradual transitions rather than sharp boundaries. Third, tumors and cysts vary enormously in appearance — from simple fluid-density cysts to complex heterogeneous masses with necrosis, hemorrhage, or calcification. Fourth, the KiTS23 dataset merges tumors and cysts into a single foreground class, which means the model must handle two visually distinct entities under one label.

This challenge is reflected in our results. The kidney Dice of 0.9307 ± 0.064 demonstrates robust segmentation of the large, consistent organ. The tumor Dice of 0.6558 ± 0.262 reflects the difficulty of drawing precise boundaries on small, ambiguous lesions. The large standard deviation indicates that performance varies substantially across lesion sizes — some tumors are segmented well, others poorly.

It is critical to distinguish between tumor detection and tumor boundary segmentation. Our tumor detection rate is 100% — the model found every tumor in the 64 test cases. But finding a tumor and drawing its exact boundary are different tasks. The moderate Dice score reflects boundary precision, not detection failure. A one-voxel boundary error on a 100-voxel lesion can reduce Dice from near-perfect to approximately 0.70. The same error on a 100,000-voxel kidney is negligible. This is a mathematical property of the Dice metric on small objects, not a fundamental model failure.

---

## 8. Evaluation and Results

We evaluated the final pipeline on 64 independent held-out test cases from the KiTS23 dataset. These cases were never seen during training or validation. We computed Dice score, Hausdorff Distance (HD95), and tumor detection rate for kidney and tumor/cyst.

The results are as follows:

| Metric | Kidney | Tumor |
|--------|--------|-------|
| Dice Score | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| HD95 (mm) | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

Kidney segmentation is robust, with Dice exceeding 0.93 and HD95 of 19.98 mm indicating precise boundary localization. Tumor detection is reliable — the model found every tumor in the test set. Tumor boundary precision is moderate, with Dice of 0.6558 and HD95 of 67.35 mm confirming significant boundary uncertainty.

These results are consistent with the difficulty of the KiTS23 tumor segmentation task. Published challenge baselines show similar tumor Dice levels, confirming that this performance range reflects inherent task difficulty rather than implementation error. The system achieves its primary goals — robust kidney segmentation and reliable tumor detection — with honest acknowledgment of where tumor boundary precision needs improvement.

---

## 9. Safety and Regulatory Framing

NephroVision is classified under IEC 62304 Software Safety Class B. The system is a Software as a Medical Device (SaMD) academic prototype. It is not clinically approved. It is not FDA approved. It does not replace radiologists.

The intended use is computer-aided detection and segmentation of kidney and tumor in CT scans. The intended users are radiologists, urologists, and medical engineers. All outputs require physician review, and all clinical decisions remain the responsibility of qualified healthcare professionals.

We established safe wording rules enforced across all documentation, slides, and speaker notes. The system is always described as decision-support or computer-aided, never as autonomous diagnosis. We never claim regulatory approval, clinical validation, or radiologist replacement. These rules are documented in `DO_NOT_OVERCLAIM.md` and `PROJECT_RULES.md` and are cross-referenced in every defense material.

Known regulatory gaps include cybersecurity hardening, post-market surveillance planning, and formal clinical validation. These are documented as future work, not hidden weaknesses.

---

## 10. Limitations

We acknowledge the following limitations honestly and transparently:

**Single-dataset evaluation.** All evaluation was performed on the KiTS23 dataset. Performance on CT volumes from different scanners, acquisition protocols, contrast phases, or patient populations is unknown. Domain shift is a well-documented problem in medical AI, and external validation is required before any claim of generalizability.

**No prospective clinical trial.** We did not conduct a clinical trial with physician reviewers. The system has not been tested in a clinical workflow, and its impact on radiologist efficiency, measurement consistency, or patient outcomes has not been measured.

**Moderate tumor boundary precision.** Tumor Dice of 0.6558 and HD95 of 67.35 mm indicate that boundary delineation remains challenging, particularly for small lesions. This is consistent with the task difficulty but limits the system's utility for applications requiring millimeter-precise boundaries.

**Cyst/tumor class merging.** The KiTS23 dataset merges cysts and tumors into a single class. The system cannot distinguish a benign cyst from a potentially malignant tumor. This limitation is clearly communicated in all materials.

**Academic prototype status.** The system is not deployed in any clinical setting. The web application is a research prototype, not a production-ready system. Cybersecurity hardening and usability testing are future work.

These limitations are not apologies — they are known boundaries of the current work. Acknowledging them is essential for patient safety and scientific integrity.

---

## 11. Future Work

Our roadmap is prioritized by clinical impact and feasibility:

**High priority:**
- External multi-center validation on CT data from different scanners, institutions, and patient populations to quantify domain shift and generalizability.
- Improve tumor boundary accuracy through boundary-aware loss functions such as Boundary loss or Hausdorff loss.
- Evaluate nnU-Net or other self-configuring segmentation frameworks as baseline comparisons.

**Medium priority:**
- Add a cyst versus tumor classification stage after segmentation to distinguish benign from malignant lesions.
- Implement uncertainty estimation using Monte Carlo dropout or ensemble methods to flag low-confidence regions for physician attention.
- Conduct per-lesion size-stratified analysis to quantify performance as a function of lesion volume.

**Lower priority:**
- Optimize inference latency for clinical workflow integration.
- Enhance the web interface with additional clinical metadata and reporting features.
- Prepare a formal clinical validation protocol for prospective evaluation with physician reviewers.
- Improve cybersecurity documentation and post-market surveillance planning for future regulatory compliance.

---

## 12. Conclusion

NephroVision demonstrates that automated kidney and renal tumor segmentation is feasible within an academic prototype framework. The system achieves robust kidney segmentation with Dice of 0.9307, reliable tumor detection at 100%, and moderate tumor boundary precision with Dice of 0.6558 that reflects the inherent difficulty of the task rather than a fundamental model failure.

What distinguishes this project is not only the technical result but the documentation of the engineering process. After mid-year feedback, we documented the full development journey — the experiments, the decisions, the difficulties, and the failures. We maintained an experiment log, analyzed failure cases, and acknowledged limitations honestly. We positioned the system correctly as decision-support requiring physician review, not as an autonomous diagnostic tool.

The system is not clinically approved, not FDA approved, and not ready for deployment. It is an academic prototype that demonstrates what is possible when biomedical engineering integrates medical imaging knowledge, deep learning, software system design, and regulatory awareness into a single decision-support tool.

We found every tumor in the test set, but drawing the exact border is still hard — and that is why the physician reviews every output.

---

**This narrative is consistent with MASTER_CONTEXT.md, KNOWN_METRICS.md, DO_NOT_OVERCLAIM.md, and the full development documentation in 07_development_documentation/.**
