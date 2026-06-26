# Development Journey Slides — Detailed Content

## NephroVision Final Defense Presentation

This document provides detailed content for the 5 emphasis slides that address mid-year feedback about documenting the team's engineering process. Each slide follows the structure: what the team did, why the decision was made, what difficulties appeared, how the team mitigated them, and what remains future work.

**Design constraint:** Maximum 4 bullets per slide. Visual-first approach.

---

## Slide 1: Development Journey

**Slide title:** Development Journey

**Main message:** The project followed an iterative engineering process with documented experiments at every stage — not just final result reporting.

**Bullets (max 4):**

1. **What we did and why:** Progressed through 10 phases — problem definition, KiTS23 exploration, preprocessing design, 3D U-Net implementation, training iterations, inference development, post-processing, web visualization, IEC 62304 safety documentation, and final validation. Each phase involved experiments that informed the next decision.
2. **Difficulties faced:** GPU memory constraints during 3D volumetric training, severe class imbalance between background and tumor/cyst voxels, and high variability in tumor size and appearance across cases.
3. **Mitigations applied:** Patch-based training and sliding-window inference for memory efficiency, specialized loss functions for class imbalance, and test-time augmentation to reduce boundary noise.
4. **Future work:** Conduct systematic hyperparameter search, evaluate nnU-Net self-configuring framework, and perform external multi-center validation.

**Visual direction:**

- Horizontal timeline graphic showing the 10 development phases as connected milestones.
- Use icons for each phase (magnifying glass for exploration, gear for preprocessing, neural network icon for model, etc.).
- Highlight phases where major difficulties were encountered with a warning color.
- Keep the timeline as the primary visual; bullets appear below or via v-click.
- Color scheme: phases in blue, difficulties in amber, mitigations in green.

**Speaker notes:**

"This slide directly addresses the feedback about documenting our engineering process. We did not jump straight to the final model — we went through ten distinct phases, each with its own experiments and decisions. The timeline shows the full journey. I want to highlight three major difficulties we faced: GPU memory limitations, which we solved with patch-based training; class imbalance, which we addressed with specialized loss functions; and tumor variability, which we mitigated with test-time augmentation. These were real engineering challenges, not theoretical ones. For future work, we plan a systematic hyperparameter search and evaluation of nnU-Net. The key message is that this was an iterative process, and we documented every step."

---

## Slide 2: Preprocessing Decisions

**Slide title:** Preprocessing Decisions

**Main message:** The preprocessing pipeline was designed through empirical evaluation to standardize CT volumes while preserving diagnostic information for kidney and tumor segmentation.

**Bullets (max 4):**

1. **What we did and why:** Implemented NIfTI loading and validation, HU clipping to [-200, 300] to preserve soft-tissue contrast while suppressing bone and air, and normalization to [0, 1] for consistent neural network input. The clipping range was selected empirically by testing multiple ranges.
2. **Difficulties faced:** Variable voxel spacing and orientation across KiTS23 cases, and extreme volume dimensions that required special handling.
3. **Mitigations applied:** Standardized orientation validation pipeline, and cropping and padding strategies for extreme volumes. Preprocessing applied identically to training and inference for consistency.
4. **Future work:** Evaluate adaptive per-volume clipping based on individual intensity statistics rather than a fixed range.

**Visual direction:**

- Before/after comparison: raw CT slice (wide HU range) on the left, preprocessed slice (clipped and normalized) on the right.
- Show an intensity histogram with the [-200, 300] window highlighted.
- Use a simple flow diagram: NIfTI Load -> HU Clip [-200, 300] -> Normalize [0, 1] -> Model Input.
- Keep text minimal; the before/after visual carries the message.
- Annotate the histogram to show what is preserved (kidney, tumor) and what is suppressed (bone, air).

**Speaker notes:**

"Preprocessing is where engineering decisions directly affect model performance. We chose HU clipping at [-200, 300] after testing multiple ranges. This range captures kidney parenchyma and tumor tissue while suppressing bone, air, and irrelevant structures. Normalization to [0, 1] ensures consistent input regardless of scanner-specific intensity variations. We faced two main difficulties: variable voxel spacing across cases and extreme volume dimensions. We mitigated these with a standardized validation pipeline and cropping and padding strategies. Critically, we applied the exact same preprocessing to training and inference — any inconsistency here would degrade performance. For future work, we want to explore adaptive clipping that adjusts per volume rather than using a fixed range."

---

## Slide 3: Model Training Documentation

**Slide title:** Model Training Documentation

**Main message:** The 3D U-Net was trained through multiple documented iterations, with every experiment logged for reproducibility and defense transparency.

**Bullets (max 4):**

1. **What we did and why:** Implemented a 3D U-Net for volumetric semantic segmentation — 3D convolutions capture spatial context across slices that 2D approaches miss. Trained on the KiTS23 training partition with validation monitoring. All experiments were logged with hyperparameters, metrics, and decisions.
2. **Difficulties faced:** GPU memory constraints during 3D volumetric training, severe class imbalance between background and tumor/cyst voxels, and training convergence instability.
3. **Mitigations applied:** Patch-based training strategy for memory efficiency, specialized loss function for class imbalance (exact choice documented in experiment log), and learning rate scheduling with early stopping for convergence.
4. **Future work:** Complete full hyperparameter documentation in the experiment log, and evaluate the nnU-Net self-configuring framework as a baseline comparison.

**Visual direction:**

- Central graphic: 3D U-Net architecture diagram showing encoder-decoder structure with skip connections.
- Side panel: small table or icon row showing the experiment log structure (ID, Date, Setup, Result, Decision).
- Use a "document" icon to emphasize that training was logged, not just run.
- Avoid listing specific hyperparameters on the slide — state they are documented in the experiment log.
- Color: architecture in blue, documentation emphasis in a distinct accent color.

**Speaker notes:**

"We selected 3D U-Net because volumetric context is essential for kidney and tumor segmentation — a 2D slice-by-slice approach misses the spatial relationships across slices. The encoder-decoder structure with skip connections captures both context and fine details. We ran multiple training iterations, and every single one was logged in our experiment log with the hyperparameters used, the metrics achieved, and the decision made afterward. This is important: we are not just presenting the final model — we are presenting the process that got us here. Our main difficulties were GPU memory, class imbalance, and convergence. We solved these with patch-based training, a specialized loss function, and learning rate scheduling. The exact optimizer settings and hyperparameters are documented in our experiment log — we did not want to overload the slide with numbers. For future work, we plan to evaluate nnU-Net as a self-configuring baseline."

---

## Slide 4: Key Challenge: Tumor/Cyst Segmentation

**Slide title:** Key Challenge: Tumor/Cyst Segmentation

**Main message:** Tumor detection and tumor boundary segmentation are different tasks — the system achieves 100% detection but moderate boundary precision, reflecting the inherent difficulty of the task.

**Bullets (max 4):**

1. **Why this is harder than kidney:** Tumors are small, variable in shape, and boundary-ambiguous. Dice is hypersensitive to boundary errors on small objects — a 1-voxel shift on a 100-voxel lesion reduces Dice from 1.0 to approximately 0.70. Cysts and tumors look similar under the merged KiTS23 class.
2. **Detection vs. boundary precision:** Tumor Detection Rate is 100% (64/64) — the model finds every tumor. Tumor Dice is 0.6558, reflecting boundary uncertainty, not detection failure. Kidney Dice is 0.9307 because the kidney is large and anatomically consistent.
3. **Mitigations applied:** Conservative post-processing (100-voxel threshold preserves small lesions), 8-flip test-time augmentation reduces boundary noise, and sliding-window overlap fusion smooths predictions.
4. **Future work:** Boundary-aware loss functions (Boundary loss, Hausdorff loss), separate cyst vs. tumor classification stage, and size-stratified performance analysis.

**Visual direction:**

- Split layout: left side shows kidney segmentation (large, clean boundaries, Dice 0.9307); right side shows tumor segmentation (small, ambiguous boundaries, Dice 0.6558).
- Include a small bar chart comparing Kidney Dice vs. Tumor Dice vs. Detection Rate.
- Use a visual analogy: "Finding the tumor is easy; drawing its exact border is hard."
- Highlight the 100% detection rate as a positive, with Dice contextualized as a boundary precision metric.
- Color: kidney in blue, tumor in orange/red, detection rate in green.

**Speaker notes:**

"This is the most important technical slide. I want to be very clear about the distinction between detection and boundary segmentation. Our system detects 100% of tumors — all 64 out of 64 test cases. That means the model finds every tumor. However, the exact boundary of each tumor is less precise, and that is what the Dice score of 0.6558 reflects. This is not a failure — it is the nature of the task. Tumors are small, variable, and their boundaries are often ambiguous even to human experts. A 1-voxel boundary error on a small tumor can reduce Dice dramatically. We mitigate this with conservative post-processing that preserves small lesions, test-time augmentation that reduces boundary noise, and overlap fusion that smooths predictions. For future work, we propose boundary-aware loss functions and a separate cyst versus tumor classification stage. The key message: reliable detection with moderate boundary precision is clinically useful as decision-support, but all outputs require physician review."

---

## Slide 5: Failure Analysis and Limitations

**Slide title:** Failure Analysis and Limitations

**Main message:** The team conducted honest failure analysis and established risk mitigation strategies. The system is decision-support only — it is not clinically approved and does not replace physician judgment.

**Bullets (max 4):**

1. **What we did:** Analyzed failure modes across test set predictions, documented boundary leakage and under-segmentation cases, quantified boundary uncertainty through HD95 (67.35 mm for tumor), and established risk mitigation strategies.
2. **Key failure modes:** Tumor boundary leakage into healthy parenchyma, small lesion sensitivity to minor boundary errors, cyst/tumor confusion due to merged class, and domain shift risk on non-KiTS23 data.
3. **Mitigations and scoping:** TTA and post-processing reduce but do not eliminate errors. System is explicitly scoped as KiTS23-only evaluation. All outputs require physician review. System is not FDA approved and not clinically validated.
4. **Future work:** External multi-center validation, uncertainty estimation for low-confidence regions, and per-lesion size-stratified analysis.

**Visual direction:**

- Use a 2x2 grid showing the four failure modes with small icon illustrations (boundary leakage, small lesion, cyst/tumor confusion, domain shift).
- Include a disclaimer banner at the bottom: "Decision-Support Only | Not Clinically Approved | Physician Review Required."
- Use a risk severity color coding: red for high risk (domain shift, missed lesions), amber for medium (boundary leakage, cyst/tumor confusion).
- Keep the visual honest — do not minimize failures. Transparency builds credibility.
- Include a small "shield" icon next to mitigations to convey risk reduction.

**Speaker notes:**

"A defense that only shows successful cases is incomplete. We conducted a systematic failure analysis across our test set predictions. We identified four main failure modes: tumor boundary leakage into healthy parenchyma, sensitivity to small lesion boundaries, cyst and tumor confusion due to the merged KiTS23 class, and domain shift risk if the system is used on non-KiTS23 data. Our mitigations include test-time augmentation, conservative post-processing, and explicit scoping as KiTS23-only evaluation. But I want to be clear: these mitigations reduce errors, they do not eliminate them. That is why this system is decision-support only. It is not clinically approved. It is not FDA approved. It does not replace radiologists. Every output requires physician review. For future work, external multi-center validation is our highest priority, along with uncertainty estimation to flag low-confidence regions. Presenting failure analysis honestly is not a weakness — it is scientific maturity and a patient safety requirement."

---

## Summary: Emphasis Slide Consistency Check

| Element | Slide 1 | Slide 2 | Slide 3 | Slide 4 | Slide 5 |
|---------|---------|---------|---------|---------|---------|
| What the team did | Yes | Yes | Yes | Yes (implied) | Yes |
| Why the decision was made | Yes | Yes | Yes | Yes | — |
| Difficulties faced | Yes | Yes | Yes | Yes | Yes |
| How the team mitigated | Yes | Yes | Yes | Yes | Yes |
| Future work | Yes | Yes | Yes | Yes | Yes |
| Max 4 bullets | 4 | 4 | 4 | 4 | 4 |
| Visual direction | Timeline | Before/after | Architecture | Split comparison | 2x2 grid |
| Decision-support framing | — | — | — | Yes | Yes |
| No invented hyperparameters | Yes | Yes | Yes | Yes | Yes |

---

## Cross-Reference Checklist

All content in this document must remain consistent with:

- `MASTER_CONTEXT.md` — project facts and metrics
- `KNOWN_METRICS.md` — validated numbers (Kidney Dice 0.9307, Tumor Dice 0.6558, Detection 100%)
- `DO_NOT_OVERCLAIM.md` — safe wording rules
- `experiment_log.md` — experiment documentation
- `model_training_documentation.md` — training setup details
- `challenges_and_solutions.md` — challenge analysis
- `cyst_and_tumor_detection_challenges.md` — tumor segmentation difficulty
- `failure_cases_analysis.md` — failure mode documentation
