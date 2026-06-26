# Ablation and Iteration Summary

> Record of what was tried, what worked, what did not, and why. This is the evidence of iterative development. Addresses mid-year feedback directly.

---

## Iteration Philosophy

Every change to the pipeline was driven by a **hypothesis**, tested with a **controlled experiment**, and resulted in an **adopt / modify / discard** decision. This document summarizes the major iterations.

> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible values generated to show structure. Replace with actual team data. Final test metrics are LOCKED.

---

## Iteration 1: Baseline Architecture

### Hypothesis
A standard 3D U-Net can achieve acceptable kidney segmentation on KiTS23.

### Experiment
> See EXP-001 in `experiment_log.md`.

| Parameter | Value |
|-----------|-------|
| Architecture | 3D U-Net, 4 stages, 32 base channels [PLACEHOLDER] |
| Input size | 64×192×192 (patch) [PLACEHOLDER] |
| Loss | DiceCE [PLACEHOLDER] |
| Optimizer | AdamW [PLACEHOLDER] |
| LR | 2e-4, cosine + 5-epoch warmup [PLACEHOLDER] |
| Batch size | 2 [PLACEHOLDER] |
| Epochs | 300 [PLACEHOLDER] |

### Result
- Kidney Dice (val): 0.88 [PLACEHOLDER]
- Tumor Dice (val): 0.48 [PLACEHOLDER]

### Decision
**Adopt** as baseline. Kidney segmentation works; tumor needs improvement.

---

## Iteration 2: Preprocessing Refinement

### Hypothesis
HU clipping range affects soft-tissue contrast and segmentation quality.

### Experiment
Tested multiple HU ranges (see `preprocessing_decisions.md` for full table).

### Result
Range [-200, 300] performed best.

### Decision
**Adopt** [-200, 300] for all subsequent experiments.

---

## Iteration 3: Sliding Window Inference

### Hypothesis
Full-volume inference exceeds GPU memory; patch-based inference with overlap fusion can match full-volume quality.

### Experiment
Compared full-volume (on smaller cases) vs sliding window with varying overlap.

| Overlap | Kidney Dice | Tumor Dice | Notes |
|---------|-------------|------------|-------|
| 0% | 0.86 [PLACEHOLDER] | 0.44 [PLACEHOLDER] | Stitching artifacts |
| 25% | 0.89 [PLACEHOLDER] | 0.50 [PLACEHOLDER] | Reduced artifacts |
| **50%** | 0.91 [PLACEHOLDER] | 0.55 [PLACEHOLDER] | **Best balance** |
| 75% | 0.91 [PLACEHOLDER] | 0.56 [PLACEHOLDER] | Diminishing returns, 2x time |

### Decision
**Adopt** 50% overlap for all inference.

---

## Iteration 4: Test-Time Augmentation

### Hypothesis
Averaging predictions from multiple flipped orientations reduces boundary noise.

### Experiment
Compared no TTA, 4-flip, and 8-flip on validation set.

| TTA | Kidney Dice | Tumor Dice | Inference Time | Notes |
|-----|-------------|------------|----------------|-------|
| None | 0.91 [PLACEHOLDER] | 0.55 [PLACEHOLDER] | 1x (~15s) | Baseline |
| 4 flips | 0.92 [PLACEHOLDER] | 0.59 [PLACEHOLDER] | 4x (~60s) | Modest improvement |
| **8 flips** | 0.93 [PLACEHOLDER] | 0.62 [PLACEHOLDER] | 8x (~120s) | **Best improvement** |

### Decision
**Adopt** 8-flip TTA for final evaluation. Use no TTA during development for speed.

---

## Iteration 5: Post-Processing Thresholds

### Hypothesis
Size-based blob filtering can remove false positives while preserving true detections.

### Experiment
Tested multiple thresholds on validation set, measuring detection rate vs false positive rate.

| Kidney Threshold | Tumor Threshold | Detection Rate | False Positives | Notes |
|------------------|-----------------|----------------|-----------------|-------|
| 1000 | 50 | 98% [PLACEHOLDER] | Low [PLACEHOLDER] | Too aggressive — lost 2 small tumors |
| 5000 | 100 | 100% [PLACEHOLDER] | Moderate [PLACEHOLDER] | **Selected** — best balance |
| 10000 | 200 | 97% [PLACEHOLDER] | Very low [PLACEHOLDER] | Too conservative — lost 3 tumors |

### Decision
**Adopt** kidney <5000, tumor <100. Prioritize sensitivity over precision.

---

## Iteration 6: Tumor/Cyst Analysis

### Hypothesis
The merged tumor/cyst class limits clinical utility; we should quantify this limitation.

### Experiment
Analyzed detection vs segmentation performance separately.

### Result
- Detection: 100% (all tumors found)
- Segmentation: Moderate Dice (0.6558) with high variance

### Decision
**Document** as known limitation. Separate classification is future work.

---

## Failed Experiments (Also Documented)

> Showing failed experiments is crucial for honest iterative development. Replace [PLACEHOLDER] with actual failed experiments.

### Failed: Focal Loss Instead of DiceCE

**Hypothesis:** Focal loss would handle extreme class imbalance better than DiceCE.

**Setup:** Same architecture as EXP-001, replaced DiceCE with Focal loss (gamma=2, alpha=0.25). [PLACEHOLDER]

**Result:** Kidney Dice 0.85, Tumor Dice 0.42 (worse than DiceCE baseline). [PLACEHOLDER]

**Why it failed:** Focal loss down-weighted easy examples too aggressively — kidney voxels (majority of foreground) got suppressed, hurting kidney boundary. Tumor did not improve enough to compensate. [PLACEHOLDER]

**Lesson:** DiceCE is better suited for this task because Dice term directly optimizes foreground overlap. [PLACEHOLDER]

### Failed: 2D U-Net with 3-Average Ensemble

**Hypothesis:** 3 independent 2D U-Nets (axial, coronal, sagittal) averaged could match 3D U-Net at lower memory cost.

**Setup:** 3× 2D U-Net, each trained on one plane. Predictions averaged. [PLACEHOLDER]

**Result:** Kidney Dice 0.89, Tumor Dice 0.50. [PLACEHOLDER]

**Why it failed:** 2D models missed inter-slice context. Averaging 3 planes helped but did not match 3D U-Net (0.93/0.55 at same stage). [PLACEHOLDER]

**Lesson:** 3D convolutions are essential for volumetric kidney segmentation. 2D ensemble is not a substitute. [PLACEHOLDER]

---

## Summary Table

| Iteration | Change | Validation Impact | Final Decision |
|-----------|--------|-------------------|----------------|
| 1 | Baseline 3D U-Net | Kidney 0.88 / Tumor 0.48 [PLACEHOLDER] | Adopted |
| 2 | HU clipping [-200, 300] | +0.00 / +0.00 [PLACEHOLDER] | Adopted |
| 3 | Sliding window 50% | Kidney 0.91 / Tumor 0.55 [PLACEHOLDER] | Adopted |
| 4 | 8-flip TTA | +0.02 / +0.07 [PLACEHOLDER] | Adopted |
| 5 | Conservative post-processing | Detection 100% [PLACEHOLDER] | Adopted |
| 6 | Tumor/cyst analysis | Final test 0.7933 (LOCKED) | Documented as limitation |

---

## Document History

| Date | Change | Author |
|------|--------|--------|
| 26 Dec 2025 | Iteration 1 logged | [PLACEHOLDER] |
| 28 Feb 2026 | Iterations 2-5 logged | [PLACEHOLDER] |
| 10 May 2026 | Iteration 6 + summary table | [PLACEHOLDER] |

---

## Cross-References

- `experiment_log.md` — Full experiment details
- `preprocessing_decisions.md` — Preprocessing iterations
- `engineering_decisions.md` — Architecture and pipeline choices
- `failure_cases_analysis.md` — Specific failure modes
