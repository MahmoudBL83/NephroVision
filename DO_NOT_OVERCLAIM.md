# Do Not Overclaim

Guard against unsafe wording in reports, slides, speaker notes, and Q&A.

---

## Forbidden Phrases

Never use the following claims:

| Forbidden Claim | Why It Is Unsafe |
|-----------------|------------------|
| FDA approved | No regulatory submission or clearance exists. |
| Clinically validated | No prospective clinical trial was conducted. |
| Replaces radiologists | System is decision-support only. |
| Diagnoses cancer | System performs segmentation, not diagnosis. |
| Autonomous medical decision | All outputs require physician review. |
| Ready for hospital deployment | Academic prototype; deployment gaps remain. |
| Guaranteed accurate | Metrics include uncertainty and known failure modes. |
| Works on all CT scanners | Evaluated only on KiTS23 data; domain shift risk exists. |

## Safe Replacement Phrases

Use these instead:

| Unsafe Phrase | Safe Alternative |
|---------------|------------------|
| FDA approved | Academic prototype; not FDA approved |
| Clinically validated | Evaluated on KiTS23 held-out test cases; clinical validation is future work |
| Replaces radiologists | Supports radiologists as a decision-support tool |
| Diagnoses cancer | Segments kidney and tumor/cyst regions for review |
| Autonomous medical decision | Provides segmentation outputs that require physician review |
| Ready for hospital deployment | Future work includes deployment readiness and cybersecurity review |
| Guaranteed accurate | Achieved X metric on the KiTS23 test set with known limitations |
| Works on all CT scanners | Evaluated on KiTS23 protocols; external validation is required |

## Additional Safe Language

- Academic prototype
- Decision-support tool
- Requires physician review
- Segmentation and volumetric quantification
- Evaluated on KiTS23 held-out test cases
- Future external validation required

## Examples: Unsafe vs Safe Wording

### Example 1: Regulatory Status

- **Unsafe:** "NephroVision is FDA approved for kidney tumor diagnosis."
- **Safe:** "NephroVision is an academic prototype and is not FDA approved. It is intended only as decision-support software."

### Example 2: Clinical Role

- **Unsafe:** "The system replaces radiologists by automatically detecting renal tumors."
- **Safe:** "The system assists radiologists by generating kidney and tumor segmentation masks for physician review."

### Example 3: Generalization

- **Unsafe:** "NephroVision works accurately on all CT scanners."
- **Safe:** "NephroVision was evaluated on 64 held-out cases from KiTS23. Performance on other scanner protocols requires external validation."

### Example 4: Performance

- **Unsafe:** "NephroVision guarantees accurate tumor segmentation."
- **Safe:** "NephroVision detected all tumors in the KiTS23 test set (64/64) and achieved a tumor Dice of 0.6558 ± 0.262."

### Example 5: Autonomy

- **Unsafe:** "NephroVision makes autonomous medical decisions about renal masses."
- **Safe:** "NephroVision produces segmentation outputs and volumetric statistics; all clinical decisions remain the responsibility of qualified healthcare professionals."

## Required Disclaimers

- Include a limitations section in the IEEE report.
- Add a limitations and intended-use slide in the presentation.
- State that the system is not a substitute for professional medical judgment.
