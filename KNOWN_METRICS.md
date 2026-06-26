# Known Metrics

Verified, defensible numbers for NephroVision.

**These metrics must not be changed.**

---

## Dataset

- **Dataset:** KiTS23 (Kidney Tumor Segmentation Challenge 2023)
- **Classes:**
  - Background
  - Kidney
  - Tumor/Cyst
- **Test Set:** 64 independent held-out cases
- **Input Format:** NIfTI CT volumes (`.nii` / `.nii.gz`)

## Official KiTS23 Dataset vs Project Evaluation Split

- The official KiTS23 challenge reports an expanded training set of **489 cases** and an official fresh test set of **110 cases**.
- NephroVision's reported metrics are based on a **project-defined held-out evaluation subset of 64 independent cases**, not the official KiTS23 test set.
- **Do not mix** official KiTS23 challenge split numbers with NephroVision's internal/project split.
- NephroVision did not report official leaderboard performance unless explicitly documented.

## Preprocessing

- **HU Clipping Range:** [-200, 300]
- **Normalization Range:** [0, 1]

## Model and Inference

- **Architecture:** 3D U-Net
- **Task:** Volumetric semantic segmentation
- **Inference Patch Size:** 64×192×192
- **Sliding Window Overlap:** 50%
- **Test-Time Augmentation:** 8 flip combinations

## Post-Processing

- **Kidney Minimum Blob Size:** 5000 voxels
- **Tumor Minimum Blob Size:** 100 voxels

## Validation Metrics

| Metric | Kidney | Tumor |
|--------|--------|-------|
| **Dice Score** | 0.9307 ± 0.064 | 0.6558 ± 0.262 |
| **HD95 (mm)** | 19.98 | 67.35 |

- **Mean Dice:** 0.7933
- **Tumor Detection Rate:** 64/64 = 100%

## Acceptance Criteria

- Tumor detection rate: 100% on the 64-case held-out test set.
- Kidney Dice ≥ 0.90.
- Tumor Dice reflects known challenge difficulty and is reported with uncertainty.
- System processes a full CT volume end-to-end through the web interface.

## Metrics That Must Never Be Changed

- Kidney Dice: **0.9307 ± 0.064**
- Tumor Dice: **0.6558 ± 0.262**
- Mean Dice: **0.7933**
- Tumor Detection Rate: **100% (64/64)**
- HD95 Kidney: **19.98 mm**
- HD95 Tumor: **67.35 mm**
- Test Set Size: **64 independent held-out cases**

## Notes

- All values come from the NephroVision project-defined **64-case held-out test subset**, not the official KiTS23 challenge test set.
- Report uncertainties where available.
- Do not generalize these metrics beyond the KiTS23 population and acquisition protocols.
- Always distinguish official KiTS23 challenge information from NephroVision's project-specific evaluation setup.
