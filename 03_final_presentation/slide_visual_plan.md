# NephroVision — Slide Visual Plan

> Defines exactly what visual appears on each slide. Existing 21 slides plus candidate additional slides. Remove slides you do not need.

---

## Existing Slides (1–21)

### Slide 1 — Title
- **Main visual:** Project name, subtitle, team, supervisor, safety badges
- **Visual type:** Text + safety badges
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** Establishes project identity, scope boundary (decision-support), and team credibility in first 20 seconds

---

### Slide 2 — The Clinical Problem
- **Main visual:** Three cards: Time-Consuming, Variable, Growing Workload
- **Visual type:** Metric card (text-based)
- **Required image:** Clinical problem illustration (radiologist at workstation)
- **Placeholder instruction:** `PLACEHOLDER: clinical_problem_illustration.png` — photo or illustration of radiologist manually contouring CT slices. Source: stock medical image or simple icon set. Can use free medical illustration from smart.servier.com
- **Why:** Frames the problem as workload + consistency, not radiologist incompetence. Committee needs to feel the pain before seeing the solution

---

### Slide 3 — Why Segmentation Matters
- **Main visual:** Three use-case cards (Surgical Planning, Treatment Monitoring, Research) + scope boundary card
- **Visual type:** Comparison card
- **Required image:** None (text cards sufficient)
- **Placeholder instruction:** Optional: `PLACEHOLDER: clinical_use_cases.png` — three-panel illustration showing kidney tumor in surgical, monitoring, and research contexts
- **Why:** Connects technical segmentation output to patient care decisions. Committee must understand what segmentation is FOR before seeing how it works

---

### Slide 4 — Project Objective
- **Main visual:** Input/Output cards + user badges + safety badges
- **Visual type:** Comparison card (Input vs Output)
- **Required image:** CT volume input placeholder
- **Placeholder instruction:** `PLACEHOLDER: ct_volume_input.png` — axial slice of abdominal CT with kidney visible. Can extract from KiTS23 case (case_00000.nii.gz, mid-slice) using ITK-SNAP or Python matplotlib. Save as PNG in public/images/
- **Why:** Defines exactly what goes in, what comes out, who uses it, and what it does NOT do. Prevents scope-creep questions later

---

### Slide 5 — Dataset: KiTS23
- **Main visual:** Dataset metric cards (489 cases, 3 classes, multi-center) + ChallengeCard for tumor/cyst merge
- **Visual type:** Metric card + challenge card
- **Required image:** KiTS23 dataset overview
- **Placeholder instruction:** `PLACEHOLDER: kits23_overview.png` — bar chart or donut showing class distribution (background, kidney, tumor/cyst), number of cases per center. Can generate from KiTS23 metadata using Python: `matplotlib` bar chart of cases per center, or pie chart of class voxel proportions. Save to public/images/kits23_overview.png
- **Why:** Establishes dataset credibility (public benchmark, multi-center) and honestly presents the merged tumor/cyst limitation upfront

---

### Slide 6 — Development Journey
- **Main visual:** 10-step pipeline (two columns of PipelineStep components)
- **Visual type:** Process timeline
- **Required image:** Development timeline
- **Placeholder instruction:** `PLACEHOLDER: development_timeline.png` — horizontal timeline with 10 phases, dates, and key decisions marked. Can create with Python matplotlib or draw.io. Alternative: use the PipelineStep Vue components already in the slide (no image needed)
- **Why:** Directly addresses mid-year feedback about documenting the process, not just results. Shows iterative engineering, not just final output

---

### Slide 7 — What We Built (System Pipeline)
- **Main visual:** 5-step horizontal pipeline: Input → Preprocess → Model → Inference → Post-process → Output
- **Visual type:** Diagram (process flow)
- **Required image:** System pipeline diagram
- **Placeholder instruction:** `PLACEHOLDER: system_pipeline.png` — horizontal flowchart with 5 boxes connected by arrows, each box with icon and label. Can create with draw.io, Excalidraw, or Python graphviz. Save to public/images/system_pipeline.png. Alternative: current HTML/CSS pipeline in slide is sufficient
- **Why:** Gives committee the 30-second mental model of the entire system before diving into details

---

### Slide 8 — Preprocessing Decisions
- **Main visual:** Two cards: HU Clipping [-200, 300] + Normalization formula + ChallengeCards for validation and consistency
- **Visual type:** Comparison card + challenge card
- **Required image:** Preprocessing workflow
- **Placeholder instruction:** `PLACEHOLDER: preprocessing_workflow.png` — before/after CT slice showing raw HU values vs clipped+normalized version. Can generate from KiTS23 data: load .nii with nibabel, show slice before and after clipping, save as side-by-side PNG with matplotlib
- **Why:** Shows preprocessing was a deliberate engineering decision, not arbitrary. Empirical range selection demonstrates rigor

---

### Slide 9 — Model Training Documentation
- **Main visual:** Experiment log structure (4 PipelineSteps) + architecture summary card
- **Visual type:** Process timeline + metric card
- **Required image:** None (text cards sufficient)
- **Placeholder instruction:** Optional: `PLACEHOLDER: training_curves.png` — loss/Dice curves over epochs from training log. Can generate if TensorBoard logs or CSV logs exist. If not, note as future documentation
- **Why:** Proves training was iterative and documented. Mid-year feedback required visible experiment log structure

---

### Slide 10 — 3D U-Net Architecture
- **Main visual:** Encoder-decoder diagram with skip connections + architecture detail cards
- **Visual type:** Diagram (neural network architecture)
- **Required image:** 3D U-Net architecture placeholder
- **Placeholder instruction:** `PLACEHOLDER: unet3d_architecture.png` — classic U-Net diagram with encoder (downsampling), bottleneck, decoder (upsampling), and skip connections. Can create with draw.io or PowerPoint. Use 3D convolution notation (3x3x3). Save to public/images/unet3d_architecture.png
- **Why:** Committee needs to see the model structure to understand how 3D context is captured across slices

---

### Slide 11 — Inference Pipeline
- **Main visual:** Three metric cards (Patch Size 64×192×192, Overlap 50%, TTA 8 flips) + two explanation cards
- **Visual type:** Metric card + diagram
- **Required image:** Sliding-window inference diagram
- **Placeholder instruction:** `PLACEHOLDER: sliding_window.png` — 2D illustration of sliding window patches over a CT volume with overlap shown. Can create with draw.io or Python matplotlib: draw a rectangle (volume) with overlapping smaller rectangles (patches) inside. Label overlap region. Save to public/images/sliding_window.png
- **Why:** Explains how full CT volumes are processed despite GPU memory limits. TTA justification shows awareness of orientation artifacts

---

### Slide 12 — Post-Processing
- **Main visual:** Two filter cards (Kidney <5000 voxels, Tumor <100 voxels) + design rationale blockquote
- **Visual type:** Comparison card
- **Required image:** Post-processing workflow
- **Placeholder instruction:** `PLACEHOLDER: postprocessing_workflow.png` — before/after segmentation showing blob removal. Can generate from inference output: show raw prediction mask vs filtered mask side-by-side. Use matplotlib with colored overlays on CT slice
- **Why:** Conservative thresholds demonstrate safety-first design: false positives acceptable, false negatives dangerous

---

### Slide 13 — Key Challenge: Tumor/Cyst
- **Main visual:** Two cards: Kidney (Favorable) vs Tumor/Cyst (Challenging) with bullet lists + detection vs segmentation callout
- **Visual type:** Comparison card
- **Required image:** Tumor/cyst challenge visual
- **Placeholder instruction:** `PLACEHOLDER: tumor_cyst_challenge.png` — CT slice showing tumor and cyst side-by-side with similar appearance. Can extract from KiTS23 cases that contain both tumor and cyst. Label each. Save to public/images/tumor_cyst_challenge.png
- **Why:** Honest presentation of the fundamental limitation. Committee will ask about this — slide pre-empts the question

---

### Slide 14 — Web Application
- **Main visual:** 4-step user flow (Upload → Process → Visualize → Review) + tech stack badges
- **Visual type:** Process timeline
- **Required image:** Web app screenshot placeholder
- **Placeholder instruction:** `PLACEHOLDER: webapp_screenshot.png` — screenshot of the NephroVision web interface showing 3D visualization viewer with kidney/tumor mesh. Take actual screenshot from running web app. If app not running, create mockup in Figma or PowerPoint showing: file upload area, 3D viewer with colored kidney/tumor mesh, volume statistics panel. Save to public/images/webapp_screenshot.png
- **Why:** Shows the system is not just a model — it is a usable tool. Committee values end-to-end delivery

---

### Slide 15 — Validation Setup
- **Main visual:** Three metric cards (64 cases, 3 metrics, 2 thresholds) + evaluation criteria list
- **Visual type:** Metric card
- **Required image:** None (text cards sufficient)
- **Placeholder instruction:** None
- **Why:** Defines evaluation methodology before showing results. Committee needs to know how success was measured

---

### Slide 16 — Results
- **Main visual:** Six metric cards (Kidney Dice, Tumor Dice, Mean Dice, HD95 Kidney, HD95 Tumor, Tumor Detection) with color coding + summary line
- **Visual type:** Metric card
- **Required image:** Results metric cards (already in slide as Vue components)
- **Placeholder instruction:** None — MetricCard Vue components display the data. Optional: `PLACEHOLDER: results_chart.png` — bar chart comparing kidney vs tumor Dice with error bars. Can generate with matplotlib from KNOWN_METRICS.md values
- **Why:** The money slide. All numbers from KNOWN_METRICS.md, color-coded for instant comprehension

---

### Slide 17 — Target vs. Achieved
- **Main visual:** Acceptance criteria table with 6 rows (Criterion, Target, Achieved, Status) — all PASS
- **Visual type:** Comparison table
- **Required image:** Acceptance criteria cards/table (already in slide as HTML table)
- **Placeholder instruction:** None — table is rendered from HTML. Optional: convert to visual cards with green PASS badges for more visual impact
- **Why:** Proves all project acceptance criteria were met. Important for graduation committee — shows project succeeded by its own definition

---

### Slide 18 — Failure Analysis & Limitations
- **Main visual:** Three ChallengeCards (Boundary Leakage, Small Lesion Sensitivity, Cyst/Tumor Confusion) + Domain Shift critical card + remaining limitations list
- **Visual type:** Comparison card (challenge categories)
- **Required image:** Failure analysis categories
- **Placeholder instruction:** `PLACEHOLDER: failure_cases.png` — 2-3 CT slices showing failed segmentation cases (boundary leakage, small lesion miss, cyst/tumor confusion). Can extract from inference outputs on test set. Label each failure mode. Save to public/images/failure_cases.png
- **Why:** Honest failure analysis is critical for academic credibility. Committee respects transparency over perfection claims

---

### Slide 19 — Safety & IEC 62304
- **Main visual:** Classification card (IEC 62304 Class B, SaMD, Decision-support) + danger badges + "Why Class B" cards + scope clarification
- **Visual type:** Comparison card + safety badges
- **Required image:** IEC 62304 safety positioning
- **Placeholder instruction:** `PLACEHOLDER: iec62304_positioning.png` — diagram showing IEC 62304 class hierarchy (Class A → B → C) with NephroVision positioned at Class B. Can create with draw.io or PowerPoint. Show decision-support vs autonomous axis. Save to public/images/iec62304_positioning.png
- **Why:** Demonstrates regulatory awareness without claiming compliance. Critical distinction: following principles ≠ FDA clearance

---

### Slide 20 — Future Work
- **Main visual:** Priority-grouped list (High: boundary losses, external validation, nnU-Net; Medium: prospective eval, uncertainty, regulatory docs) + "none implemented yet" disclaimer
- **Visual type:** Process timeline (roadmap)
- **Required image:** Future work roadmap
- **Placeholder instruction:** `PLACEHOLDER: future_work_roadmap.png` — horizontal roadmap timeline with 3 phases (Short-term, Medium-term, Long-term) and milestones. Can create with draw.io or PowerPoint. Color-code by priority. Save to public/images/future_work_roadmap.png
- **Why:** Shows forward-thinking without over-promising. External validation as highest priority demonstrates scientific maturity

---

### Slide 21 — Final Takeaway
- **Main visual:** Three metric cards (Kidney Dice 0.9307, Tumor Detection 100%, Tumor Dice 0.6558) + key message + thank you badge
- **Visual type:** Metric card
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** End strong. Three numbers + one message. Committee remembers the last slide most

---

## Additional Candidate Slides (22+)

> Add any of these to expand the deck. Remove the ones you do not need.

### Slide 22 — Related Work (Literature Review)
- **Main visual:** Comparison table of related systems (U-Net, nnU-Net, KiTS challenge winners) vs NephroVision
- **Visual type:** Comparison table
- **Required image:** None
- **Placeholder instruction:** None — table can be built from literature review in IEEE report Section 3
- **Why:** Shows awareness of prior art. Committee expects literature context in a graduation defense

---

### Slide 23 — Anatomy & Pathology Background
- **Main visual:** CT slice with labeled kidney anatomy (cortex, medulla, renal pelvis) + tumor types (RCC, cyst, angiomyolipoma)
- **Visual type:** Diagram (anatomical illustration)
- **Required image:** `PLACEHOLDER: kidney_anatomy.png` — labeled CT slice or anatomical illustration showing kidney cross-section with tumor types
- **Placeholder instruction:** Use medical anatomy illustration from textbook or create labeled diagram from KiTS23 CT slice. Save to public/images/kidney_anatomy.png
- **Why:** Non-medical committee members need basic anatomy context to understand segmentation challenges

---

### Slide 24 — GPU Memory Constraint (Engineering Challenge)
- **Main visual:** Diagram showing CT volume size (512×512×N slices) vs GPU memory (VRAM) → why patches are needed
- **Visual type:** Diagram (memory vs volume comparison)
- **Required image:** `PLACEHOLDER: gpu_memory_diagram.png` — bar chart comparing full CT volume size (GB) vs available GPU VRAM (GB)
- **Placeholder instruction:** Create with matplotlib: show typical CT volume (512×512×300 = ~150MB float32) vs GPU VRAM (e.g., 8GB, 11GB, 24GB). Show why full-volume inference is infeasible. Save to public/images/gpu_memory_diagram.png
- **Why:** Explains the engineering constraint that drove the sliding-window design decision. Shows problem-solving, not just using existing code

---

### Slide 25 — Class Imbalance Challenge
- **Main visual:** Bar chart showing voxel counts: Background (99%+), Kidney (<1%), Tumor (<0.1%)
- **Visual type:** Diagram (class distribution chart)
- **Required image:** `PLACEHOLDER: class_imbalance.png` — bar chart or pie chart showing voxel proportions per class
- **Placeholder instruction:** Generate from KiTS23 data: count voxels per class across all training cases, create log-scale bar chart with matplotlib. Save to public/images/class_imbalance.png
- **Why:** Visual proof of why segmentation is hard — tumor is a tiny fraction of the volume. Justifies loss function and post-processing choices

---

### Slide 26 — Loss Function Selection
- **Main visual:** Comparison of Dice Loss vs Cross-Entropy vs Combined + formula cards
- **Visual type:** Comparison card
- **Required image:** None
- **Placeholder instruction:** Optional: `PLACEHOLDER: loss_comparison.png` — plot showing training curves for different loss functions (if experiment log has this data)
- **Why:** Shows the loss function was a deliberate choice, not default. Dice loss addresses class imbalance directly

---

### Slide 27 — Training Infrastructure
- **Main visual:** Cards showing GPU model, training time, framework (PyTorch), batch size, epochs
- **Visual type:** Metric card
- **Required image:** None (or `PLACEHOLDER: gpu_photo.png` — photo of the GPU/workstation used)
- **Placeholder instruction:** Fill with actual hardware specs from experiment log. If no photo, text cards are sufficient
- **Why:** Committee may ask about compute resources. Shows the project was constrained by real hardware

---

### Slide 28 — Data Augmentation Strategy
- **Main visual:** Grid showing augmentation types (flip, rotate, scale, intensity shift) applied to training data
- **Visual type:** Diagram (augmentation examples grid)
- **Required image:** `PLACEHOLDER: augmentation_grid.png` — 2×4 grid showing original CT slice + 7 augmented versions (flipped, rotated, scaled, intensity-shifted, noisy, elastic, cropped)
- **Placeholder instruction:** Generate from KiTS23 case with Python: apply each augmentation, save as grid PNG with matplotlib. Save to public/images/augmentation_grid.png
- **Why:** Shows awareness of data augmentation best practices for medical imaging

---

### Slide 29 — Experiment Log Summary
- **Main visual:** Table of experiment runs (EXP-001 through EXP-006) with columns: ID, Date, Key Change, Val Dice, Decision
- **Visual type:** Comparison table
- **Required image:** None
- **Placeholder instruction:** Fill from actual experiment_log.md in 07_development_documentation/. If experiments not documented, show as TODO table
- **Why:** Direct evidence of iterative development. Committee wants to see what was tried, what worked, what was discarded

---

### Slide 30 — Segmentation Quality Visualization
- **Main visual:** Side-by-side CT slices: ground truth mask vs predicted mask for 3 cases (best, average, worst)
- **Visual type:** Comparison card (visual examples)
- **Required image:** `PLACEHOLDER: segmentation_comparison.png` — 3×3 grid: Row 1 = best case, Row 2 = average case, Row 3 = worst case. Columns: CT slice, ground truth overlay, prediction overlay
- **Placeholder instruction:** Generate from test set results: load CT + ground truth + prediction, create overlay with matplotlib (green=TP, red=FP, blue=FN). Save to public/images/segmentation_comparison.png
- **Why:** Visual proof of segmentation quality. Shows both successes and honest failures. Much more convincing than just Dice numbers

---

### Slide 31 — 3D Visualization Demo
- **Main visual:** Screenshot or GIF of the 3D viewer rotating kidney + tumor mesh
- **Visual type:** Screenshot / animation
- **Required image:** `PLACEHOLDER: 3d_viewer_demo.gif` or `3d_viewer_screenshot.png` — 3D mesh visualization from the web app
- **Placeholder instruction:** Run web app, load a test case, screenshot the 3D viewer. Or record 5-second GIF of rotating mesh. Save to public/images/3d_viewer_demo.gif
- **Why:** Visual impact of seeing a 3D kidney with tumor is powerful. Shows the system produces actionable 3D output, not just 2D slices

---

### Slide 32 — Uncertainty & Error Bounds
- **Main visual:** CT slice with confidence heatmap showing where the model is uncertain (boundary regions)
- **Visual type:** Diagram (uncertainty map)
- **Required image:** `PLACEHOLDER: uncertainty_map.png` — CT slice with overlay showing prediction uncertainty (red=high uncertainty, blue=low)
- **Placeholder instruction:** If TTA flip variance was computed, generate uncertainty map from TTA disagreement. If not, create synthetic illustration showing high uncertainty at tumor boundaries. Save to public/images/uncertainty_map.png
- **Why:** Shows awareness that segmentation is not binary correct/incorrect. Uncertainty quantification is advanced topic for graduation level

---

### Slide 33 — Comparison with KiTS23 Challenge Top Solutions
- **Main visual:** Bar chart comparing NephroVision Dice vs top-3 KiTS23 challenge methods
- **Visual type:** Comparison table / bar chart
- **Required image:** `PLACEHOLDER: kits23_comparison.png` — grouped bar chart: Kidney Dice and Tumor Dice for NephroVision vs top-3 challenge entries
- **Placeholder instruction:** Get top-3 results from KiTS23 challenge paper (Helmberger et al. 2023). Create grouped bar chart with matplotlib. CRITICAL: label NephroVision as "project subset" not "challenge submission". Save to public/images/kits23_comparison.png
- **Why:** Contextualizes results. Shows where NephroVision stands relative to state-of-the-art. Must NOT claim leaderboard ranking

---

### Slide 34 — Reproducibility
- **Main visual:** Checklist card showing: code repository, trained weights, config files, environment file, experiment log, documentation
- **Visual type:** Metric card (checklist)
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** Reproducibility is a core scientific requirement. Shows the project meets engineering documentation standards

---

### Slide 35 — Team Contributions
- **Main visual:** Table showing each team member and their primary responsibilities
- **Visual type:** Comparison table
- **Required image:** None (or team photo `PLACEHOLDER: team_photo.png`)
- **Placeholder instruction:** Fill with actual role assignments. Optional team photo if available
- **Why:** Committee may ask about individual contributions. Transparency about division of work

---

### Slide 36 — Project Timeline & Milestones
- **Main visual:** Gantt chart or horizontal timeline showing project phases with dates
- **Visual type:** Process timeline
- **Required image:** `PLACEHOLDER: project_gantt.png` — Gantt chart with phases: literature review, dataset exploration, preprocessing, model training, inference, web app, evaluation, documentation
- **Placeholder instruction:** Create with Python matplotlib or draw.io. Fill dates from actual project timeline in 07_development_documentation/development_timeline.md. Save to public/images/project_gantt.png
- **Why:** Shows project management discipline. Committee values evidence of planned, not ad-hoc, development

---

### Slide 37 — Cost & Resource Analysis
- **Main visual:** Cards showing compute hours, storage, software costs (all $0 for academic project)
- **Visual type:** Metric card
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** Shows fiscal responsibility. Important if committee includes industry members

---

### Slide 38 — Ethical Considerations
- **Main visual:** Cards covering: patient data anonymity (KiTS23 is de-identified), IRB status, bias considerations, clinical deployment ethics
- **Visual type:** Comparison card
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** Medical AI projects must address ethics. Committee will ask about patient data and bias

---

### Slide 39 — References
- **Main visual:** Key citations list (KiTS23 paper, U-Net paper, IEC 62304 standard, nnU-Net, etc.)
- **Visual type:** Text (reference list)
- **Required image:** None
- **Placeholder instruction:** Pull from refs.bib in 02_ieee_report/. Show top 8-10 most cited references in the presentation
- **Why:** Academic standard. Committee expects citations for claims made during the defense

---

### Slide 40 — Q&A
- **Main visual:** "Questions?" with key metrics summary as backdrop + contact info
- **Visual type:** Text
- **Required image:** None
- **Placeholder instruction:** None
- **Why:** Dedicated Q&A slide signals the presentation is over and invites discussion

---

## Required Visuals Coverage Checklist

| Required Visual | Slide(s) | Status |
|---|---|---|
| Clinical problem illustration | Slide 2 | Placeholder needed |
| CT volume input placeholder | Slide 4 | Placeholder needed |
| KiTS23 dataset overview | Slide 5 | Placeholder needed |
| Development timeline | Slide 6 | Vue components sufficient |
| System pipeline diagram | Slide 7 | Vue components sufficient |
| Preprocessing workflow | Slide 8 | Placeholder needed |
| 3D U-Net architecture placeholder | Slide 10 | Placeholder needed |
| Sliding-window inference diagram | Slide 11 | Placeholder needed |
| Post-processing workflow | Slide 12 | Placeholder needed |
| Web app screenshot placeholder | Slide 14 | Placeholder needed |
| Results metric cards | Slide 16 | Vue components done |
| Acceptance criteria cards/table | Slide 17 | HTML table done |
| Tumor/cyst challenge visual | Slide 13 | Placeholder needed |
| Failure analysis categories | Slide 18 | Vue components sufficient |
| IEC 62304 safety positioning | Slide 19 | Placeholder needed |
| Future work roadmap | Slide 20 | Placeholder needed |

---

## Image Generation Priority

### High Priority (must have for defense)
1. `ct_volume_input.png` — CT slice from KiTS23 (Slide 4)
2. `unet3d_architecture.png` — U-Net diagram (Slide 10)
3. `system_pipeline.png` — End-to-end flow (Slide 7)
4. `segmentation_comparison.png` — GT vs prediction (Slide 30)
5. `webapp_screenshot.png` — Web app interface (Slide 14)

### Medium Priority (nice to have)
6. `kits23_overview.png` — Dataset stats chart (Slide 5)
7. `preprocessing_workflow.png` — Before/after CT (Slide 8)
8. `sliding_window.png` — Patch overlap diagram (Slide 11)
9. `tumor_cyst_challenge.png` — CT with tumor+cyst (Slide 13)
10. `results_chart.png` — Dice bar chart (Slide 16)

### Low Priority (optional)
11. `failure_cases.png` — Failed segmentation examples (Slide 18)
12. `iec62304_positioning.png` — Class hierarchy (Slide 19)
13. `future_work_roadmap.png` — Roadmap timeline (Slide 20)
14. `class_imbalance.png` — Voxel distribution (Slide 25)
15. `augmentation_grid.png` — Augmentation examples (Slide 28)
16. `project_gantt.png` — Project timeline (Slide 36)

---

## Image Generation Instructions

### Can generate from code (Python + nibabel + matplotlib):
- `ct_volume_input.png` — Load KiTS23 .nii, plot mid-slice
- `kits23_overview.png` — Parse metadata, bar chart
- `preprocessing_workflow.png` — Load CT, apply clip+norm, side-by-side
- `segmentation_comparison.png` — Load CT+GT+pred, overlay colors
- `class_imbalance.png` — Count voxels per class, bar chart
- `results_chart.png` — Bar chart from KNOWN_METRICS.md
- `gpu_memory_diagram.png` — Bar chart, volume vs VRAM
- `augmentation_grid.png` — Apply augmentations, grid plot

### Must create with drawing tool (draw.io / PowerPoint / Figma):
- `unet3d_architecture.png` — Network diagram
- `system_pipeline.png` — Flowchart
- `sliding_window.png` — Patch overlap illustration
- `iec62304_positioning.png` — Class hierarchy
- `future_work_roadmap.png` — Roadmap timeline
- `project_gantt.png` — Gantt chart

### Must capture from running system:
- `webapp_screenshot.png` — Browser screenshot
- `3d_viewer_demo.gif` — Screen recording

---

## Rules Followed
- No screenshots invented — all marked as PLACEHOLDER with clear instructions
- Placeholders clearly labeled with `PLACEHOLDER: filename.png` format
- Visuals that can be generated from code have Python instructions
- Visuals that need drawing tools are identified
- All 16 required visuals covered across existing + candidate slides
- Extra slides added beyond 21 for committee questions and depth
