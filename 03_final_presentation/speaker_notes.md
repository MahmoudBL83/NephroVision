# Speaker Notes

## Slide 1: Title
Welcome the committee. Introduce NephroVision as a decision-support prototype for automated kidney and renal tumor segmentation. Mention the team and supervisor. Emphasize immediately that this is an academic prototype, not a clinically approved device.

## Slide 2: Clinical Problem
Set the clinical context. Radiologists spend significant time on manual segmentation. This is tedious, variable, and delays workflow. Do not claim radiologists are incompetent — frame this as a workload and consistency challenge.

## Slide 3: Why Segmentation Matters
Connect the technical work to patient care. Mention surgical planning, treatment monitoring, and longitudinal follow-up. The key message: accurate volumetric assessment saves kidneys and lives.

## Slide 4: Project Objective
State the scope clearly. Input: CT volumes. Output: masks + statistics + visualization. Users: medical professionals. Scope: decision-support only. Repeat: physician review is required.

## Slide 5: Dataset: KiTS23
Describe KiTS23 briefly. Three classes. 64 held-out test cases. Mention the tumor/cyst merged class — this is important context for later slides. The dataset variability is why tumor segmentation is hard.

## Slide 6: Development Journey (EMPHASIS SLIDE)

One of the main improvements after the mid-year discussion was documenting our development process more systematically. Before that feedback, we had been focused on getting the model to work. After it, we made sure to record every decision, every experiment, and every difficulty along the way.

What I want the committee to take from this slide is that we did not only report the final model; we also documented the pipeline decisions, training setup, inference choices, and known limitations. The timeline you see here represents ten distinct phases, from understanding the clinical problem all the way to safety documentation and final validation.

At each phase, we ran experiments and recorded what worked and what did not. We faced three major difficulties. First, GPU memory constraints — full 3D volumes are too large to process at once, so we moved to patch-based training and sliding-window inference. Second, class imbalance — tumor voxels are a tiny fraction of the volume, which biases the model toward background. We addressed this with specialized loss functions and conservative post-processing. Third, tumor variability — tumors differ widely in size, shape, and appearance, which we mitigated with test-time augmentation and overlap fusion.

I want to be honest: we did not solve every problem. A systematic hyperparameter search is still future work, and we plan to evaluate nnU-Net as a self-configuring baseline. But the key message is that this was an iterative engineering process, and we have the documentation to prove it.

## Slide 7: What We Built
Show the pipeline visually. Walk through each stage: preprocessing -> model -> inference -> post-processing -> output. Keep it high-level. The goal is to give the committee a mental model of the system.

## Slide 8: Preprocessing Decisions (EMPHASIS SLIDE)

Preprocessing is where engineering decisions directly affect model performance, and we want to show the committee that these choices were deliberate, not arbitrary.

We implemented NIfTI loading and validation, then applied HU clipping to the range of minus two hundred to three hundred. We chose this range empirically — we tested multiple clipping windows, and this one captured kidney parenchyma and tumor tissue clearly while suppressing bone, air, and other irrelevant structures. After clipping, we normalized intensities to the zero-to-one range so that the network received consistent input regardless of scanner-specific intensity variations.

The difficulties we faced here were practical. Different KiTS23 cases had different voxel spacing and orientation, which could distort anatomical structures if not handled. We mitigated this with a standardized orientation validation pipeline. We also encountered extreme volume dimensions that required cropping and padding strategies to make processing feasible.

A critical point: we applied the exact same preprocessing to training and inference. Any inconsistency between the two would degrade performance silently, and that is a mistake we made sure to avoid.

For future work, we want to explore adaptive clipping that adjusts based on each volume's own intensity statistics rather than using a fixed range. But the current pipeline is reproducible and well-documented, which was a direct response to the mid-year feedback.

## Slide 9: Model Training Documentation (EMPHASIS SLIDE)

This slide is about transparency. We did not only report the final model; we also documented the pipeline decisions, training setup, inference choices, and known limitations. That documentation is what I want to highlight here.

We selected a 3D U-Net for volumetric semantic segmentation because 3D convolutions capture spatial context across slices — something that 2D slice-by-slice approaches simply cannot do. The encoder-decoder structure with skip connections gives us both context for detection and fine details for localization. The output is a three-class probability map: background, kidney, and tumor or cyst.

We ran multiple training iterations, and every single one was logged in our experiment log with the hyperparameters used, the metrics achieved, and the decision made afterward. I want to be transparent: the exact optimizer settings, learning rate schedule, and batch size are documented in the experiment log rather than on this slide, because we did not want to overload the presentation with numbers. That detail is available for the committee to review.

Our main difficulties during training were GPU memory constraints, severe class imbalance, and convergence instability. We mitigated these with patch-based training, a specialized loss function, and learning rate scheduling with early stopping.

For future work, we plan to complete the full hyperparameter documentation and evaluate the nnU-Net self-configuring framework as a baseline comparison. The important point is that our training process is documented and reproducible — that was a direct improvement after the mid-year discussion.

## Slide 10: 3D U-Net Architecture
Brief technical overview. Encoder-decoder with skip connections. Three-class output. Emphasize why 3D over 2D: volumetric context across slices.

## Slide 11: Inference Pipeline
Walk through the configuration: 64x192x192 patches, 50% overlap, 8-flip TTA, averaging fusion. Explain why each choice: memory constraints, boundary noise reduction, stitching artifact minimization.

## Slide 12: Post-processing
Explain the blob removal thresholds. Kidney < 5000 voxels removed. Tumor < 100 voxels removed. Emphasize the conservative tumor threshold: it preserves small true lesions at the cost of potentially retaining some noise. This is a safety-conscious choice.

## Slide 13: Key Challenge: Tumor/Cyst Segmentation (EMPHASIS SLIDE)

This is the most important technical slide, and I want to address it honestly and confidently.

Tumor and cyst segmentation was the most challenging part because these structures are smaller, more variable, and have less clear boundaries than the kidney. The kidney is a large organ with a consistent shape and relatively clear margins. Tumors can be as small as a few hundred voxels, they grow in irregular patterns, and their boundaries often blend into the surrounding parenchyma. On top of that, the KiTS23 dataset merges cysts and tumors into a single class, so the model has to handle two visually different entities under one label.

Here is the key distinction I want the committee to understand: tumor detection and tumor boundary segmentation are different tasks. Our tumor detection rate was 100%, meaning we found all 64 tumors in the 64 test cases. But boundary-level segmentation remains more challenging, as reflected by the tumor Dice score of 0.6558. That number does not mean we missed tumors — it means the exact borders we drew were less precise than the borders we drew for the kidney.

This makes sense when you consider how Dice works. On a small lesion, even a one-voxel boundary error can drop the Dice from near-perfect to around 0.70. The same error on a large organ like the kidney is negligible. So the gap between kidney Dice of 0.93 and tumor Dice of 0.66 reflects the difficulty of the task, not a fundamental failure of the model.

We mitigated this challenge with conservative post-processing that preserves small lesions, eight-flip test-time augmentation that reduces boundary noise, and overlap fusion that smooths predictions. We also report HD95, which is 67.35 millimeters for tumor, to give an honest picture of boundary uncertainty.

For future work, we propose boundary-aware loss functions, a separate cyst-versus-tumor classification stage, and size-stratified performance analysis. I want to be clear: we are not claiming this problem is solved. We are presenting it as an honest engineering result — reliable detection with moderate boundary precision — and that is why the system is decision-support only, with all outputs requiring physician review.

## Slide 14: Web Application
Show the interface. Upload, visualization, statistics. Mention that no specialized software is needed. If you have a demo, offer to show it. If not, describe the planned demo.

## Slide 15: Validation Setup
Describe the 64 held-out test cases. Emphasize independence: never seen during training or validation. Same preprocessing. Full-volume inference. Metrics: Dice, HD95, detection rate.

## Slide 16: Results
Present the metrics table. Read the numbers clearly. Kidney Dice 0.9307. Tumor Dice 0.6558. Detection 100%. HD95 values. After revealing the numbers, interpret them: kidney is robust, detection is reliable, tumor boundaries need work. This interpretation is honest and shows understanding.

## Slide 17: Target vs. Achieved
Compare goals to results. Kidney Dice exceeded target. Tumor detection met target. Tumor Dice is moderate — acknowledge this. Web visualization implemented. The interpretation: the system achieves its primary goals with known limitations.

## Slide 18: Failure Analysis and Limitations (EMPHASIS SLIDE)

A defense that only shows successful cases is incomplete, and the mid-year feedback pushed us to document our limitations just as thoroughly as our results. That is what this slide is about.

We conducted a systematic failure analysis across our test set predictions. We did not just look at the average metrics — we went case by case to understand where and why the system struggles. We identified four main failure modes.

First, tumor boundary leakage — the predicted tumor mask sometimes extends beyond the true lesion into healthy parenchyma. Our HD95 for tumor is 67.35 millimeters, which quantifies this boundary uncertainty honestly.

Second, small lesion sensitivity — even minor boundary errors on small tumors cause large drops in Dice, which is a mathematical property of the metric rather than a catastrophic model failure.

Third, cyst and tumor confusion — because KiTS23 merges these into one class, our system cannot distinguish a benign cyst from a potentially malignant tumor. We label the output as tumor or cyst to make this clear, but the limitation remains.

Fourth, domain shift — we evaluated only on KiTS23 data. Performance on other scanners, protocols, or patient populations is unknown, and we explicitly state this rather than assuming generalizability.

Our mitigations include test-time augmentation, conservative post-processing, and explicit scoping as KiTS23-only evaluation. But I want to be clear: these mitigations reduce errors, they do not eliminate them. That is why this system is decision-support only. It is not clinically approved. It is not FDA approved. It does not replace radiologists. Every output requires physician review, and all clinical decisions remain the responsibility of qualified healthcare professionals.

For future work, external multi-center validation is our highest priority, along with uncertainty estimation to flag low-confidence regions for the physician. Presenting failure analysis honestly is not a weakness — it is scientific maturity and a patient safety requirement. That is the standard we set for ourselves after the mid-year discussion.

## Slide 19: Safety and IEC 62304
State the regulatory framing clearly. Class B. Academic prototype. Not FDA approved. All outputs require physician review. Does not replace radiologists. This slide protects the team from overclaiming accusations.

## Slide 20: Future Work
Walk through the prioritized directions. High priority: boundary accuracy, external validation, nnU-Net. Medium: cyst/tumor classification, uncertainty estimation. Low: inference optimization. Show that the team has a clear roadmap.

## Slide 21: Final Takeaway
Summarize in four points: robust kidney segmentation, reliable tumor detection, moderate tumor boundaries, decision-support only. Thank the committee. Invite questions.

---

## General Delivery Tips

- Speak slowly and clearly. Pause after key metrics.
- Do not read bullets verbatim — paraphrase and add context.
- If an examiner asks about a TODO placeholder, be honest: "That detail is documented in our experiment log and will be completed before final submission."
- Never say "we tried everything" or "our model is the best." Use measured language.
- If asked about clinical validation, state clearly: "No prospective clinical trial was conducted. External validation is future work."
- If asked about tumor Dice, refer to Slide 13 talking points. Do not get defensive.
- Always return to the decision-support framing: the system assists, not replaces, the physician.
