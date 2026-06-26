# Reproducibility Notes

> Everything needed for another engineer to replicate our results. Addresses mid-year feedback and is a core scientific requirement.

---

## Reproducibility Checklist

- [x] Code available
- [x] Experiment log maintained
- [ ] Trained model weights archived
- [ ] Environment specification complete
- [ ] Dataset documentation complete
- [ ] Random seeds documented
- [ ] Preprocessing pipeline scripted
- [ ] Inference pipeline scripted
- [ ] Evaluation script automated

> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible values generated to show structure. Replace with actual team data before final submission.

---

## 1. Code Location

Main repository: `[PLACEHOLDER — add repo URL or local path]`

Key scripts:
- Training: `train.py` [PLACEHOLDER]
- Inference: `inference.py` [PLACEHOLDER]
- Evaluation: `evaluate.py` [PLACEHOLDER]
- Preprocessing: `preprocess.py` [PLACEHOLDER]

---

## 2. Environment Specification

### Hardware
> [TODO: Fill with actual hardware used]

| Component | Specification |
|-----------|--------------|
| GPU | NVIDIA RTX 3090 [PLACEHOLDER] |
| GPU Memory | 24 GB [PLACEHOLDER] |
| CPU | [PLACEHOLDER — verify model] |
| RAM | 32 GB [PLACEHOLDER] |
| Storage | 1 TB NVMe SSD [PLACEHOLDER] |

### Software

| Package | Version | Notes |
|---------|---------|-------|
| Python | 3.10 [PLACEHOLDER] | |
| PyTorch | 2.1.0 [PLACEHOLDER] | |
| MONAI | 1.3.0 [PLACEHOLDER] | Medical imaging toolkit |
| CUDA | 12.1 [PLACEHOLDER] | |
| cuDNN | 8.9 [PLACEHOLDER] | |
| NumPy | 1.24 [PLACEHOLDER] | |
| NiBabel | 5.1 [PLACEHOLDER] | NIfTI I/O |
| SciPy | 1.11 [PLACEHOLDER] | Connected-component analysis |
| TensorBoard | 2.15 [PLACEHOLDER] | Training logging |

Generate full environment:
```bash
pip freeze > requirements.txt
```

> [TODO: Attach actual requirements.txt or environment.yml]

---

## 3. Dataset

### Source
KiTS23 Challenge (2023)
- URL: https://kits-challenge.org/kits23/
- License: [TODO]

### Splits
> [TODO: Define exact case IDs for train / val / test splits]

| Split | Cases | Case IDs |
|-------|-------|----------|
| Training | 361 [PLACEHOLDER] | [PLACEHOLDER — list case IDs or reference file] |
| Validation | 64 [PLACEHOLDER] | [PLACEHOLDER — list case IDs or reference file] |
| Test (held-out) | 64 | [PLACEHOLDER — list case IDs or reference file] |

### Preprocessing
Identical for all splits:
1. HU clip to [-200, 300]
2. Normalize: `(x + 200) / 500`
3. No resampling — native voxel spacing preserved [PLACEHOLDER — verify]

---

## 4. Random Seeds

> [TODO: Document all random seeds used]

| Seed | Purpose |
|------|---------|
| 42 | PyTorch training [PLACEHOLDER] |
| 42 | NumPy operations [PLACEHOLDER] |
| 42 | Data shuffling [PLACEHOLDER] |
| 42 | Python random [PLACEHOLDER] |

Set seeds:
```python
import torch
import numpy as np
import random

SEED = 42  # [PLACEHOLDER — verify]

torch.manual_seed(SEED)
np.random.seed(SEED)
random.seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.benchmark = False  # [PLACEHOLDER — verify]
torch.backends.cudnn.deterministic = True  # [PLACEHOLDER — verify]
```

---

## 5. Training Reproduction

### Command
> [TODO: Provide exact training command]

```bash
python train.py \
  --data_dir /data/kits23/ \
  --output_dir /outputs/nephrovision/ \
  --epochs 300 \
  --batch_size 2 \
  --lr 2e-4 \
  --seed 42 \
  --patch_size 64 192 192 \
  --loss dicece \
  --optimizer adamw \
  --scheduler cosine \
  --warmup_epochs 5
```
> [PLACEHOLDER — verify exact command and arguments]

### Expected Output
- Checkpoint files: `best_val_dice.pth`, `last.pth` [PLACEHOLDER]
- Training log: `training_log.txt` + TensorBoard logs [PLACEHOLDER]
- Validation metrics: `val_metrics.json` [PLACEHOLDER]

### Expected Training Time
~48 hours total (300 epochs on RTX 3090) [PLACEHOLDER — verify]

---

## 6. Inference Reproduction

### Command
> [TODO: Provide exact inference command]

```bash
python inference.py \
  --input /data/kits23/test/case_XXXX.nii.gz \
  --checkpoint /outputs/nephrovision/best_val_dice.pth \
  --output /outputs/predictions/case_XXXX/ \
  --tta \
  --overlap 0.5 \
  --patch_size 64 192 192
```
> [PLACEHOLDER — verify exact command and arguments]

### Expected Output
- Segmentation masks (NIfTI format): `prediction.nii.gz`
- Volumetric statistics: `stats.json` (kidney volume, tumor volume, voxel counts)
- [PLACEHOLDER — verify any additional outputs]

### Expected Inference Time
~120 seconds per case (with 8-flip TTA on RTX 3090) [PLACEHOLDER — verify]
~15 seconds per case (no TTA) [PLACEHOLDER — verify]

---

## 7. Evaluation Reproduction

### Command
> [TODO: Provide exact evaluation command]

```bash
python evaluate.py \
  --pred_dir /outputs/predictions/ \
  --gt_dir /data/kits23/test/ \
  --output /outputs/metrics.json \
  --metrics dice hd95 detection
```
> [PLACEHOLDER — verify exact command and arguments]

### Expected Metrics
See `KNOWN_METRICS.md` for verified values.

---

## 8. Known Variability Sources

Even with fixed seeds, some variability is expected:

| Source | Impact | Mitigation |
|--------|--------|------------|
| GPU non-determinism | Small | cuDNN deterministic mode enabled |
| CUDA version | Small | Pin CUDA 12.1 [PLACEHOLDER] |
| PyTorch version | Moderate | Pin PyTorch 2.1.0 [PLACEHOLDER] |
| Patch sampling order | Small | Fixed seed + deterministic sampler [PLACEHOLDER] |

---

## 9. Model Weights

> [TODO: Document where trained weights are archived]

| Checkpoint | File | Size | Notes |
|------------|------|------|-------|
| Final (best val) | best_val_dice.pth [PLACEHOLDER] | ~35 MB [PLACEHOLDER] | Used for test evaluation |
| Last epoch | last.pth [PLACEHOLDER] | ~35 MB [PLACEHOLDER] | Final epoch checkpoint |

---

## Document History

| Date | Change | Author |
|------|--------|--------|
| [TODO] | Initial document created | [TODO] |

---

## Cross-References

- `experiment_log.md` — Full experiment records
- `model_training_documentation.md` — Training configuration
- `preprocessing_decisions.md` — Preprocessing specification
