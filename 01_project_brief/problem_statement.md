# Problem Statement

## NephroVision — Automated Kidney and Renal Tumor Segmentation System

---

## Short Version (~100 words)

Manual slice-by-slice delineation of kidney and renal tumors in abdominal CT scans is time-consuming, costly, and affected by inter-observer variability. Accurate segmentation matters because it supports anatomical localization of the kidney and volumetric quantification of tumors and cysts for surgical planning, treatment monitoring, and follow-up. Automated segmentation can reduce radiologist workload and improve consistency, but tumor and cyst segmentation is technically challenging due to small lesion size, ambiguous boundaries, and heterogeneous appearance. NephroVision addresses this challenge as a decision-support prototype — it assists physicians but does not replace them, and all outputs require clinical review.

---

## Medium Version (~250 words)

Contrast-enhanced abdominal CT is the primary imaging modality for kidney and renal tumor assessment. However, manual segmentation of the kidney and any tumors or cysts is performed slice by slice, which is time-consuming, resource-intensive, and subject to inter-observer variability. Different radiologists may draw different boundaries for the same lesion, especially when tumor margins are infiltrative or ill-defined. This variability affects the reliability of volumetric measurements used in surgical planning, treatment response assessment, and longitudinal follow-up.

Automated segmentation offers a way to reduce workload and improve consistency. A system that produces a 3D segmentation mask, volumetric statistics, and interactive visualization can support radiologists and urologists by providing a fast, reproducible starting point that the physician can review and adjust. This is the role NephroVision is designed to fill.

The technical challenge is significant. Kidney segmentation is relatively tractable because the organ is large and anatomically consistent. Tumor and cyst segmentation is substantially harder. Lesions can be very small, their boundaries are often ambiguous, and their appearance on CT is heterogeneous — ranging from simple fluid-density cysts to complex heterogeneous masses. The KiTS23 dataset merges tumors and cysts into a single class, adding further complexity. These factors make automated tumor segmentation an open research problem.

This problem is well-suited for biomedical engineering because it requires integrating medical imaging knowledge, deep learning, software system design, and regulatory awareness into a single decision-support tool. NephroVision is an academic prototype, not a clinically approved device, and it does not replace physician judgment.

---

## Presentation Version (4 Bullet Points)

- **Manual segmentation is slow and variable:** Slice-by-slice delineation of kidney and tumor in CT is time-consuming and subject to inter-observer variability, affecting measurement reliability.
- **Volumetric segmentation supports clinical decisions:** Accurate kidney localization and tumor volume quantification inform surgical planning, treatment monitoring, and follow-up.
- **Tumor/cyst segmentation is technically hard:** Small lesions, ambiguous boundaries, and heterogeneous appearance make automated tumor segmentation significantly more challenging than kidney segmentation.
- **NephroVision is decision-support only:** The system assists physicians with reproducible segmentation and visualization — it does not diagnose, it is not clinically approved, and all outputs require physician review.

---

## Spoken Version (45-Second Script)

> "Kidney and renal tumor assessment relies on CT imaging, but manual segmentation is done slice by slice. It is slow, and different radiologists often draw different boundaries for the same tumor, especially when the margins are unclear. This variability matters because the measurements are used for surgical planning and treatment monitoring. NephroVision addresses this by automating kidney and tumor segmentation using a 3D U-Net trained on the KiTS23 dataset. The technical challenge is real — tumors are small, their boundaries are ambiguous, and their appearance varies widely. Our system provides reproducible segmentation and volumetric statistics that a physician can review. It is a decision-support tool, not a replacement for the radiologist."

---

## Key Constraints

- NephroVision is an academic prototype.
- It is not clinically approved and not FDA approved.
- It does not diagnose cancer.
- It does not replace radiologists or physician judgment.
- All outputs require physician review.
- Tumor/cyst segmentation difficulty is acknowledged honestly.

---

**This problem statement is consistent with MASTER_CONTEXT.md and DO_NOT_OVERCLAIM.md.**
