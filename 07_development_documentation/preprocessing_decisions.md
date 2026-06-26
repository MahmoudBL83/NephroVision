# Preprocessing Decisions

> Documented rationale for every preprocessing choice. Addresses mid-year feedback: "show what was done, not just the final result."
>
> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible values generated to show structure. Replace with actual team data.

---

## 1. HU Clipping Range: [-200, 300]

### Decision
Clip CT Hounsfield Unit (HU) values to the range **[-200, 300]** before normalization.

### Rationale
- **Kidney parenchyma** typically ranges from ~20-70 HU (contrast-enhanced)
- **Tumor tissue** typically ranges from ~30-90 HU
- **Bone** exceeds 300 HU and is not relevant for kidney segmentation
- **Air** is below -200 HU and is not relevant
- The range [-200, 300] captures all relevant soft-tissue contrast while suppressing bone and air

### Empirical Evaluation
> [TODO: Fill with actual tested ranges and validation results]

| Range Tested | Kidney Dice (Val) | Tumor Dice (Val) | Notes |
|-------------|-------------------|------------------|-------|
| [-200, 300] | 0.88 [PLACEHOLDER] | 0.48 [PLACEHOLDER] | **Selected** — best balance |
| [-400, 400] | 0.85 [PLACEHOLDER] | 0.44 [PLACEHOLDER] | Includes more bone, no benefit |
| [-150, 350] | 0.87 [PLACEHOLDER] | 0.46 [PLACEHOLDER] | Slightly wide, marginal loss |
| [0, 100] | 0.82 [PLACEHOLDER] | 0.40 [PLACEHOLDER] | Too narrow, loses tumor contrast |

### Date Evaluated
15 Nov — 05 Dec 2025 [PLACEHOLDER]

---

## 2. Normalization: Min-Max to [0, 1]

### Formula
```
x_norm = (x + 200) / 500
```

Where:
- `x` = clipped HU value
- `+200` shifts minimum to 0
- `/500` scales range to [0, 1]

### Rationale
- Simple, reproducible, no dataset-dependent statistics
- Identical transformation for training and inference prevents distribution mismatch
- No reliance on batch statistics (unlike batch normalization)

### Critical Rule
> **Training and inference must use identical preprocessing.** Any difference causes distribution shift and performance degradation.

---

## 3. NIfTI Standardization

### Problem
KiTS23 cases come from multiple centers with varying NIfTI metadata (orientation, spacing, origin).

### Validation Pipeline
> [TODO: Describe the validation steps performed on each input volume]

1. **Orientation check**: Verify RAS+ orientation [PLACEHOLDER — confirm]
2. **Spacing check**: Verify spacing in typical range (~0.5-1.0 mm in-plane, ~1.0-5.0 mm slice) [PLACEHOLDER — confirm]
3. **Dimension check**: Verify 3D volume (not 2D slice), typical ~30-1000 slices [PLACEHOLDER — confirm]
4. **Data type check**: Verify int16 or float32 [PLACEHOLDER — confirm]

### Handling Anomalies
- 20 Nov 2025: 3 cases with non-RAS orientation detected — auto-corrected via nibabel.as_closest_canonical(). [PLACEHOLDER — verify]
- 22 Nov 2025: 1 case with unusual high slice count (>1000) — handled by sliding window without issue. [PLACEHOLDER — verify]

---

## 4. No Resampling Decision

### Decision
No resampling applied — native voxel spacing preserved. [PLACEHOLDER — verify]

If no resampling:
- Original voxel spacing preserved
- Model trained on native resolution
- Avoids interpolation artifacts
- [PLACEHOLDER — verify]

---

## 5. No Intensity Augmentation

### Decision
No intensity augmentation applied. [PLACEHOLDER — verify]

### Rationale
CT intensities are physically meaningful (HU). Random intensity augmentation can distort the clinical meaning of voxel values. Spatial augmentation (flips, rotations) is preferred. [PLACEHOLDER — verify]

---

## Document History

| Date | Change | Author |
|------|--------|--------|
| 16 Nov 2025 | Initial document created | [PLACEHOLDER] |
| 05 Dec 2025 | Empirical evaluation table filled | [PLACEHOLDER] |
| 10 May 2026 | Reviewed for defense | [PLACEHOLDER] |

---

## Cross-References

- `experiment_log.md` — EXP-002: Preprocessing Refinement
- `model_training_documentation.md` — Training configuration
- `reproducibility_notes.md` — Exact preprocessing code path
