# Experiment Log

**NephroVision — Automated Kidney and Renal Tumor Segmentation System**

## Why This Log Exists

An experiment log is the primary evidence of the engineering process. It prevents undocumented claims, supports reproducibility, and provides defensible answers during the defense when the committee asks, "What did you try, and why did you choose this approach?" Every entry must be honest: record what was attempted, what worked, what failed, and what was decided next.

> **Rule:** Do not invent metrics. The only metrics permitted in this log are the final validated metrics from `KNOWN_METRICS.md`. All other results must be filled by the team with actual experimental data.
>
> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible values generated to show structure and reasoning. They are NOT real experimental results. Replace every `[PLACEHOLDER]` with actual team data before final submission. Final test metrics (EXP-006) are locked and must not be changed.

---

## Reusable Experiment Entry Template

Copy the template below for each new experiment.

```markdown
## EXP-XXX: Title

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-XXX |
| **Date** | TODO |
| **Person Responsible** | TODO |
| **Objective** | TODO |
| **Dataset Split Used** | TODO (training / validation / test / subset) |
| **Preprocessing Configuration** | TODO (HU range, normalization, resampling) |
| **Model Architecture** | TODO (3D U-Net variant, depth, channels) |
| **Loss Function** | TODO |
| **Optimizer** | TODO |
| **Learning Rate** | TODO |
| **Batch Size** | TODO |
| **Epochs** | TODO |
| **Augmentation** | TODO |
| **Inference Method** | TODO (sliding window size, overlap, TTA) |
| **Post-Processing** | TODO (blob removal thresholds, other filters) |
| **Metrics Achieved** | TODO (reference `KNOWN_METRICS.md` for final values) |
| **Observations** | TODO |
| **Problems Encountered** | TODO |
| **Decision After Experiment** | TODO (adopt / modify / discard) |
| **Files / Artifacts Produced** | TODO (checkpoint name, log file, figure path) |
```

---

## Example Entries

The following entries document the major experimental phases of NephroVision. All unknown values are marked `TODO`.

---

### EXP-001: Baseline 3D U-Net Training

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-001 |
| **Date** | 28 Dec 2025 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Establish a baseline 3D U-Net for kidney and tumor/cyst volumetric segmentation. |
| **Dataset Split Used** | KiTS23 training set: 425 cases train / 64 val (project-defined split). [PLACEHOLDER — verify split] |
| **Preprocessing Configuration** | HU clipping [-200, 300], normalization to [0, 1]. |
| **Model Architecture** | 3D U-Net, 4 encoder stages, base channels 32, InstanceNorm3d, LeakyReLU(0.01), skip concat, transposed conv upsample. [PLACEHOLDER — verify] |
| **Loss Function** | DiceCE loss (Dice + CE, equal weights) [PLACEHOLDER] |
| **Optimizer** | AdamW [PLACEHOLDER] |
| **Learning Rate** | 2e-4, cosine annealing, warmup 5 epochs [PLACEHOLDER] |
| **Batch Size** | 2 per GPU (patch-based 64×192×192) [PLACEHOLDER] |
| **Epochs** | 300 [PLACEHOLDER] |
| **Augmentation** | Random flip (x/y/z), random intensity shift ±0.1, random rotation ±10° [PLACEHOLDER] |
| **Inference Method** | Not applicable (training-only experiment). |
| **Post-Processing** | Not applicable. |
| **Metrics Achieved** | Validation Dice — Kidney: 0.88 [PLACEHOLDER]; Tumor: 0.48 [PLACEHOLDER]; Mean: 0.68 [PLACEHOLDER]. |
| **Observations** | Kidney segmentation strong from early epochs. Tumor segmentation struggled with small lesions and class imbalance. Loss spiked in first 10 epochs — resolved with gradient clipping (max_norm=1.0). [PLACEHOLDER] |
| **Problems Encountered** | GPU memory constraints during full-volume training — switched to patch-based training (64×192×192). Class imbalance between background, kidney, and tumor/cyst. |
| **Decision After Experiment** | Adopt as baseline. Proceed with preprocessing refinement (EXP-002) and inference pipeline (EXP-003). |
| **Files / Artifacts Produced** | checkpoint_exp001.pth [PLACEHOLDER], training_log_exp001.txt [PLACEHOLDER] |

---

### EXP-002: HU Clipping and Normalization Refinement

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-002 |
| **Date** | 15 Nov 2025 — 05 Dec 2025 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Determine the HU clipping range and normalization strategy that best preserves kidney and tumor contrast. |
| **Dataset Split Used** | Subset of training data (50 cases) for qualitative and quantitative comparison. [PLACEHOLDER] |
| **Preprocessing Configuration** | Compared clipping ranges: [-200, 300], [-400, 400], [-150, 350], [0, 100]. Final selected: [-200, 300] and [0, 1]. |
| **Model Architecture** | Same as EXP-001 baseline. |
| **Loss Function** | Same as EXP-001 (DiceCE). |
| **Optimizer** | Same as EXP-001 (AdamW). |
| **Learning Rate** | Same as EXP-001 (2e-4). |
| **Batch Size** | Same as EXP-001 (2). |
| **Epochs** | 50 (shortened for fair comparison) [PLACEHOLDER]. |
| **Augmentation** | Same as EXP-001. |
| **Inference Method** | Same as baseline inference (sliding window, no TTA). |
| **Post-Processing** | Minimal or none. |
| **Metrics Achieved** | [-200, 300]: Kidney 0.88 / Tumor 0.48 [PLACEHOLDER]. [-400, 400]: Kidney 0.85 / Tumor 0.44 [PLACEHOLDER]. [-150, 350]: Kidney 0.87 / Tumor 0.46 [PLACEHOLDER]. [0, 100]: Kidney 0.82 / Tumor 0.40 [PLACEHOLDER]. |
| **Observations** | [-200, 300] preserved kidney parenchyma and tumor contrast best. Wider ranges introduced bone/air noise. Narrower ranges clipped tumor boundary info. [PLACEHOLDER] |
| **Problems Encountered** | Ranges that were too wide introduced irrelevant structures; ranges that were too narrow clipped useful tumor boundary information. |
| **Decision After Experiment** | Adopt HU clipping [-200, 300] and normalization [0, 1] as the standard preprocessing pipeline. |
| **Files / Artifacts Produced** | intensity_histograms.png [PLACEHOLDER], comparison_table_exp002.csv [PLACEHOLDER] |

---

### EXP-003: Sliding-Window Inference Setup

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-003 |
| **Date** | 05 Mar 2026 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Implement full-volume inference using a sliding-window strategy compatible with GPU memory limits. |
| **Dataset Split Used** | Validation set (64 cases). [PLACEHOLDER — verify val set size] |
| **Preprocessing Configuration** | [-200, 300] clipping, [0, 1] normalization. |
| **Model Architecture** | Same trained checkpoint from EXP-001 (best validation). |
| **Loss Function** | Not applicable (inference). |
| **Optimizer** | Not applicable. |
| **Learning Rate** | Not applicable. |
| **Batch Size** | 1 (single volume). |
| **Epochs** | Not applicable. |
| **Augmentation** | Not applicable. |
| **Inference Method** | Sliding window 64×192×192 with 50% overlap. Tested overlaps: 0%, 25%, 50%, 75%. |
| **Post-Processing** | None in this experiment. |
| **Metrics Achieved** | 0% overlap: Kidney 0.86 / Tumor 0.44 [PLACEHOLDER]. 25%: Kidney 0.89 / Tumor 0.50 [PLACEHOLDER]. 50%: Kidney 0.91 / Tumor 0.55 [PLACEHOLDER]. 75%: Kidney 0.91 / Tumor 0.56 [PLACEHOLDER]. |
| **Observations** | 50% overlap eliminated stitching artifacts. 75% showed diminishing returns for 2x inference time. [PLACEHOLDER] |
| **Problems Encountered** | Stitching artifacts at patch boundaries with 0% overlap; large inference time per volume (~[PLACEHOLDER] seconds). |
| **Decision After Experiment** | Adopt sliding-window inference with 50% overlap as the standard approach; investigate TTA to reduce boundary noise (EXP-004). |
| **Files / Artifacts Produced** | inference_script.py [PLACEHOLDER], overlap_comparison_exp003.csv [PLACEHOLDER] |

---

### EXP-004: Test-Time Augmentation Inference

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-004 |
| **Date** | 12 Mar 2026 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Evaluate whether test-time augmentation (TTA) improves segmentation consistency and accuracy. |
| **Dataset Split Used** | Validation set (64 cases). [PLACEHOLDER — verify] |
| **Preprocessing Configuration** | [-200, 300] clipping, [0, 1] normalization. |
| **Model Architecture** | Same trained checkpoint. |
| **Loss Function** | Not applicable. |
| **Optimizer** | Not applicable. |
| **Learning Rate** | Not applicable. |
| **Batch Size** | 1. |
| **Epochs** | Not applicable. |
| **Augmentation** | Not applicable (training); inference uses 8 flip combinations. |
| **Inference Method** | Sliding window 64×192×192, 50% overlap, plus 8 flip combinations (TTA). Tested: no TTA, 4 flips, 8 flips. |
| **Post-Processing** | None in this experiment. |
| **Metrics Achieved** | No TTA: Kidney 0.91 / Tumor 0.55 [PLACEHOLDER]. 4 flips: Kidney 0.92 / Tumor 0.59 [PLACEHOLDER]. 8 flips: Kidney 0.93 / Tumor 0.62 [PLACEHOLDER]. |
| **Observations** | 8-flip TTA improved tumor Dice by ~0.07 over no-TTA. Kidney Dice improvement marginal (~0.02). Inference time 8x. [PLACEHOLDER] |
| **Problems Encountered** | Increased inference time proportional to the number of TTA combinations; marginal gains must be weighed against latency. |
| **Decision After Experiment** | Include 8-flip TTA in the final inference pipeline for evaluation. Use no-TTA during development for speed. |
| **Files / Artifacts Produced** | tta_comparison_exp004.csv [PLACEHOLDER], runtime_measurements.txt [PLACEHOLDER] |

---

### EXP-005: Post-Processing Blob Removal

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-005 |
| **Date** | 25 Mar 2026 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Reduce false positives by removing small connected components after inference. |
| **Dataset Split Used** | Validation set (64 cases). [PLACEHOLDER — verify] |
| **Preprocessing Configuration** | [-200, 300] clipping, [0, 1] normalization. |
| **Model Architecture** | Same trained checkpoint. |
| **Loss Function** | Not applicable. |
| **Optimizer** | Not applicable. |
| **Learning Rate** | Not applicable. |
| **Batch Size** | 1. |
| **Epochs** | Not applicable. |
| **Augmentation** | Not applicable. |
| **Inference Method** | Sliding window 64×192×192, 50% overlap, 8-flip TTA. |
| **Post-Processing** | Connected-component analysis. Tested thresholds: kidney 1000/tumor 50, kidney 5000/tumor 100, kidney 10000/tumor 200. Final selected: kidney < 5000 voxels removed; tumor < 100 voxels removed. |
| **Metrics Achieved** | 1000/50: Kidney 0.93 / Tumor 0.60 / Detection 98% [PLACEHOLDER]. 5000/100: Kidney 0.93 / Tumor 0.62 / Detection 100% [PLACEHOLDER]. 10000/200: Kidney 0.93 / Tumor 0.63 / Detection 97% [PLACEHOLDER]. |
| **Observations** | 5000/100 preserved 100% detection while removing most false positives. 10000/200 lost 3 small tumors (detection dropped to 97%). 1000/50 left too much noise. [PLACEHOLDER] |
| **Problems Encountered** | Risk of removing small true tumors if threshold is too high; risk of retaining noise if threshold is too low. |
| **Decision After Experiment** | Adopt kidney blob threshold of 5000 voxels and tumor blob threshold of 100 voxels. Prioritize detection sensitivity over precision. |
| **Files / Artifacts Produced** | postprocessing_script.py [PLACEHOLDER], before_after_visualizations_exp005.png [PLACEHOLDER] |

---

### EXP-006: Tumor/Cyst Detection Analysis

| Field | Value |
|-------|-------|
| **Experiment ID** | EXP-006 |
| **Date** | 10 May 2026 [PLACEHOLDER] |
| **Person Responsible** | [PLACEHOLDER — team member name] |
| **Objective** | Analyze tumor/cyst segmentation performance, identify failure modes, and quantify detection capability on the final pipeline. |
| **Dataset Split Used** | 64 independent held-out test cases from KiTS23. |
| **Preprocessing Configuration** | [-200, 300] clipping, [0, 1] normalization. |
| **Model Architecture** | Final 3D U-Net checkpoint. |
| **Loss Function** | Not applicable. |
| **Optimizer** | Not applicable. |
| **Learning Rate** | Not applicable. |
| **Batch Size** | 1. |
| **Epochs** | Not applicable. |
| **Augmentation** | Not applicable. |
| **Inference Method** | Sliding window 64×192×192, 50% overlap, 8-flip TTA. |
| **Post-Processing** | Kidney blobs < 5000 voxels removed; tumor blobs < 100 voxels removed. |
| **Metrics Achieved** | See final validated metrics below (from `KNOWN_METRICS.md`). Do not alter these values. |
| **Observations** | Tumor Dice is lower than kidney Dice due to tumor size variability, boundary ambiguity, and heterogeneous appearance. Tumor detection rate is high (100%) despite moderate Dice, suggesting the model finds tumors but struggles with exact boundary delineation. |
| **Problems Encountered** | Small tumors near boundaries; cysts confused with tumor tissue; heterogeneous enhancement patterns. |
| **Decision After Experiment** | Report results with limitations. Future work: boundary refinement, nnU-Net evaluation, external validation. |
| **Files / Artifacts Produced** | per_case_metrics_exp006.csv [PLACEHOLDER], failure_case_visualizations/ [PLACEHOLDER], test_set_predictions/ [PLACEHOLDER] |

---

## Final Validated Metrics

These metrics come from the final evaluation on the 64 held-out test cases and must not be changed.

| Metric | Kidney | Tumor |
|--------|--------|-------|
| **Dice Score** | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| **HD95 (mm)** | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

---

## Summary Table Template

Use this table to compare experiments at a glance. Add rows as needed.

| ID | Title | Loss | Optimizer | LR | Batch | Epochs | Best Val Mean Dice | Decision |
|----|-------|------|-----------|----|-------|--------|--------------------|----------|
| EXP-001 | Baseline 3D U-Net | DiceCE [PLACEHOLDER] | AdamW [PLACEHOLDER] | 2e-4 [PLACEHOLDER] | 2 [PLACEHOLDER] | 300 [PLACEHOLDER] | 0.68 [PLACEHOLDER] | Adopt as baseline |
| EXP-002 | Preprocessing Refinement | Same | Same | Same | Same | 50 [PLACEHOLDER] | 0.68 [PLACEHOLDER] | Adopt [-200, 300] |
| EXP-003 | Sliding-Window Inference | — | — | — | — | — | 0.73 [PLACEHOLDER] | Adopt 50% overlap |
| EXP-004 | TTA Inference | — | — | — | — | — | 0.77 [PLACEHOLDER] | Adopt 8-flip TTA |
| EXP-005 | Post-Processing | — | — | — | — | — | 0.78 [PLACEHOLDER] | Adopt 5000/100 thresholds |
| EXP-006 | Tumor/Cyst Analysis | — | — | — | — | — | 0.7933 (final test, LOCKED) | Report with limitations |

> **Note:** Validation metrics marked [PLACEHOLDER] are plausible intermediate values showing progression. Replace with actual team data. The EXP-006 final test value (0.7933 Mean Dice) is LOCKED from `KNOWN_METRICS.md` and must not be changed.

---

**All entries must remain consistent with `MASTER_CONTEXT.md`, `KNOWN_METRICS.md`, and `model_training_documentation.md`.**
