# Slide Content Source

## NephroVision — 21-Slide Defense Presentation

### Slide Structure

| # | Slide Title | Emphasis |
|---|-------------|----------|
| 1 | Title | Project identity, team, supervisor |
| 2 | Clinical Problem | Why automation is needed |
| 3 | Why Segmentation Matters | Clinical impact |
| 4 | Project Objective | Decision-support scope |
| 5 | Dataset: KiTS23 | Data foundation |
| 6 | **Development Journey** | What we did, why, difficulties, mitigations, future work |
| 7 | What We Built | Pipeline overview |
| 8 | **Preprocessing Decisions** | What we did, why, difficulties, mitigations, future work |
| 9 | **Model Training Documentation** | What we did, why, difficulties, mitigations, future work |
| 10 | 3D U-Net Architecture | Technical overview |
| 11 | Inference Pipeline | Sliding window + TTA |
| 12 | Post-processing | Blob removal thresholds |
| 13 | **Key Challenge: Tumor/Cyst Segmentation** | What we did, why, difficulties, mitigations, future work |
| 14 | Web Application | Visualization demo |
| 15 | Validation Setup | 64 held-out test cases |
| 16 | Results | Metrics table |
| 17 | Target vs. Achieved | Goal comparison |
| 18 | **Failure Analysis and Limitations** | What we did, failure modes, mitigations, future work |
| 19 | Safety and IEC 62304 | Regulatory framing |
| 20 | Future Work | Prioritized directions |
| 21 | Final Takeaway | Summary + Q&A |

### Visual Design Notes

- Max 4 bullets per slide (enforced)
- Use tables for structured data (metrics, comparisons)
- Use v-click for progressive reveal on key messages
- Include footer: "Decision-Support Prototype | Not Clinically Approved"
- Emphasis slides (6, 8, 9, 13, 18) use 4-section layout: What/Why, Difficulties, Mitigations, Future Work

### Metrics to Display

- Kidney Dice: 0.9307 +/- 0.064
- Tumor Dice: 0.6558 +/- 0.262
- Mean Dice: 0.7933
- Tumor Detection Rate: 64/64 = 100%
- HD95 Kidney: 19.98 mm
- HD95 Tumor: 67.35 mm

### TODO Items

- [ ] Add project logo/branding to title slide
- [ ] Insert dataset sample images (Slide 5)
- [ ] Create pipeline diagram (Slide 7)
- [ ] Add architecture diagram (Slide 10)
- [ ] Insert result overlays: ground truth vs. prediction (Slide 16)
- [ ] Add web app screenshots (Slide 14)
- [ ] Record demo video or GIF for web interface
- [ ] Insert failure case examples (Slide 18)
- [ ] Verify all metrics match KNOWN_METRICS.md
- [ ] Complete TODO placeholders in Slides 8, 9, 14
