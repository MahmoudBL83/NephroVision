# Engineering Decisions

> Key engineering choices made during development, with alternatives considered and rationale. Addresses mid-year feedback about documenting the development process.

---

## 1. 3D U-Net vs 2D U-Net

### Decision
Use **3D convolutions** (3D U-Net) instead of 2D slice-by-slice processing.

### Alternatives Considered

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **2D U-Net** | Lower memory, faster training | Misses inter-slice context | Rejected |
| **2.5D U-Net** (3 adjacent slices) | Some context, moderate memory | Limited context window | Rejected |
| **3D U-Net** | Full volumetric context | Higher memory, slower | **Selected** |

### Rationale
- Kidney is a 3D organ — spatial relationships across slices are clinically meaningful
- Tumors can span multiple slices; 2D approaches miss this continuity
- 3D convolutions naturally handle anisotropic spacing

### Trade-off
- **Memory cost**: ~4-8x more GPU memory than 2D
- **Mitigation**: Patch-based training (64×192×192) and sliding-window inference

---

## 2. Sliding Window Inference vs Full-Volume

### Decision
Use **sliding window** with 50% overlap for inference.

### Alternatives Considered

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **Full-volume** | Single pass, no stitching | Exceeds GPU memory for most CTs | Rejected |
| **Sliding window** | Fits in memory, overlap fusion | Multiple passes, slower | **Selected** |
| **Tiled with no overlap** | Fastest | Stitching artifacts at boundaries | Rejected |

### Configuration
- Patch size: **64×192×192** voxels
- Overlap: **50%** in all dimensions
- Fusion: **Averaging** of overlapping predictions

---

## 3. Test-Time Augmentation (TTA): 8 Flips

### Decision
Apply **8-flip TTA** (all combinations of x, y, z axis flips) during final evaluation.

### Alternatives Considered

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **No TTA** | Fastest inference | More boundary noise | Used for dev |
| **4 flips** | Moderate cost, some benefit | Misses some orientations | Rejected |
| **8 flips** | Maximum orientation coverage | 8x inference time | **Selected for final eval** |
| **Rotation TTA** | More augmentation | Harder to invert, slower | Rejected |

### Rationale
- Flips are trivial to invert (just flip back)
- Averaging 8 predictions reduces orientation-dependent artifacts
- Cost acceptable for final evaluation (not real-time)

---

## 4. Conservative Post-Processing

### Decision
Use **size-based blob filtering** with deliberately conservative thresholds.

### Thresholds
- Kidney: remove connected components < **5000 voxels**
- Tumor: remove connected components < **100 voxels**

### Design Philosophy
> In decision-support, **false negatives are worse than false positives**.

- False positive → physician sees it, reviews it, dismisses it
- False negative → physician never sees it, cannot review it

### Alternatives Considered

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **Aggressive filtering** | Cleaner masks | Risk of removing small tumors | Rejected |
| **Conservative filtering** | Preserves detection | Some false positives remain | **Selected** |
| **No filtering** | Maximum sensitivity | Many false positives | Rejected |

---

## 5. Web Application Architecture

### Decision
Browser-based 3D visualization with **server-side inference**.

### Rationale
- No specialized software (3D Slicer) required by user
- Centralized model deployment — no client-side GPU needed
- Standard web technologies (HTML, WebGL) for cross-platform access

### Technology Stack
> [TODO: Fill with actual stack]

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Flask [PLACEHOLDER] | Python REST API for inference |
| Frontend | React [PLACEHOLDER] | Single-page application |
| Visualization | Three.js [PLACEHOLDER] | WebGL 3D mesh rendering |

---

## 6. Loss Function Selection

### Decision
DiceCE loss (Dice + Cross-entropy, equal weights). [PLACEHOLDER — verify]

### Alternatives Considered

| Loss | Pros | Cons | Verdict |
|------|------|------|---------|
| **Cross-entropy** | Simple, well-understood | Ignores class imbalance | Rejected |
| **Dice loss** | Focuses on foreground overlap | Can be unstable with small objects | Considered |
| **Dice + CE** | Balances overlap and classification | More hyperparameters | **Selected** [PLACEHOLDER] |
| **Focal loss** | Handles extreme imbalance | Hard to tune | Rejected |

### Rationale
DiceCE combines region overlap (Dice) with per-voxel classification (CE). Dice term forces foreground overlap despite extreme class imbalance. CE term stabilizes gradients for small objects. [PLACEHOLDER — verify]

---

## Document History

| Date | Change | Author |
|------|--------|--------|
| 06 Dec 2025 | Initial document created | [PLACEHOLDER] |
| 10 May 2026 | Reviewed for defense | [PLACEHOLDER] |

---

## Cross-References

- `experiment_log.md` — Training experiments
- `model_training_documentation.md` — Full training configuration
- `preprocessing_decisions.md` — Preprocessing choices
