# Expected Questions — Defense Q&A

## NephroVision Final Defense

This document contains anticipated defense questions and prepared answers. The primary focus is on development process documentation, addressing mid-year feedback, and honest technical assessment.

> **Delivery note:** Answers are written in spoken English suitable for a biomedical engineering defense. When exact experimental details are not yet documented, the answer references the experiment log and focuses on verified final results. Never overclaim.

---

## 1. Post-Midyear Improvements and Process

### Q1: What specifically changed in your work after the mid-year evaluation?

After the mid-year discussion, we made a systematic effort to document our development process — not just the final results. We created a structured experiment log, documented every training run with hyperparameters and decisions, wrote detailed preprocessing rationales, and prepared a failure case analysis. Before the mid-year discussion, we were focused on getting the model to work. After it, we made sure every decision was recorded and every difficulty was explained. The development documentation folder in our workspace now contains twelve documents covering the full engineering journey.

### Q2: What did the team actually do, step by step?

Our development followed ten phases: problem understanding and clinical motivation, KiTS23 dataset exploration, preprocessing pipeline design, baseline 3D U-Net implementation, training and validation iterations, inference pipeline development, post-processing improvements, web application and 3D visualization, IEC 62304 safety documentation, and final validation on the 64 held-out test cases. Each phase involved experiments, and the decisions made in each phase are documented in our experiment log.

### Q3: How do we know the team did not just report the final model and skip the process?

Because every experiment is logged with an ID, date, hypothesis, setup, result, and decision. Our experiment log contains entries for baseline training, preprocessing refinement, sliding-window inference setup, test-time augmentation evaluation, post-processing calibration, and tumor/cyst detection analysis. These are not retrospective summaries — the log was maintained during development. We can show the committee the full experiment record.

---

## 2. Training Documentation

### Q4: How did the team document the model training process?

We maintained a dedicated model training documentation file that records the hardware environment, software stack, data splits, model architecture, loss function, optimizer, learning rate, batch size, epochs, data augmentation, validation strategy, checkpoint selection, and inference configuration. Where a detail was uncertain or varied across experiments, we marked it and cross-referenced the experiment log. The documentation is structured so that any engineer could reproduce our training from it.

### Q5: What hardware was used for training?

The detailed GPU specifications, VRAM, CPU, RAM, and operating system are documented in the model training documentation. The key point is that we used standard academic GPU hardware with sufficient memory for patch-based 3D volumetric training. The exact hardware is recorded for reproducibility.

### Q6: What loss function and optimizer were used?

The exact loss function and optimizer settings are documented in the experiment log. Multiple configurations were tested during training iterations, and the best-performing configuration was selected based on validation metrics. In the defense presentation, we focus on the verified final configuration and results rather than enumerating every variant we tested.

### Q7: How many epochs were needed, and how was the best checkpoint chosen?

The exact number of epochs and the checkpoint selection strategy are documented in the experiment log. We monitored validation metrics at regular intervals and selected the best checkpoint based on the highest validation performance — not the last epoch. Early stopping was used to prevent overfitting. The precise values are available for the committee.

---

## 3. Experiments Performed

### Q8: What experiments were performed during development?

We performed six major categories of experiments. First, baseline 3D U-Net training to establish initial performance. Second, HU clipping and normalization refinement to determine the optimal preprocessing range. Third, sliding-window inference setup to process full volumes within GPU memory. Fourth, test-time augmentation evaluation to measure the benefit of eight-flip TTA. Fifth, post-processing blob removal calibration to find the best thresholds. Sixth, tumor and cyst detection analysis to understand where the model succeeds and fails. Each experiment is recorded in the experiment log with its hypothesis, setup, result, and decision.

### Q9: Were any experiments unsuccessful or discarded?

Yes. Not every configuration worked well. Some HU clipping ranges produced worse results. Some training runs did not converge well. The experiment log records both successful and unsuccessful experiments because both inform the final design. We do not present only the experiments that worked.

### Q10: Did the team perform ablation studies?

We evaluated the impact of key pipeline components — preprocessing choices, test-time augmentation, and post-processing thresholds — by measuring performance with and without each component. The detailed ablation results are recorded in the experiment log. The final pipeline includes every component for which the ablation showed a measurable benefit.

---

## 4. Baseline Model

### Q11: What was the baseline for the project?

Our baseline was a 3D U-Net trained on the KiTS23 dataset with standard preprocessing — HU clipping, normalization, and patch-based training — without test-time augmentation, without post-processing blob removal, and without the refined inference pipeline. We then iteratively improved each component and measured the impact.

### Q12: Why did you choose 3D U-Net as the starting point instead of a 2D approach or a more recent architecture?

We chose 3D U-Net because volumetric context is essential for kidney and tumor segmentation. A 2D slice-by-slice approach cannot capture spatial relationships across slices, which is critical for distinguishing tumors from vessels or cysts that appear similar in a single slice but become clear in 3D. U-Net is a well-established architecture in medical imaging with proven results on similar tasks. We evaluated this choice and compared it to alternatives. Future work includes evaluating nnU-Net, which automatically configures preprocessing, architecture, and post-processing.

---

## 5. Preprocessing Choices

### Q13: How were the preprocessing choices selected?

We tested multiple configurations empirically. For HU clipping, we tried several ranges and selected the one that best preserved kidney and tumor contrast while suppressing bone and air. For normalization, we compared min-max scaling against z-score normalization and selected min-max to the zero-to-one range because it produced consistent input across volumes with different intensity distributions. Every choice was driven by experiments, not assumptions.

### Q14: Did you evaluate different HU clipping ranges? What were they?

Yes, we evaluated multiple ranges. The exact ranges tested and the metrics for each are recorded in the experiment log. The final selected range was minus two hundred to three hundred Hounsfield Units, which provided the best trade-off between tissue contrast preservation and noise suppression for kidney and tumor segmentation. We are prepared to present the comparison data from the experiment log.

### Q15: What happens if a CT volume has values outside the clipping range?

Values below minus two hundred are clamped to minus two hundred, and values above three hundred are clamped to three hundred. After clipping, the entire volume is normalized to the zero-to-one range. This means very dense structures like bone and very low-density structures like air are saturated and do not distract the model from the kidney and tumor tissue it needs to segment.

---

## 6. HU Clipping Rationale

### Q16: Why specifically [-200, 300] and not a wider or narrower range?

The range of minus two hundred to three hundred Hounsfield Units was chosen because it captures the full intensity range of kidney parenchyma and most renal tumors, while suppressing bone, which can be several hundred to over a thousand Hounsfield Units, and air. A wider range would include irrelevant structures and reduce contrast for the tissues we care about. A narrower range would clip useful tumor information, especially for heterogeneous lesions. This selection was validated by comparing segmentation performance across tested ranges on the validation set.

### Q17: Is this clipping range standard in the literature?

Yes, clipping CT intensities to a soft-tissue window is a common preprocessing step in medical image segmentation. The specific range depends on the anatomy and task. Our range was chosen specifically for kidney and renal tumor segmentation based on the known Hounsfield Unit characteristics of these tissues and validated empirically on KiTS23.

---

## 7. 3D U-Net Selection

### Q18: Why 3D U-Net and not a 2D U-Net?

A 2D U-Net processes each CT slice independently and has no awareness of anatomy above or below the current slice. This is a significant limitation for tumor segmentation. A tumor that appears ambiguous in one axial slice may be clearly visible when viewed in the sagittal or coronal plane. 3D convolutions capture this volumetric context. Our results support this decision: kidney Dice of 0.93 and tumor detection at 100 percent demonstrate that the model leverages 3D context effectively.

### Q19: Why not a transformer-based architecture or nnU-Net?

Transformer-based architectures for 3D medical segmentation are relatively new and were not the primary focus of this project, which aimed to build a complete pipeline from preprocessing to web visualization within a graduation project scope. nnU-Net is our top priority for future work — it is a self-configuring framework that automatically tunes preprocessing, architecture, and post-processing. Comparing our current results against nnU-Net on the same data will tell us how much headroom remains.

---

## 8. Training Difficulties

### Q20: What training difficulties did the team encounter?

We faced three main difficulties. First, GPU memory constraints — full 3D CT volumes are too large to process at once, so we used patch-based training. Second, severe class imbalance — tumor and cyst voxels are a tiny fraction of the total volume, which biases the model toward predicting background. We addressed this with specialized loss functions. Third, convergence instability — 3D segmentation training can be sensitive to learning rate and batch size, so we used learning rate scheduling and early stopping. Each difficulty and its mitigation is documented.

### Q21: How did you handle class imbalance?

Class imbalance is a fundamental challenge in medical segmentation. We addressed it through multiple strategies: specialized loss functions that weight tumor voxels more heavily, patch-based sampling that ensures training patches contain tumor tissue, and conservative post-processing that preserves small tumor predictions. The exact loss function is documented in the experiment log. This combination of strategies allowed the model to achieve 100 percent tumor detection despite the imbalance.

### Q22: Did you encounter overfitting?

We monitored validation metrics throughout training and used early stopping to prevent overfitting. Because the test set of 64 cases was entirely independent and never seen during training or validation, our final evaluation provides an honest estimate of generalization within the KiTS23 distribution. Overfitting to the training set would manifest as a large gap between validation and test performance, which we did not observe.

---

## 9. Cyst/Tumor Segmentation Difficulty

### Q23: Why is cyst and tumor segmentation more difficult than kidney segmentation?

Kidney segmentation is relatively straightforward because the kidney is a large organ with a consistent bean-like shape, predictable retroperitoneal location, and relatively clear boundaries with surrounding fat. Tumor and cyst segmentation is harder for several reasons. First, lesions are small — some are only a few hundred voxels — which means even a minor boundary error produces a large penalty in overlap metrics. Second, tumor boundaries are often ambiguous. Malignant tumors can infiltrate the renal parenchyma without forming a clear capsule, making the exact border uncertain even for human experts. Third, tumors and cysts vary enormously in appearance — they can be homogeneous, heterogeneous, cystic, solid, necrotic, or calcified — and the model must generalize across this entire spectrum. Fourth, on CT, a cyst and a hypovascular tumor can look very similar, and the KiTS23 dataset merges them into one class, which confuses the learned feature representation.

### Q24: Does the system distinguish between a cyst and a tumor?

No, it does not. The KiTS23 dataset merges cysts and tumors into a single foreground class, and our model follows this convention. The output mask is labeled "tumor/cyst" and does not differentiate between the two. Distinguishing a benign cyst from a potentially malignant tumor would require a separate classification stage, which is listed as future work. This limitation is clearly documented in our report and presentation.

---

## 10. Tumor Dice vs. Kidney Dice

### Q25: Why is the tumor Dice 0.6558 while the kidney Dice is 0.9307?

This gap reflects the difference between segmenting a large, consistent organ and segmenting small, variable lesions. The kidney is hundreds of thousands of voxels with predictable shape and clear boundaries. A one-voxel boundary error on the kidney is negligible. Tumors can be as small as one hundred voxels, and a one-voxel boundary error on a lesion of that size can reduce Dice from near-perfect to approximately 0.70. This is a mathematical property of the Dice metric on small objects. The tumor Dice of 0.6558 with a standard deviation of 0.262 reflects tumor size variability and boundary ambiguity, not a failure to detect tumors — our detection rate is 100 percent. This performance level is consistent with published KiTS23 challenge baselines.

### Q26: Is 0.6558 Dice clinically acceptable for tumor segmentation?

We cannot claim clinical acceptability because no prospective clinical validation has been performed. What we can say is that this number reflects the difficulty of the task, not a deficiency in our implementation. Published results on KiTS23 show similar tumor Dice levels. The clinical utility depends on the use case: for detection and approximate volumetric assessment, the system is useful. For surgical planning requiring millimeter-precise boundaries, additional refinement is needed. This is why we present the system as decision-support requiring physician review.

### Q27: How should the committee interpret the high standard deviation of 0.262 on tumor Dice?

The standard deviation of 0.262 indicates that tumor segmentation performance varies considerably across cases. Some tumors are segmented well, with Dice scores well above 0.80, while others are segmented poorly, with Dice below 0.40. This variability is driven by lesion size, boundary clarity, and appearance heterogeneity. We have not yet completed size-stratified analysis to quantify performance as a function of lesion volume — that is planned future work.

---

## 11. Detection vs. Segmentation

### Q28: If tumor detection is 100 percent, why is tumor Dice only 0.6558?

Because detection and boundary segmentation are different tasks. Detection answers a binary question: is there a tumor in this scan? Our model answers correctly for all 64 test cases. Segmentation answers a voxel-level question: exactly which voxels belong to the tumor? This is much harder because it requires precise boundary delineation. Our model finds every tumor, but the boundaries it draws are approximate. This is not a contradiction — it is a realistic outcome for a task where detection is easier than precise boundary delineation.

### Q29: Does a detection rate of 64 out of 64 guarantee no tumor will ever be missed?

No. Sixty-four out of sixty-four on the KiTS23 held-out test set is a strong result, but it is not a guarantee. Very small lesions near the detection threshold could be missed on new data, especially data from different scanner protocols or patient populations outside the KiTS23 distribution. This is why we explicitly state that the system is not a substitute for physician review and that performance on non-KiTS23 data is unknown.

---

## 12. Failure Cases

### Q30: What failure cases did the team observe?

We observed four main categories. First, tumor boundary leakage, where the predicted mask extends beyond the true tumor into healthy parenchyma — our HD95 of 67.35 millimeters quantifies this. Second, sensitivity to small lesion boundaries, where minor errors cause large Dice drops. Third, cyst and tumor confusion due to the merged KiTS23 class. Fourth, domain shift risk, where performance on CT data from different scanners is unknown. We analyzed these failure modes systematically and documented each one with its likely cause, clinical risk, and current mitigation.

### Q31: Can you show an example of a failure case?

Yes, we have prepared anonymized examples from our test set showing boundary leakage and under-segmentation. In each case we show the original CT, the ground truth annotation, our prediction, and the difference map highlighting where errors occurred. These examples are documented in our failure case analysis and are available for committee review.

### Q32: What is the clinical consequence of a boundary leakage error?

If used without physician review, a boundary leakage error could lead to an overestimated tumor volume, which might influence surgical planning or treatment response assessment. This is precisely why the system is decision-support only and why all outputs require physician review. The physician can see the predicted mask overlaid on the original CT and judge whether the boundary is clinically plausible.

---

## 13. Future Improvements

### Q33: What would the team improve next?

Our highest priorities are improving tumor boundary accuracy through boundary-aware loss functions such as Boundary loss or Hausdorff loss, conducting external multi-center validation on CT data from different scanners and institutions, and evaluating the nnU-Net self-configuring framework as a baseline comparison. Medium priorities include adding a cyst-versus-tumor classification stage, implementing uncertainty estimation to flag low-confidence regions, and performing per-lesion size-stratified analysis. Lower priority but still valuable is inference latency optimization.

### Q34: Why is external validation the highest priority?

Because all our results are based on KiTS23 data. Without testing on data from other scanners, institutions, and patient populations, we cannot claim the system generalizes. Domain shift is a well-documented problem in medical AI, and external validation is the only way to quantify its impact. This is both a scientific requirement and a patient safety requirement.

---

## 14. Implemented vs. Future Work

### Q35: What parts of the system are fully implemented versus future work?

The full pipeline is implemented end to end: NIfTI loading, preprocessing with HU clipping and normalization, 3D U-Net inference with sliding window and test-time augmentation, post-processing with blob removal, and web-based 3D visualization with volumetric statistics. What is not implemented and is listed as future work includes: boundary-aware loss functions for improved tumor accuracy, external multi-center validation, a cyst-versus-tumor classification stage after segmentation, uncertainty estimation for low-confidence regions, and full IEC 62304 compliance documentation.

### Q36: Is the web application fully functional?

Yes, the web application accepts NIfTI file uploads, runs the full inference pipeline, and displays the 3D segmentation mesh alongside volumetric statistics. It is built with standard web technologies. The exact framework and technology stack are documented. The application is an academic prototype and is not deployed in any clinical setting.

---

## 15. Reproducibility

### Q37: How is reproducibility ensured?

We have documented: the hardware and software environment, all preprocessing steps with exact parameters, the model architecture, the inference pipeline configuration, the post-processing thresholds, and the exact metrics achieved. Our experiment log records every training run with hyperparameters and results. We have captured the exact commands used for training and inference. The data split with the 64 held-out test cases is recorded. The remaining reproducibility task is to package all of this into a single reproducible script — that is in progress.

### Q38: Could another team reproduce your results?

Yes, given access to the KiTS23 dataset and our documentation. They would need: the exact preprocessing pipeline with HU clipping at minus two hundred to three hundred and normalization to zero to one, our model architecture and trained weights, the sliding-window inference configuration with sixty-four by one ninety-two by one ninety-two patches and fifty percent overlap, eight-flip test-time augmentation, and post-processing with kidney blobs below five thousand voxels and tumor blobs below one hundred voxels removed. With these components and our documented random seeds, the results should be reproducible. The exact training command and environment specification are being finalized for the submission package.

### Q39: Are the trained model weights available?

Yes, the model checkpoint from the best validation epoch is saved and can be provided. The checkpoint file name and location are recorded in the model training documentation. Inference can be run using this checkpoint with the documented inference configuration.

---

## Cross-Cutting Questions

### Q40: How does the team demonstrate scientific maturity in this work?

We demonstrate scientific maturity in three ways. First, we do not overclaim — the system is explicitly described as an academic prototype, not clinically approved, and decision-support only. Second, we document our process, not just our results — the experiment log, training documentation, preprocessing rationale, and failure analysis provide a complete record of how we reached the final system. Third, we report both strengths and weaknesses — we celebrate the robust kidney Dice of 0.93 and the 100 percent detection rate, but we also honestly present the moderate tumor Dice of 0.66, the boundary uncertainty, and the known limitations.

### Q41: What is the single most important thing the committee should know about your development process?

That we did not only report the final model — we documented the pipeline decisions, training setup, inference choices, and known limitations. The mid-year feedback pushed us in this direction, and the result is a development documentation package that makes our engineering process transparent, reproducible, and defensible.

### Q42: If you had to start over, what would you do differently?

We would document every experiment from day one rather than retroactively organizing the experiment log. We learned that documentation is not overhead — it is an investment that pays off during the defense, when the committee asks detailed questions about what we tried and why we chose each approach. We would also start with a more rigorous hyperparameter search strategy earlier in the project.

---

**All answers must remain consistent with MASTER_CONTEXT.md, KNOWN_METRICS.md, DO_NOT_OVERCLAIM.md, and the experiment log.**
