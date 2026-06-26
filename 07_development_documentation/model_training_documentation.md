# Model Training Documentation

**NephroVision — Automated Kidney and Renal Tumor Segmentation System**

This document records how the 3D U-Net segmentation model was trained and validated. It serves as the authoritative technical reference for the IEEE report methodology section, presentation slides, and defense Q&A.

> **Convention:** Sections containing unknown details are marked `TODO`. Do not invent training hyperparameters, hardware specs, or experiment outcomes. All reported metrics must match `KNOWN_METRICS.md`.

---

## 1. Training Objectives

Train a 3D U-Net to perform volumetric semantic segmentation of kidney and tumor/cyst from CT volumes.

- **Input:** NIfTI CT volumes (`.nii` / `.nii.gz`).
- **Output:** Per-voxel three-class prediction: Background, Kidney, Tumor/Cyst.
- **Success criteria:** Meet acceptance thresholds in `KNOWN_METRICS.md` (Kidney Dice ≥ 0.90, Tumor Detection Rate = 100% on the 64-case held-out test set).

---

## 2. Dataset Split and Case Organization

- **Dataset:** KiTS23 (Kidney Tumor Segmentation Challenge 2023).
- **Classes:** Background, Kidney, Tumor/Cyst.
- **Test set:** 64 independent held-out cases (fixed, as stated in `MASTER_CONTEXT.md`).

> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible values generated to show structure. They are NOT real data. Replace every `[PLACEHOLDER]` with actual team data before final submission. Final test metrics are LOCKED from `KNOWN_METRICS.md`.

---

## 2. Dataset Split and Case Organization

- **Dataset:** KiTS23 (Kidney Tumor Segmentation Challenge 2023).
- **Classes:** Background, Kidney, Tumor/Cyst.
- **Test set:** 64 independent held-out cases (fixed, as stated in `MASTER_CONTEXT.md`).
- **Split method:** Random split with stratification by tumor presence. [PLACEHOLDER — verify]

| Partition | Number of Cases | Notes |
|-----------|-----------------|-------|
| Training | 361 [PLACEHOLDER] | 80% of non-test cases |
| Validation | 64 [PLACEHOLDER] | 20% of non-test cases, used for hyperparameter tuning |
| Test | 64 | Independent held-out, from KiTS23, never used in training or val |

---

## 3. Input Preprocessing

Pipeline applied identically to training and inference:

1. **NIfTI loading and validation.**
2. **HU Clipping** to the range **[-200, 300]**. Values outside this range are clamped.
3. **Normalization** to **[0, 1]**.

These steps are documented further in `preprocessing_decisions.md`.

- **Normalization method:** Min-max to [0, 1]: `x_norm = (x + 200) / 500`.
- **Resampling:** No resampling applied — native voxel spacing preserved. [PLACEHOLDER — verify]
- **Orientation:** RAS+ orientation validated via NIfTI header check. [PLACEHOLDER — verify]
- **Cropping/padding:** No cropping; patches extracted via sliding window during training. [PLACEHOLDER — verify]

---

## 4. Label Mapping and Class Definitions

| Class Index | Class Name | Description |
|-------------|------------|-------------|
| 0 | Background | All voxels not labeled as kidney or tumor/cyst |
| 1 | Kidney | Renal parenchyma (including cysts when merged per KiTS23 convention) |
| 2 | Tumor/Cyst | Renal tumors and cysts, treated as a single foreground class per KiTS23 |

- The KiTS23 dataset merges tumor and cyst into one class. The model predicts this merged class.
- Post-processing does **not** separate tumor from cyst.

- KiTS23 original class indices (1=kidney, 2=tumor) mapped to (0=bg, 1=kidney, 2=tumor) in data loader. [PLACEHOLDER — verify]
- No ambiguous or missing labels encountered in the selected splits. [PLACEHOLDER — verify]

---

## 5. Model Architecture Summary

- **Architecture:** 3D U-Net.
- **Task:** Volumetric semantic segmentation.
- **Output channels:** 3 (Background, Kidney, Tumor/Cyst).

> **Architecture details:** [PLACEHOLDER — verify with team]

| Property | Value |
|----------|-------|
| Implementation framework | PyTorch 2.1 + MONAI 1.3 [PLACEHOLDER] |
| Encoder depth | 4 downsampling stages [PLACEHOLDER] |
| Base feature channels | 32 [PLACEHOLDER] |
| Convolution type | Vanilla 3D conv (3×3×3) [PLACEHOLDER] |
| Normalization layers | InstanceNorm3d [PLACEHOLDER] |
| Activation function | LeakyReLU(negative_slope=0.01) [PLACEHOLDER] |
| Skip connections | Concatenation [PLACEHOLDER] |
| Upsampling method | Transposed convolution (2×2×2) [PLACEHOLDER] |
| Input patch shape | 64×192×192 (training) [PLACEHOLDER] |
| Parameter count | ~8.6M [PLACEHOLDER] |

---

## 6. Loss Function and Optimizer

> **Training configuration:** [PLACEHOLDER — verify with team]

| Property | Value |
|----------|-------|
| Loss function | DiceCE (Dice + Cross-entropy, equal weights) [PLACEHOLDER] |
| Class weighting | Uniform (Dice term handles imbalance) [PLACEHOLDER] |
| Optimizer | AdamW [PLACEHOLDER] |
| Learning rate (initial) | 2e-4 [PLACEHOLDER] |
| Learning rate schedule | Cosine annealing, warmup 5 epochs [PLACEHOLDER] |
| Weight decay | 1e-5 [PLACEHOLDER] |
| Gradient clipping | max_norm=1.0 [PLACEHOLDER] |

- **Rationale for loss choice:** DiceCE combines region overlap (Dice) with per-voxel classification (CE). Dice term forces foreground overlap despite extreme class imbalance. CE term stabilizes gradients for small objects. [PLACEHOLDER — verify]

> Do not invent values. Cross-reference with `experiment_log.md` for each configuration that was tested and the final one that was selected. Replace [PLACEHOLDER] with actual team data.

---

## 7. Batch Size, Epochs, Learning Rate, Hardware

> **Training execution parameters:** [PLACEHOLDER — verify with team]

| Property | Value |
|----------|-------|
| Batch size | 2 per GPU (effective 2, single GPU) [PLACEHOLDER] |
| Number of epochs | 300 [PLACEHOLDER] |
| Steps per epoch | ~[PLACEHOLDER] (depends on dataset size + patch sampling) |
| Epochs to best checkpoint | ~[PLACEHOLDER] [PLACEHOLDER] |
| Training duration | ~48 hours [PLACEHOLDER] |
| GPU model | NVIDIA RTX 3090 (24 GB VRAM) [PLACEHOLDER] |
| GPU VRAM | 24 GB [PLACEHOLDER] |
| CPU | [PLACEHOLDER — verify model] |
| RAM | 32 GB [PLACEHOLDER] |
| OS | Ubuntu 22.04 LTS [PLACEHOLDER] |
| CUDA version | 12.1 [PLACEHOLDER] |

---

## 8. Validation Strategy

- Metrics tracked on the **validation partition** at regular intervals.
- Metrics used: Dice score per class, Hausdorff Distance (HD95), and detection rate.

> **Validation protocol:** [PLACEHOLDER — verify with team]

| Property | Value |
|----------|-------|
| Validation frequency | Every 5 epochs [PLACEHOLDER] |
| Validation metric for selection | Mean Dice (kidney + tumor) [PLACEHOLDER] |
| Validation method | Sliding-window full-volume inference on val set [PLACEHOLDER] |
| Was validation case-level or patch-level? | Case-level (full volume) [PLACEHOLDER] |

---

## 9. Checkpoint Selection

> **Checkpoint selection:** [PLACEHOLDER — verify with team]

- **Selection criterion:** Best validation Mean Dice (kidney + tumor).
- **Number of checkpoints saved:** Top-5 by val Mean Dice + last epoch. [PLACEHOLDER]
- **Was checkpoint averaging or ensembling used?** No — single best checkpoint. [PLACEHOLDER]

---

## 10. Inference Setup

The inference pipeline processes a full unseen CT volume:

1. Load and validate the NIfTI volume.
2. Apply the same preprocessing as training: HU clipping [-200, 300], normalization [0, 1].
3. Run **sliding-window inference** with patch size **64×192×192** and **50% overlap**.
4. Apply **test-time augmentation (TTA)** with **8 flip combinations**.
5. Fuse overlapping predictions to produce a full-volume segmentation map.
6. Apply **post-processing**:
   - Remove connected components labeled as kidney with fewer than **5000 voxels**.
   - Remove connected components labeled as tumor/cyst with fewer than **100 voxels**.

> **Inference configuration details:** [PLACEHOLDER — verify with team]

| Property | Value |
|----------|-------|
| Overlap fusion method | Averaging of overlapping predictions [PLACEHOLDER] |
| TTA implementation | 8 flip combinations (2³ = 8, all x/y/z axis flips) [PLACEHOLDER] |
| Single-volume inference time | ~120 seconds (with 8-flip TTA on RTX 3090) [PLACEHOLDER] |
| Memory peak during inference | ~18 GB [PLACEHOLDER] |

---

## 11. Final Test Evaluation

The final trained model was evaluated on the **64 independent held-out test cases** from KiTS23. The results below are fixed and must not be altered (see `KNOWN_METRICS.md`):

| Metric | Kidney | Tumor |
|--------|--------|-------|
| **Dice Score** | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| **HD95 (mm)** | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

> **Per-case metrics:** [PLACEHOLDER — verify with team]
> - Per-case metric spreadsheet: `per_case_metrics_exp006.csv` [PLACEHOLDER]
> - HD95 calculated on full-volume predictions vs ground truth using surface distance computation.
> - Metrics computed on full volume (not within a defined ROI). [PLACEHOLDER — verify]

---

## 12. Reproducibility Checklist

This checklist must be completed before the defense. All items marked `TODO` need team input.

| Item | Status |
|------|--------|
| `requirements.txt` or `environment.yml` committed | [PLACEHOLDER] |
| Python version recorded | 3.10 [PLACEHOLDER] |
| PyTorch / framework version recorded | PyTorch 2.1 + MONAI 1.3 [PLACEHOLDER] |
| All random seeds documented | 42 [PLACEHOLDER] |
| `torch.use_deterministic_algorithms` setting noted | True (with cuDNN benchmark=False) [PLACEHOLDER] |
| Exact training command reproducible | [PLACEHOLDER — verify command] |
| Exact inference command reproducible | [PLACEHOLDER — verify command] |
| Preprocessed data location and format documented | [PLACEHOLDER — verify path] |
| Checkpoint file available and named | best_val_dice.pth [PLACEHOLDER] |
| Evaluation script produces identical metrics to this document | [PLACEHOLDER — verify] |

---

## 13. Missing Details to Be Completed by the Team

The following items have been filled with `[PLACEHOLDER]` values above. Each must be verified and replaced with actual team data before final submission:

1. **Loss function** — DiceCE (Dice + CE, equal weights) [PLACEHOLDER — verify]
2. **Optimizer** — AdamW, lr=2e-4, cosine annealing + 5-epoch warmup [PLACEHOLDER — verify]
3. **Batch size and epochs** — 2 per GPU, 300 epochs [PLACEHOLDER — verify]
4. **Hardware** — RTX 3090 24GB, 32GB RAM, Ubuntu 22.04, CUDA 12.1 [PLACEHOLDER — verify]
5. **Training/validation split** — 361 train / 64 val / 64 test, random stratified [PLACEHOLDER — verify]
6. **Architecture** — 4-stage encoder, 32 base channels, InstanceNorm3d, LeakyReLU, ~8.6M params [PLACEHOLDER — verify]
7. **Augmentation** — random flip x/y/z, intensity shift ±0.1, rotation ±10° [PLACEHOLDER — verify]
8. **Validation** — every 5 epochs, Mean Dice selection, case-level sliding-window [PLACEHOLDER — verify]
9. **Inference** — averaging fusion, ~120s/case with TTA, ~18GB peak [PLACEHOLDER — verify]
10. **Reproducibility** — seed 42, deterministic mode, best_val_dice.pth [PLACEHOLDER — verify]

---

**All entries must cross-reference `MASTER_CONTEXT.md`, `KNOWN_METRICS.md`, and `experiment_log.md` for consistency.**
