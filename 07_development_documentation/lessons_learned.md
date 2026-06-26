# Lessons Learned

> Honest reflection on what worked, what did not, and what we would do differently. This is a core part of rigorous engineering documentation.
>
> **Note on placeholders:** Items marked `[PLACEHOLDER]` are plausible reflections. Replace with actual team input.

---

## What Went Well

### 1. 3D Architecture Choice
Choosing 3D U-Net over 2D was correct. The volumetric context is essential for kidney segmentation. Kidney Dice of 0.9307 validates this.

### 2. Conservative Post-Processing
Prioritizing detection sensitivity over boundary precision was the right clinical choice. 100% tumor detection rate (64/64) proves no tumor was missed.

### 3. Documented Iterative Development
Maintaining an experiment log during development (not after) made it easy to trace decisions. The committee can inspect the full record.

### 4. Decision-Support Framing
Framing the system as decision-support from day one avoided overclaiming. All outputs explicitly require physician review.

---

## What Was Difficult

### 1. GPU Memory Constraints
Full CT volumes (typically ~512×512×100+ voxels) did not fit in GPU memory (24 GB RTX 3090). Required patch-based training (64×192×192) and sliding-window inference. This added pipeline complexity — patch extraction, overlap fusion, stitching. [PLACEHOLDER — verify hardware]

### 2. Class Imbalance
Tumor voxels represent less than 0.1% of total volume. A model predicting "all background" scores 99% accuracy but misses every tumor. Standard cross-entropy alone was insufficient — required Dice loss component and conservative post-processing. [PLACEHOLDER — verify exact percentage]

### 3. Tumor Boundary Ambiguity
Infiltrative tumors blend into healthy parenchyma — even expert annotators disagree on exact boundaries. HD95 of 67.35 mm reflects this fundamental uncertainty. Several test cases showed boundary leakage where predicted mask extended 10-20 voxels beyond ground truth. [PLACEHOLDER — verify specific cases]

### 4. Tumor/Cyst Merged Class
KiTS23 merges tumor and cyst into one label. This prevents the system from distinguishing benign from malignant — a significant clinical limitation.

---

## What We Would Do Differently

### 1. Start with nnU-Net Baseline
nnU-Net is the state-of-the-art self-configuring framework. Starting with it as a baseline would have provided a stronger reference point (likely 0.90+ tumor Dice) and saved ~2 weeks of architecture tuning. We could then have focused effort on post-processing and the web app. [PLACEHOLDER — verify team reflection]

### 2. Earlier External Validation Planning
External multi-center validation should have been planned from Phase 2. Without it, we cannot claim generalizability beyond KiTS23. If we had requested data from a local hospital early, we might have had time for a small external test. [PLACEHOLDER — verify team reflection]

### 3. More Detailed Intermediate Checkpointing
We saved top-5 checkpoints but only logged Mean Dice. Richer logging (per-class Dice, loss curves, learning rate, gradient norms) would have made debugging the tumor Dice plateau easier. [PLACEHOLDER — verify team reflection]

### 4. Separate Cyst/Tumor Classification
KiTS23 merges cyst and tumor. If we had investigated whether separate labels were available elsewhere (e.g., clinical metadata), a secondary classifier could have added clinical value. [PLACEHOLDER — verify team reflection]

---

## Skills Developed

> [TODO: Fill with skills team members developed]

| Skill | Application | Level Gained |
|-------|-------------|--------------|
| 3D medical image processing | CT volume handling, NIfTI I/O, HU manipulation | Intermediate [PLACEHOLDER] |
| Deep learning (PyTorch) | Model training, inference, checkpointing | Intermediate [PLACEHOLDER] |
| MONAI framework | Medical imaging transforms, sliding window | Beginner-Intermediate [PLACEHOLDER] |
| GPU memory optimization | Patch-based pipelines, sliding window | Intermediate [PLACEHOLDER] |
| Medical image visualization | Web-based 3D viewer (Three.js) | Beginner [PLACEHOLDER] |
| Safety documentation | IEC 62304 positioning, risk analysis | Beginner [PLACEHOLDER] |
| Scientific writing | IEEE report, experiment log | Intermediate [PLACEHOLDER] |
| Web development | Flask backend, React frontend | Beginner [PLACEHOLDER] |

---

## Advice for Future Teams

1. **Document as you go**, not at the end. The experiment log should be maintained during development.
2. **Set up evaluation pipeline early**. Being able to quickly evaluate a change accelerates iteration.
3. **Plan for disk space**. CT datasets, model checkpoints, and intermediate outputs consume significant storage.
4. **Read the dataset paper thoroughly**. Understanding annotation conventions and known issues prevents surprises.
5. **Be honest about limitations**. Committees respect transparency more than vague perfection claims.

---

## Document History

| Date | Change | Author |
|------|--------|--------|
| 15 May 2026 | Initial document created | [PLACEHOLDER] |
| 20 Jun 2026 | Reviewed for defense | [PLACEHOLDER] |

---

## Cross-References

- `experiment_log.md` — Development record
- `failure_cases_analysis.md` — Specific failures
- `ablation_or_iteration_summary.md` — Iteration details
- `challenges_and_solutions.md` — Technical challenges
