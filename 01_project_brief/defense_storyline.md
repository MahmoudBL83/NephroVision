# Defense Storyline

## NephroVision — Automated Kidney and Renal Tumor Segmentation System

**Duration target:** 12–15 minutes presentation, followed by Q&A.

---

## Full Storyline

This is the narrative arc of the NephroVision defense. It is designed to be memorable, honest, and defense-ready.

### Beat 1 — Clinical Problem

Every kidney and renal tumor assessment begins with a CT scan. But turning that scan into a measurement requires a radiologist to draw the kidney boundary and the tumor boundary slice by slice. This is slow, it is costly, and different radiologists draw different boundaries for the same tumor. That variability affects every downstream decision — surgical planning, treatment monitoring, and follow-up. There is a real clinical need for automated support, but that support must assist physicians, not replace them.

### Beat 2 — Engineering Objective

We set out to build NephroVision, an academic decision-support prototype for automated kidney and renal tumor segmentation from CT volumes. The goal was not to build a diagnostic system. The goal was to build a tool that produces a fast, reproducible segmentation that a physician can review and trust as a starting point.

### Beat 3 — Dataset

We used the KiTS23 challenge dataset — contrast-enhanced abdominal CT volumes with expert annotations for three classes: background, kidney, and tumor or cyst. We held out 64 cases for independent testing and never touched them during development. We did not create this dataset; we used it as the foundation for training and evaluation.

### Beat 4 — Development Process

We built the system through an iterative, documented engineering process. We designed the preprocessing pipeline — HU clipping to minus two hundred to three hundred, normalization to zero to one. We implemented a 3D U-Net for volumetric segmentation. We developed sliding-window inference with test-time augmentation. We added post-processing to remove false positives. And we built a web application for 3D visualization. After mid-year feedback, we documented every step — the timeline, the experiments, the decisions, and the difficulties.

### Beat 5 — Technical Challenge

The central technical challenge was tumor and cyst segmentation. The kidney is large and anatomically consistent, so segmenting it is relatively tractable. Tumors are small, their boundaries are often ambiguous, and their appearance varies widely — from simple cysts to complex heterogeneous masses. The KiTS23 dataset merges tumors and cysts into one class, which adds further complexity. This is an open research problem, and we approached it honestly.

### Beat 6 — System Output

The system takes a NIfTI CT volume as input and produces three outputs: a 3D segmentation mask, kidney and tumor volumetric statistics, and an interactive browser-based 3D visualization. No specialized software is required. The physician can see the original CT and the predicted mask side by side and judge whether the result is clinically plausible.

### Beat 7 — Validation

We evaluated the final pipeline on 64 independent held-out test cases from KiTS23. These cases were never seen during training or validation. We computed Dice score, Hausdorff Distance, and tumor detection rate.

### Beat 8 — Results

The results tell a clear story. Kidney segmentation is robust — Dice of 0.9307. Tumor detection is reliable — 100 percent, all 64 tumors found. But tumor boundary segmentation is moderate — Dice of 0.6558. This is not a failure. It reflects the difficulty of drawing precise borders on small, ambiguous lesions. A one-voxel error on a small tumor can drop Dice dramatically. The Hausdorff Distance for tumor — 67.35 millimeters — confirms that boundary uncertainty is the main remaining challenge.

### Beat 9 — Safety

We classified NephroVision under IEC 62304 Software Safety Class B. The system is an academic prototype. It is not clinically approved. It is not FDA approved. It does not replace radiologists. Every output requires physician review, and every clinical decision remains the responsibility of qualified healthcare professionals. We built safe wording rules into every document, slide, and speaker note to ensure we never overclaim.

### Beat 10 — Honest Limitations

We are honest about what the system does not do. We did not conduct a prospective clinical trial. We evaluated only on KiTS23, so performance on other scanners and patient populations is unknown. Tumor boundary accuracy can improve. The system cannot distinguish a benign cyst from a malignant tumor. These are not hidden weaknesses — they are known boundaries that we documented explicitly.

### Beat 11 — Future Work

Our roadmap is clear. The highest priority is external multi-center validation. We want to evaluate nnU-Net as a self-configuring baseline. We want to improve tumor boundaries with boundary-aware loss functions. We want to add a cyst-versus-tumor classification stage. And we want to implement uncertainty estimation so the system can flag low-confidence regions for the physician.

### Beat 12 — Final Takeaway

NephroVision demonstrates a documented end-to-end biomedical AI prototype for kidney and tumor segmentation. We did not only report the final model — we documented the process, the challenges, the failures, and the decisions. The system achieves robust kidney segmentation and reliable tumor detection, with honest acknowledgment of where tumor boundary precision needs improvement. This is decision-support, not diagnosis. And it is the product of an engineering process that we can defend in detail.

---

## Slide-to-Story Mapping

This maps the 21-slide presentation to the 12-story beats. Use this to ensure the narrative flows during delivery.

| Slide | Title | Story Beat | Time Target |
|-------|-------|------------|-------------|
| 1 | Title | Opening — set identity and tone | 0:30 |
| 2 | Clinical Problem | Beat 1 — manual segmentation burden | 1:00 |
| 3 | Why Segmentation Matters | Beat 1 — clinical impact | 1:15 |
| 4 | Project Objective | Beat 2 — decision-support scope | 1:30 |
| 5 | Dataset: KiTS23 | Beat 3 — data foundation | 2:00 |
| 6 | Development Journey | Beat 4 — iterative documented process | 3:00 |
| 7 | What We Built | Beat 4 — pipeline overview | 3:30 |
| 8 | Preprocessing Decisions | Beat 4 — preprocessing detail | 4:15 |
| 9 | Model Training Documentation | Beat 4 — training detail | 5:00 |
| 10 | 3D U-Net Architecture | Beat 4 — architecture rationale | 5:30 |
| 11 | Inference Pipeline | Beat 4 — inference configuration | 6:00 |
| 12 | Post-processing | Beat 4 — post-processing thresholds | 6:30 |
| 13 | Key Challenge: Tumor/Cyst Segmentation | Beat 5 — the hardest problem | 7:30 |
| 14 | Web Application | Beat 6 — system output and visualization | 8:00 |
| 15 | Validation Setup | Beat 7 — independent test evaluation | 8:30 |
| 16 | Results | Beat 8 — metrics and interpretation | 9:30 |
| 17 | Target vs. Achieved | Beat 8 — goals comparison | 10:00 |
| 18 | Failure Analysis and Limitations | Beat 10 — honest limitations | 11:00 |
| 19 | Safety and IEC 62304 | Beat 9 — regulatory positioning | 11:30 |
| 20 | Future Work | Beat 11 — roadmap | 12:00 |
| 21 | Final Takeaway | Beat 12 — closing message | 12:30 |

**Total presentation time:** ~12.5 minutes, leaving 2.5 minutes buffer within a 15-minute slot.

**Pacing notes:**
- Slides 1–5: fast pacing, set context (2 minutes)
- Slides 6–12: moderate pacing, show process (4.5 minutes) — this is where mid-year feedback is addressed
- Slide 13: slow down, this is the critical technical message (1.5 minutes)
- Slides 14–17: moderate pacing, show results (2.5 minutes)
- Slides 18–21: deliberate pacing, close honestly (2 minutes)

---

## 90-Second Opening Speech

> "Good morning, and thank you for being here today. Our project is called NephroVision, and it addresses a problem that every radiologist faces: drawing the boundary of the kidney and the boundary of a tumor, slice by slice, across hundreds of CT images. This manual process is slow, it is costly, and when two radiologists draw the same tumor, they often draw different boundaries. That variability affects surgical planning, treatment monitoring, and patient follow-up.
>
> We built NephroVision to address this — not as a diagnostic system, and not as a replacement for the radiologist, but as a decision-support tool that produces a fast, reproducible segmentation for physician review. We trained a 3D U-Net on the KiTS23 challenge dataset, and we evaluated it on 64 independent held-out test cases. Our kidney segmentation is robust, our tumor detection is reliable, and our tumor boundary precision is honest — it is moderate, and we will explain exactly why.
>
> What makes this defense different is that we are not only presenting the final result. After our mid-year discussion, we documented the entire engineering process — the experiments, the decisions, the difficulties, and the failures. We will walk you through that journey today."

---

## 30-Second Final Closing Speech

> "NephroVision demonstrates that automated kidney and tumor segmentation is feasible within an academic framework. We achieved robust kidney segmentation, reliable tumor detection, and we honestly reported where tumor boundary precision needs improvement. This is decision-support, not diagnosis — every output requires physician review. We documented the process, we acknowledged the limitations, and we have a clear roadmap for future work. Thank you. We welcome your questions."

---

## Key Message Per Team Member

**For a 5-person team presentation, each member should own a specific part of the story. This ensures every member can speak confidently and the committee sees balanced contribution.**

### Rashed Mamdouh — Clinical Problem and Project Objective

**Key message:** "We framed this as a decision-support problem from the start. Manual segmentation is slow and variable, and our goal was to build a tool that assists physicians, not one that replaces them."

**Owns:** Slides 1–4 (Title, Clinical Problem, Why Segmentation Matters, Project Objective)

**If asked:** Explain the clinical workflow, the inter-observer variability problem, and why decision-support is the correct framing. Never claim the system diagnoses or replaces radiologists.

---

### Mohamed Walid — Dataset and Preprocessing

**Key message:** "We used KiTS23 as our data foundation and designed a reproducible preprocessing pipeline with HU clipping at minus two hundred to three hundred and normalization to zero to one. Every preprocessing choice was documented and validated empirically."

**Owns:** Slides 5 and 8 (Dataset: KiTS23, Preprocessing Decisions)

**If asked:** Explain the dataset structure, the three classes, the 64 held-out test cases, the HU clipping rationale, and why preprocessing consistency between training and inference matters.

---

### Mahmoud BahaaAldeen — Model Training and Inference Pipeline

**Key message:** "We implemented a 3D U-Net for volumetric segmentation and built a sliding-window inference pipeline with test-time augmentation. Every experiment was logged with hyperparameters and decisions — we can show the committee the full record."

**Owns:** Slides 6, 9, 10, 11 (Development Journey, Model Training Documentation, 3D U-Net Architecture, Inference Pipeline)

**If asked:** Explain why 3D over 2D, the sliding-window configuration, the 8-flip TTA, and the experiment log. If asked for exact hyperparameters, reference the experiment log and state: "The detailed values are recorded in the experiment log; in the defense we focus on the verified final configuration and results."

---

### Mahmoud Mohammed — Tumor/Cyst Challenge, Results, and Failure Analysis

**Key message:** "Tumor and cyst segmentation was the hardest part. Our tumor detection rate is 100 percent — we found every tumor. But boundary precision is moderate, with a Dice of 0.6558, and we explain exactly why: small lesions, ambiguous boundaries, and Dice sensitivity to boundary errors on small objects."

**Owns:** Slides 12, 13, 16, 17, 18 (Post-processing, Key Challenge, Results, Target vs. Achieved, Failure Analysis and Limitations)

**If asked:** Explain the detection-versus-boundary distinction, the Dice sensitivity to small lesions, the HD95 values, the failure modes, and the mitigations. Do not apologize for the tumor Dice — contextualize it.

---

### Youssef Mohammed — Web Application, Safety, and Future Work

**Key message:** "We built a browser-based 3D visualization system and classified the software under IEC 62304 Class B. The system is an academic prototype — not clinically approved, not FDA approved, and all outputs require physician review. Our future work focuses on external validation and improved tumor segmentation."

**Owns:** Slides 7, 14, 15, 19, 20, 21 (What We Built, Web Application, Validation Setup, Safety and IEC 62304, Future Work, Final Takeaway)

**If asked:** Explain the web interface, the IEC 62304 classification, the intended-use statement, the known regulatory gaps, and the prioritized future work roadmap.

---

## Storytelling Principles

1. **Start with the patient, not the code.** The opening should make the committee care about the problem before any technical detail.
2. **Show the process, not just the result.** The mid-year feedback is addressed by demonstrating that the team documented the journey — experiments, decisions, difficulties, and failures.
3. **Be honest about tumor Dice.** Do not hide the 0.6558. Contextualize it: detection is 100 percent, boundaries are moderate, and this is consistent with the task difficulty.
4. **Return to decision-support framing.** Whenever the conversation drifts toward "does it diagnose?" or "is it clinically approved?", return to: "This is decision-support. All outputs require physician review."
5. **End with the roadmap.** Do not end on limitations. End on what comes next — external validation, nnU-Net, boundary-aware losses, and clinical validation protocol.
6. **Make it memorable.** The committee will remember one sentence: "We found every tumor, but drawing the exact border is still hard — and that is why the physician reviews every output."

---

## Time Budget Summary

| Segment | Slides | Time |
|---------|--------|------|
| Opening and context | 1–5 | 2:00 |
| Development process | 6–12 | 4:30 |
| Key challenge | 13 | 1:30 |
| Results and evaluation | 14–17 | 2:30 |
| Limitations and safety | 18–19 | 1:30 |
| Future work and closing | 20–21 | 1:30 |
| **Total** | **21** | **~13:00** |

**Buffer:** 2 minutes within a 15-minute slot for natural pauses, slide transitions, and committee attention shifts.

---

**This storyline is consistent with MASTER_CONTEXT.md, KNOWN_METRICS.md, DO_NOT_OVERCLAIM.md, and the full development documentation.**
