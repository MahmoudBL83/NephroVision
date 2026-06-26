# Elevator Pitch

## NephroVision — Automated Kidney and Renal Tumor Segmentation System

Multiple versions for different audiences and time constraints. All versions are consistent with `MASTER_CONTEXT.md` and `DO_NOT_OVERCLAIM.md`.

---

## 1. Ten-Second Pitch

> NephroVision is an academic prototype that automatically segments kidneys and renal tumors from CT scans using a 3D U-Net, to support radiologists — not replace them.

---

## 2. Thirty-Second Pitch

> NephroVision is an academic decision-support prototype for automated kidney and renal tumor segmentation from abdominal CT scans. It uses a 3D U-Net trained on the KiTS23 dataset and outputs a 3D segmentation mask, volumetric statistics, and an interactive browser-based visualization. On 64 held-out test cases, it achieved a kidney Dice of 0.93, tumor detection of 100%, and a tumor Dice of 0.66. It is not clinically approved, and every output requires physician review.

---

## 3. Sixty-Second Pitch

> NephroVision is an academic decision-support prototype that automates kidney and renal tumor segmentation from contrast-enhanced CT scans. Manual segmentation is slow and variable between radiologists, so we built a system that produces a fast, reproducible starting point for physician review. Our pipeline loads NIfTI CT volumes, applies HU clipping and normalization, runs a 3D U-Net with sliding-window inference and test-time augmentation, and applies post-processing to remove false positives. The output is a 3D segmentation mask, kidney and tumor volumetric statistics, and a browser-based 3D viewer. We evaluated on 64 independent held-out cases from KiTS23. Kidney Dice was 0.9307, tumor detection was 100%, and tumor Dice was 0.6558 — the lower tumor Dice reflects boundary difficulty on small lesions, not detection failure. The system is not clinically approved, does not diagnose, and all outputs require physician review.

---

## 4. Technical Pitch

> NephroVision is a volumetric semantic segmentation system for abdominal CT. The pipeline: NIfTI loading and validation, HU clipping to [-200, 300], normalization to [0, 1], a 3D U-Net with three output classes — background, kidney, and tumor/cyst — sliding-window inference at 64×192×192 with 50% overlap, 8-flip test-time augmentation, and connected-component post-processing removing kidney blobs below 5000 voxels and tumor blobs below 100 voxels. Evaluated on 64 held-out KiTS23 cases: kidney Dice 0.9307 ± 0.064, tumor Dice 0.6558 ± 0.262, mean Dice 0.7933, tumor detection 100%, HD95 kidney 19.98 mm, HD95 tumor 67.35 mm. The tumor Dice gap reflects Dice sensitivity to boundary errors on small lesions, not detection failure. It is an academic prototype, not clinically approved.

---

## 5. Clinical-Support Pitch

> NephroVision is a decision-support tool that helps radiologists and urologists assess kidney and renal tumors from CT scans. Instead of drawing boundaries slice by slice, the physician uploads a CT volume and the system produces a 3D segmentation mask, kidney and tumor volume measurements, and an interactive 3D view. The physician reviews the result, adjusts if needed, and makes the clinical decision. On our test set, the system found every tumor — 100% detection — and segmented the kidney with high accuracy. Tumor boundaries are less precise, especially for small lesions, so physician review is essential. NephroVision is an academic prototype. It is not clinically approved, it does not diagnose cancer, and it does not replace the radiologist. It supports the workflow — the physician stays in charge.

---

## 6. Examiner-Safe Pitch

> NephroVision is an academic decision-support prototype for automated kidney and renal tumor/cyst segmentation from CT volumes, developed as a graduation project in the Medical Engineering Department. We trained a 3D U-Net on the KiTS23 dataset and evaluated on 64 independent held-out test cases. Kidney Dice was 0.9307, tumor detection was 100%, and tumor Dice was 0.6558. We documented the full development process — preprocessing decisions, training setup, inference configuration, challenges, and failure analysis — in response to mid-year feedback. The system is classified under IEC 62304 Class B. It is not clinically approved, not FDA approved, and all outputs require physician review. We distinguish clearly between implemented work, observed limitations, and planned future work.

---

## 7. Arabic Explanation (Internal Team Use)

> نظام NephroVision هو نموذج أولي أكاديمي لتجزئة الكلى والأورام والكيسات الكلوية من صور التصوير المقطعي المحوسب. يستخدم شبكة 3D U-Net مدرّبة على مجموعة بيانات KiTS23. المخرجات عبارة عن قناع تجزئة ثلاثي الأبعاد، وإحصاءات حجمية للكلية والورم، وتصور ثلاثي الأبعاد عبر المتصفح. تم التقييم على 64 حالة اختبار مستقلة: معامل دايس للكلية 0.93، واكتشاف الأورام 100%، ومعامل دايس للورم 0.66 الأقل بسبب صعوبة تحديد الحدود في الأورام الصغيرة. النظام أداة دعم قرار وليس تشخيصًا، وكل المخرجات تحتاج مراجعة طبيب، وهو غير معتمد سريريًا.

---

## Usage Guide

| Version | Use Case | Audience |
|---------|----------|----------|
| 10-second | Quick introduction, networking | Anyone |
| 30-second | Brief hallway conversation | General academic |
| 60-second | Short formal introduction | Committee member before defense |
| Technical | Peer engineer or CS faculty | Technical audience |
| Clinical-support | Clinician or medical faculty | Clinical audience |
| Examiner-safe | Defense Q&A fallback | Examiner committee |
| Arabic | Internal team coordination | Team members |

---

**All versions are consistent with MASTER_CONTEXT.md, KNOWN_METRICS.md, and DO_NOT_OVERCLAIM.md. No version claims clinical approval, diagnosis, or radiologist replacement.**
