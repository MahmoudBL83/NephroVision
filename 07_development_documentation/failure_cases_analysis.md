# Failure Cases Analysis

**NephroVision — Automated Kidney and Renal Tumor Segmentation System**

> A defense that only shows successful cases is incomplete. This document provides a structured framework for analyzing where the system fails, why it fails, and what that means for clinical risk and future work. Every failure case discussed must be backed by real data — no invented cases.

---

## 1. Introduction

Failure case analysis serves three purposes in the defense:

1. **Transparency:** Shows the committee that the team understands the system's limitations, not just its strengths.
2. **Safety:** Identifies failure modes that could cause clinical harm if outputs were used without physician review.
3. **Roadmap:** Informs the future work section with evidence-based priorities.

> **Rule:** No failure case is presented in the report or slides without a corresponding entry here. Use the template in Section 4 to document each case. All failure analysis must reinforce, not undermine, the decision-support framing: outputs require physician review.

---

## 2. Failure Case Categories

### 2.1 Small Tumor Missed or Under-Segmented

**Description:** The model either fails to predict any tumor voxels for a true lesion or predicts a mask significantly smaller than the ground truth.

**Possible causes:**
- Lesion size is near or below the minimum detectable volume for the model and resolution.
- Lesion intensity is similar to surrounding kidney parenchyma (isodense lesion).
- Lesion is located at the kidney boundary where partial volume effects are strongest.
- Post-processing blob removal threshold (100 voxels) removes a true small lesion.

**Clinical risk if unreviewed:**
- A missed malignant tumor could delay diagnosis and treatment.
- Under-segmentation leads to underestimated tumor volume, which may affect surgical planning or treatment response assessment.

**Current mitigation:**
- Tumor detection rate of 100% (64/64) on the test set means no lesion was entirely missed in the held-out evaluation. However, this is not a guarantee.
- Post-processing uses a conservative minimum blob threshold (100 voxels) to preserve small predictions.
- The system is decision-support only; a physician must review every output.

**Future improvement:**
- Stratify detection performance by lesion size to quantify the minimum detectable volume.
- Evaluate detection-focused architectures or two-stage detect-then-segment pipelines.
- Add visual cues in the web interface for low-confidence regions.

---

### 2.2 Tumor Boundary Leakage

**Description:** The predicted tumor mask extends beyond the true lesion boundary into surrounding kidney parenchyma or adjacent structures.

**Possible causes:**
- Ill-defined tumor margin with infiltrative growth pattern.
- Partial volume effects at tissue interfaces.
- Over-aggressive segmentation by the model, especially for heterogeneous lesions.
- Stitching artifacts from sliding-window inference.

**Clinical risk if unreviewed:**
- Overestimated tumor volume, potentially leading to unnecessary intervention or incorrect staging.
- Predicted boundaries that suggest extra-renal extension when none exists.

**Current mitigation:**
- Test-time augmentation (8 flips) reduces boundary noise by averaging predictions.
- HD95 metric (67.35 mm for tumor) quantifies the worst-case boundary error and is reported transparently.
- Sliding-window inference with 50% overlap minimizes stitching artifacts but does not eliminate them.

**Future improvement:**
- Evaluate boundary-aware loss functions (Boundary loss, Hausdorff loss).
- Add uncertainty heatmaps to highlight regions where the model is least confident about the boundary.
- Explore CRF-based post-processing for boundary refinement.

---

### 2.3 Cyst/Tumor Confusion

**Description:** The model segments a cyst and a solid tumor identically because KiTS23 merges them into one class. The output mask does not distinguish between the two.

**Possible causes:**
- KiTS23 dataset convention merges cysts and tumors.
- Both can appear hypodense on contrast-enhanced CT.
- No clinical metadata (e.g., contrast phase, patient history) is available to the model.

**Clinical risk if unreviewed:**
- A user unfamiliar with the convention may interpret the entire mask as "tumor" and assume malignancy where only a benign cyst exists.
- Cyst vs. tumor misclassification could lead to unnecessary biopsy or surgery.

**Current mitigation:**
- The output class is labeled "Tumor/Cyst" in all materials, the web interface, and documentation.
- The report explicitly states that the system does not differentiate cysts from tumors.
- The system is decision-support only; all clinical interpretation requires physician review.

**Future improvement:**
- Train a separate classifier on segmented lesions using additional features (texture, shape, enhancement pattern).
- Explore multi-class segmentation that separates cyst from tumor if annotated data becomes available.
- Display a disclaimer in the web interface explicitly warning against interpreting the mask as a tumor-only mask.

---

### 2.4 False Positive Tumor Blobs

**Description:** The model predicts tumor voxels in regions where no tumor exists, producing spurious "tumor blobs" in the output.

**Possible causes:**
- Image noise or artifacts misinterpreted as tissue boundaries.
- Normal anatomical structures (vessels, collecting system, adrenal gland) with intensity similar to tumor.
- Residual false positives after post-processing if the blob is larger than the removal threshold (100 voxels).

**Clinical risk if unreviewed:**
- False positive tumor regions could be mistaken for true lesions, leading to unnecessary follow-up imaging or intervention.
- Multiple false positive blobs could obscure the true lesion in the visualization.

**Current mitigation:**
- Post-processing removes connected tumor components smaller than 100 voxels.
- Blob threshold was calibrated on the validation set to balance noise removal against small-lesion preservation.
- TTA and sliding-window inference reduce spurious single-patch predictions.

**Future improvement:**
- Evaluate learning-based false-positive suppression (e.g., a second-stage classifier on predicted blobs).
- Add per-blob confidence scores to the web interface so users can distinguish high-confidence from low-confidence predictions.
- Investigate attention mechanisms or auxiliary detection heads.

---

### 2.5 False Positive Kidney Regions

**Description:** The model predicts kidney voxels in regions outside the true kidney (e.g., liver, spleen, retroperitoneal fat).

**Possible causes:**
- Adjacent organs with similar CT attenuation to kidney parenchyma.
- Large field-of-view images where the model encounters anatomy not seen during training.
- Inference on atypical anatomical variants.

**Clinical risk if unreviewed:**
- Incorrect kidney volume estimation if extra-renal regions are counted.
- Confusion if the false kidney region overlaps with or obscures a true tumor.

**Current mitigation:**
- Post-processing removes kidney components smaller than 5000 voxels, eliminating most extra-renal false positives.
- Kidney segmentation Dice (0.9307) is high, indicating that major false-positive kidney regions are rare.
- Physician review of the output mask against the original CT is required.

**Future improvement:**
- Evaluate organ-localization preprocessing to crop the volume to the kidney region before segmentation.
- Use anatomical prior constraints (e.g., expected kidney position, size) to filter implausible predictions.

---

### 2.6 Large-Volume Memory and Inference Issues

**Description:** Very large CT volumes or volumes with unusual dimensions exceed available GPU memory during inference, causing failures or requiring fallback handling.

**Possible causes:**
- Volumes with unusually large axial dimensions or high slice counts.
- Inference patch configuration incompatible with extreme volume shapes.
- GPU memory ceiling on the available hardware.

**Clinical risk if unreviewed:**
- Inference failure means no segmentation output is produced, potentially delaying clinical workflow.
- If a fallback strategy is used (e.g., downsampling), the resulting mask may have reduced resolution or accuracy.

**Current mitigation:**
- Sliding-window inference processes the volume in patches, handling large volumes without loading the entire volume into GPU memory at once.
- The system was tested on the KiTS23 test set (64 cases) without reported inference failures.

**Remaining limitation:**
- The maximum supported volume size has not been formally characterized.
- No graceful degradation strategy (e.g., warning the user, offering lower resolution) is documented.

**Future improvement:**
- Define and document the maximum supported input dimensions.
- Implement memory-aware inference that adapts patch size or overlap to available GPU memory.
- Add input validation with clear error messages for unsupported volumes.

---

### 2.7 Domain Shift from Different Scanner Protocols

**Description:** The model was trained and evaluated exclusively on KiTS23 data. Performance on CT volumes from different scanners, acquisition protocols, contrast phases, or patient populations is unknown and may be significantly worse.

**Possible causes:**
- Different convolution kernels, reconstruction algorithms, and contrast timing produce different image characteristics.
- KiTS23 may have specific inclusion criteria that bias the data distribution.
- The model may rely on spurious correlations specific to the training data distribution.

**Clinical risk if unreviewed:**
- A drop in segmentation accuracy on out-of-distribution data could produce clinically misleading outputs.
- A false sense of reliability if users assume the system generalizes to their local scanner.

**Current mitigation:**
- The system is explicitly described as "evaluated on KiTS23 held-out test cases."
- The report and presentation include a domain shift limitation statement.
- No claim of cross-scanner or cross-institution generalizability is made.
- The system is decision-support only; physician review is required for every output.

**Future improvement:**
- External multi-center validation study as the primary future work item.
- Evaluate domain adaptation techniques.
- Collect and test on data from local hospital scanners to quantify the domain gap.

---

## 3. Summary Table

| Failure Category | Clinical Severity | Current Mitigation Strength | Primary Future Direction |
|------------------|-------------------|-----------------------------|--------------------------|
| Small tumor missed/under-segmented | High | Moderate (100% detection on test set, but not guaranteed) | Size-stratified analysis, detection-focused architecture |
| Tumor boundary leakage | Medium | Moderate (TTA, overlap, HD95 reporting) | Boundary-aware loss, uncertainty maps |
| Cyst/tumor confusion | Medium | Good (labeled as "Tumor/Cyst", documented convention) | Separate cyst/tumor classifier |
| False positive tumor blobs | Medium | Moderate (100-voxel threshold) | Per-blob confidence, second-stage classifier |
| False positive kidney regions | Low | Good (5000-voxel threshold, high kidney Dice) | Organ localization preprocessing |
| Large-volume memory issues | Low | Good (sliding window; no test set failures) | Document max volume, memory-aware inference |
| Domain shift | High | Weak (no external data tested) | External multi-center validation |

---

## 4. Failure Case Documentation Template

Use this template to document each concrete failure case identified during review of the test set predictions.

```markdown
### Case FC-XXX

| Field | Value |
|-------|-------|
| **Case ID** | FC-XXX (anonymized; link to the original case ID in internal records) |
| **Failure Category** | [Select from Section 2 categories] |
| **Date Identified** | TODO |
| **Identified By** | TODO |

#### Ground Truth Summary
- TODO: Description of the true anatomy. Number of lesions, approximate sizes, location.

#### Prediction Summary
- TODO: Description of the model output. What was correct, what was incorrect.

#### Metric Impact
- Kidney Dice: TODO
- Tumor Dice: TODO
- HD95: TODO
- Detection: [Detected / Missed]

#### Visual Evidence
- TODO: Path to side-by-side comparison figure (ground truth vs. prediction overlay).

#### Root Cause Hypothesis
- TODO: Why did this failure occur? Reference relevant sections above.

#### Corrective Action
- TODO: Was a mitigation attempted? With what result? Or is this deferred to future work?
```

---

## 5. Safe Presentation Wording

When discussing failure cases in the defense, use these framing statements:

**Opening the topic:**
- "We conducted a failure case analysis to understand where the system is most and least reliable."

**Describing a failure:**
- "Case [ID] illustrates a boundary leakage failure where the predicted tumor mask extends beyond the true lesion. This is a known challenge with infiltrative tumors and is reflected in our tumor HD95 of 67.35 mm."

**Contextualizing the risk:**
- "If used without physician review, this error could lead to an overestimated tumor volume. This is precisely why the system is decision-support only."

**Connecting to mitigations:**
- "We mitigate this class of error through test-time augmentation and conservative post-processing. However, residual errors remain, and physician review is essential."

**Transitioning to future work:**
- "Addressing this failure mode is a high-priority future work item. We propose boundary-aware loss functions and per-lesion confidence scoring."

**What not to say:**
- "This is a rare edge case." (Unless backed by quantitative evidence.)
- "The model is still good enough." (Defensiveness undermines credibility.)
- "No radiologist could do better." (No comparison was performed.)
- "We fixed this." (If the fix was partial or unvalidated.)

---

## 6. Concrete Failure Cases

> The following entries use the template from Section 4. Items marked `[PLACEHOLDER]` are plausible values. Replace with real anonymized cases from test set review.
>
> **Note:** All failure cases below are constructed to illustrate typical failure modes. The team must replace [PLACEHOLDER] values with actual case data and attach real comparison figures before the defense.

---

### Case FC-001: Boundary Leakage in Infiltrative Tumor

| Field | Value |
|-------|-------|
| **Case ID** | FC-001 (anonymized; internal case ID: case_0042 [PLACEHOLDER]) |
| **Failure Category** | 2.2 Tumor Boundary Leakage |
| **Date Identified** | 12 May 2026 [PLACEHOLDER] |
| **Identified By** | [PLACEHOLDER — team member] |

#### Ground Truth Summary
- Single infiltrative tumor in lower pole of right kidney. ~2,400 voxels. Ill-defined margins with parenchymal infiltration. [PLACEHOLDER — verify]

#### Prediction Summary
- Tumor detected (true positive). Predicted mask extends ~18 voxels beyond true boundary into healthy parenchyma at medial aspect. Kidney segmentation accurate (Dice 0.95). [PLACEHOLDER — verify]

#### Metric Impact
- Kidney Dice: 0.95 [PLACEHOLDER]
- Tumor Dice: 0.52 [PLACEHOLDER] (lower than average due to boundary error)
- HD95: 78 mm [PLACEHOLDER]
- Detection: Detected

#### Visual Evidence
- `failure_cases/fc_001_boundary_leakage.png` [PLACEHOLDER — generate: ground truth (green), prediction (red), overlay (yellow = overlap)]

#### Root Cause Hypothesis
- Infiltrative growth pattern creates ambiguous boundary even on ground truth
- Model tends to over-predict tumor extent when boundary is unclear
- TTA averaging reduced but did not eliminate the over-prediction

#### Corrective Action
- Documented as known limitation
- Future work: boundary-aware loss functions (Boundary loss, Hausdorff loss)
- No immediate code change — physician review is the mitigation

---

### Case FC-002: Small Tumor with Low Contrast

| Field | Value |
|-------|-------|
| **Case ID** | FC-002 (anonymized; internal case ID: case_0017 [PLACEHOLDER]) |
| **Failure Category** | 2.1 Small Tumor Missed or Under-Segmented |
| **Date Identified** | 14 May 2026 [PLACEHOLDER] |
| **Identified By** | [PLACEHOLDER — team member] |

#### Ground Truth Summary
- Small hypodense lesion (~120 voxels) in mid-pole of left kidney. Near-isodense with surrounding parenchyma. [PLACEHOLDER — verify]

#### Prediction Summary
- Tumor detected but under-segmented. Predicted mask is ~45% of ground truth volume (~54 voxels). Boundary contracted toward lesion center. [PLACEHOLDER — verify]

#### Metric Impact
- Kidney Dice: 0.94 [PLACEHOLDER]
- Tumor Dice: 0.38 [PLACEHOLDER] (significantly lower than average)
- HD95: 85 mm [PLACEHOLDER]
- Detection: Detected

#### Visual Evidence
- `failure_cases/fc_002_small_tumor.png` [PLACEHOLDER — generate zoomed-in view to show detail]

#### Root Cause Hypothesis
- Small lesion size makes Dice hypersensitive to boundary errors (1-voxel shift on 120-voxel tumor drops Dice ~0.15)
- Low contrast with parenchyma reduces model confidence at boundary
- Conservative post-processing (100-voxel threshold) did not remove the detection, but could not improve boundary precision

#### Corrective Action
- Documented as known limitation
- Future work: size-stratified analysis, detection-focused architectures
- No immediate code change — detection preserved, boundary is future work

---

### Case FC-003: Cyst with Tumor-Like Appearance

| Field | Value |
|-------|-------|
| **Case ID** | FC-003 (anonymized; internal case ID: case_0058 [PLACEHOLDER]) |
| **Failure Category** | 2.3 Cyst/Tumor Confusion |
| **Date Identified** | 16 May 2026 [PLACEHOLDER] |
| **Identified By** | [PLACEHOLDER — team member] |

#### Ground Truth Summary
- Large simple cyst (~8,500 voxels) in upper pole of right kidney. Well-circumscribed, hypodense (~10-20 HU), no enhancement. [PLACEHOLDER — verify]

#### Prediction Summary
- Cyst correctly segmented as "Tumor/Cyst" class. Segmentation quality good (high Dice ~0.82). However, system cannot distinguish this benign cyst from a malignant tumor. [PLACEHOLDER — verify]

#### Metric Impact
- Kidney Dice: 0.96 [PLACEHOLDER]
- Tumor Dice: 0.82 [PLACEHOLDER] (good segmentation quality)
- HD95: 22 mm [PLACEHOLDER]
- Detection: Detected

#### Visual Evidence
- `failure_cases/fc_003_cyst_confusion.png` [PLACEHOLDER — generate: show good segmentation but note class label ambiguity in caption]

#### Root Cause Hypothesis
- KiTS23 dataset convention merges cyst and tumor into one class
- Model has no information to distinguish cyst from tumor (same label, similar appearance)
- This is a dataset limitation, not a model failure per se

#### Corrective Action
- Documented as known limitation in all outputs
- Output labeled "Tumor/Cyst" not "Tumor"
- Future work: separate cyst/tumor classifier with additional features

---

**Referenced documents:** `MASTER_CONTEXT.md`, `KNOWN_METRICS.md`, `DO_NOT_OVERCLAIM.md`, `challenges_and_solutions.md`, `cyst_and_tumor_detection_challenges.md`.
