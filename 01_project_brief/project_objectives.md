# Project Objectives

## NephroVision — Automated Kidney and Renal Tumor Segmentation System

---

## 1. Main Objective

Develop NephroVision, an academic decision-support prototype for automated kidney and renal tumor/cyst segmentation from contrast-enhanced abdominal CT scans. The system provides volumetric quantification and interactive 3D visualization to assist medical professionals in renal assessment, supporting workflow efficiency and measurement consistency.

**Scope:** NephroVision is an academic prototype, not a clinically approved device. It does not diagnose, it does not replace physician judgment, and all outputs require clinical review.

---

## 2. Technical Objectives

### 2.1 Segmentation Model
- Implement a 3D U-Net architecture for volumetric semantic segmentation of kidney and tumor/cyst from CT volumes.
- Achieve robust kidney segmentation with Dice score ≥ 0.90.
- Achieve reliable tumor detection across the test set.
- Apply test-time augmentation (8 flip combinations) to reduce boundary noise.

### 2.2 Preprocessing Pipeline
- Design a reproducible preprocessing pipeline including NIfTI loading, validation, HU clipping [-200, 300], and normalization [0, 1].
- Ensure preprocessing consistency between training and inference.
- Handle variable voxel spacing and orientation across cases.

### 2.3 Inference and Post-Processing
- Implement sliding-window inference with patch size 64×192×192 and 50% overlap to handle full volumes within GPU memory constraints.
- Apply connected-component post-processing to remove false-positive kidney blobs (< 5000 voxels) and tumor blobs (< 100 voxels).
- Balance detection sensitivity with false-positive reduction through conservative thresholds.

### 2.4 Evaluation
- Evaluate the system on 64 independent held-out test cases from KiTS23.
- Report Dice score, Hausdorff Distance (HD95), and detection rate for kidney and tumor/cyst.
- Distinguish between detection performance and boundary segmentation accuracy.

---

## 3. Clinical-Support Objectives

### 3.1 Workflow Support
- Reduce radiologist workload by providing automated segmentation as a reproducible starting point.
- Improve measurement consistency by reducing inter-observer variability in volumetric quantification.
- Support surgical planning, treatment monitoring, and longitudinal follow-up through standardized volumetric assessment.

### 3.2 Decision-Support Role
- Position NephroVision as a decision-support tool, not an autonomous diagnostic system.
- Ensure all outputs are presented as requiring physician review and clinical judgment.
- Clearly communicate that the system does not diagnose cancer, does not replace radiologists, and is not clinically approved.

### 3.3 User-Centered Design
- Target intended users: radiologists, urologists, and medical engineers.
- Provide outputs in clinically relevant formats: 3D segmentation masks, volumetric statistics, and interactive visualization.
- Ensure the interface supports rapid review and adjustment of automated results.

---

## 4. Software and System Objectives

### 4.1 End-to-End Pipeline
- Build a complete pipeline from NIfTI input to segmentation output, volumetric statistics, and web-based 3D visualization.
- Ensure the pipeline is reproducible and documented for future validation.

### 4.2 Web-Based Visualization
- Develop a browser-based interface for interactive 3D mesh viewing and volumetric statistics display.
- Support NIfTI file upload and real-time visualization without requiring specialized software.
- Ensure the interface is accessible and usable across modern browsers.

### 4.3 Software Quality
- Maintain clean, modular code with clear separation between preprocessing, model, inference, post-processing, and visualization components.
- Document all software dependencies, environment requirements, and execution commands.
- Ensure the system can be deployed and tested by the team and reviewers.

---

## 5. Documentation Objectives

### 5.1 Development Process Documentation
- Document the full development timeline from problem definition to final prototype, including all phases: dataset exploration, preprocessing design, model implementation, training iterations, inference development, post-processing, web application, and safety documentation.
- Record every major decision with rationale, including preprocessing choices, model selection, inference configuration, and post-processing thresholds.

### 5.2 Training and Inference Documentation
- Document the training setup including hardware, software environment, data splits, model architecture, loss function, optimizer, learning rate, batch size, epochs, and augmentation strategy.
- Document the inference configuration including sliding-window parameters, test-time augmentation, and post-processing thresholds.
- Maintain an experiment log recording all training runs with hyperparameters, metrics, and decisions.

### 5.3 Challenges and Failure Analysis
- Document the technical challenges encountered during development, especially tumor/cyst segmentation difficulty, GPU memory constraints, class imbalance, and convergence issues.
- Analyze failure cases including boundary leakage, small lesion under-segmentation, false positives, and domain shift risk.
- Explain how challenges were mitigated and what limitations remain.

### 5.4 Distinguishing Implemented Work from Future Work
- Clearly separate completed work from planned future work in all documentation.
- Do not present future plans as already achieved.
- Mark unknown or incomplete details with TODO markers and complete them with actual data before final submission.

### 5.5 Reproducibility
- Ensure all experiments are reproducible by documenting random seeds, environment specifications, data splits, and execution commands.
- Provide a reproducibility checklist covering environment, dependencies, data, and commands.

---

## 6. Safety Objectives

### 6.1 Regulatory Awareness
- Classify NephroVision under IEC 62304 Software Safety Class B.
- Document the intended use, intended users, and decision-support role.
- Clearly state that the system is an academic prototype, not clinically approved, and not FDA approved.

### 6.2 Risk Mitigation
- Implement conservative post-processing thresholds to prioritize detection sensitivity over false-positive reduction.
- Ensure the web interface clearly communicates that outputs require physician review.
- Document known limitations including single-dataset evaluation, moderate tumor boundary precision, domain shift risk, and lack of prospective clinical validation.

### 6.3 Ethical Positioning
- Never claim the system diagnoses cancer, replaces radiologists, or is ready for clinical deployment.
- Always present the system as decision-support requiring physician review.
- Acknowledge limitations honestly and transparently in all documentation and presentations.

---

## 7. Future Objectives

### 7.1 Model Improvement
- Improve tumor boundary accuracy through boundary-aware loss functions (e.g., Boundary loss, Hausdorff loss).
- Evaluate nnU-Net or other self-configuring segmentation frameworks as baseline comparisons.
- Investigate multi-scale architectures or attention mechanisms for improved small-lesion segmentation.

### 7.2 Validation and Generalization
- Conduct external multi-center validation on CT data from different scanners, institutions, and patient populations.
- Evaluate domain adaptation techniques to address scanner protocol variability.
- Perform size-stratified analysis to quantify performance as a function of lesion volume.

### 7.3 Clinical Translation
- Prepare a formal clinical validation protocol for prospective evaluation with physician reviewers.
- Develop a cyst vs. tumor classification stage after segmentation to distinguish benign from malignant lesions.
- Improve cybersecurity documentation and post-market surveillance planning for future regulatory compliance.

### 7.4 System Optimization
- Optimize inference latency for clinical workflow integration.
- Implement uncertainty estimation (e.g., Monte Carlo dropout) to flag low-confidence regions for physician attention.
- Enhance web interface with additional clinical metadata and reporting features.

---

## Summary

NephroVision aims to deliver a complete, documented, decision-support prototype for automated kidney and renal tumor/cyst segmentation. The project balances technical achievement (robust kidney segmentation, reliable tumor detection) with honest acknowledgment of limitations (moderate tumor boundary precision, single-dataset evaluation, academic prototype status). The development process is documented systematically, challenges are addressed transparently, and the system is positioned clearly as decision-support requiring physician review.

---

**This document is consistent with MASTER_CONTEXT.md, PROJECT_RULES.md, and DO_NOT_OVERCLAIM.md.**
