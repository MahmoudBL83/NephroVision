# Figures

Place all report figures here.

## Required Figures for IEEE Report

| Filename | Description | Used In Section |
|----------|-------------|-----------------|
| `fig_pipeline.pdf` | System pipeline overview (NIfTI -> Preprocessing -> 3D U-Net -> Inference -> Post-processing -> Output) | 07_methodology.tex |
| `fig_architecture.pdf` | 3D U-Net architecture diagram (encoder-decoder with skip connections) | 07_methodology.tex |
| `fig_inference.pdf` | Inference workflow (sliding window, TTA, fusion) | 08_training_and_inference.tex |
| `fig_webapp.pdf` | Web application screenshot (3D viewer + stats panel) | 09_software_system_design.tex |
| `fig_results.pdf` | Results summary (Dice comparison bar chart, detection rate, example overlays) | 10_evaluation_results.tex |

## Format Guidelines

- **Vector preferred:** PDF, EPS, SVG
- **Raster acceptable:** PNG (300+ dpi), TIFF
- **Naming:** `fig_<section>_<number>_<topic>.<ext>`
- **Width:** Design for single-column (~8.5 cm) or double-column (~17.5 cm) placement
- **Font size:** Minimum 8 pt after scaling; ensure readability in two-column layout
- **Color:** Use colorblind-safe palettes. Consider print-friendly grayscale compatibility.

## Placeholder Status

All figures are currently placeholders in the LaTeX source. Uncomment the `\includegraphics` line and replace the `\fbox` placeholder when the final figure is ready.
