# NephroVision Defense Presentation — Slidev

Premium medical AI presentation for final graduation defense.

## Quick Start

```bash
# Install dependencies
npm install

# Start dev server (opens browser)
npm run dev

# Export to PPTX (requires Chrome/Playwright)
npm run export:pptx

# Export to PDF (backup)
npm run export:pdf

# Export individual slides as PNG
npm run export:png
```

## Web Interface Features

### Export Button (Top-Right Corner)
A floating **Export** button appears in the top-right corner of the presentation:
- **PowerPoint (.pptx)** — Best for presenting
- **PDF Document** — Universal format
- **PNG Images** — Individual slide images

> **Note:** PPTX export requires Chrome/Playwright (~180MB). If disk space is limited, use the PDF export or present directly from the browser.

### Slide Navigator (Bottom Corners)
- **Bottom-left:** Slide counter (e.g., "12 / 48")
- **Bottom-right:** Navigation arrows (Previous / Next)
- **Bottom edge:** Progress bar showing talk completion

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `O` | Slide overview (grid) |
| `P` | Presenter mode |
| `F` | Fullscreen |
| `G` | Go to slide number |

## Project Structure

```
slidev/
├── package.json          # Dependencies + export scripts
├── slides.md             # 48 slides with speaker notes
├── style.css             # Academic gravitas theme
├── README.md             # This file
├── setup/
│   └── main.ts           # Global component injection
├── components/
│   ├── MetricCard.vue    # Color-coded metric display
│   ├── PipelineStep.vue  # Pipeline diagram step
│   ├── SectionTitle.vue  # Styled section header with number
│   ├── ChallengeCard.vue # Challenge/limitation card
│   ├── SafetyBadge.vue   # Safety status badge
│   └── ExportButton.vue  # Floating export menu
├── public/
│   └── images/           # SVG diagrams + visual assets
└── export/               # PPTX/PDF/PNG output
```

## Presentation Specs

- **Slides:** 48
- **Duration:** 18-22 minutes
- **Theme:** White background, Inter + Crimson Text fonts
- **Accent:** Deep navy (#1e3a5f)
- **Export:** PPTX (primary), PDF (backup), PNG (slides)

## Color System

| Color | Hex | Usage |
|-------|-----|-------|
| Navy | `#1e3a5f` | Primary accent, headings |
| Forest Green | `#2d6a4f` | Success, achieved, PASS |
| Terracotta | `#bc4b31` | Caution, limitations |
| Crimson | `#9b2c2c` | Critical risk, danger |
| White | `#ffffff` | Background |
| Gray | `#8a8a8a` | Secondary text |

## Visual Slide Categories

### Charts & Diagrams (20+ placeholders)
- Dataset distribution bar chart
- Results bar chart (Kidney vs Tumor)
- Metric box plots (per-case variability)
- Kidney-Tumor correlation scatter plot
- Detection grid (64 cases)
- Benchmark comparison bar chart
- Evolution timeline chart
- Voxel distribution pie chart
- HU histograms (before/after)
- Sliding window diagram
- TTA 8-flip grid
- Architecture layer diagram
- Skip connection diagram
- Failure case comparison figures
- Scanner variability diagram
- Performance timeline curve

### Before/After Comparisons
- Raw CT vs Normalized input
- Pre-processing effect masks
- Post-processing blob removal

## Speaker Notes

Each slide includes speaker notes in HTML comment blocks (`<!-- Notes ... -->`). View notes in Slidev presenter mode by pressing `P` during the dev server.

## Export Troubleshooting

### PPTX Export Fails (ENOSPC)
If you see `ENOSPC: no space left on device`:
1. Free up disk space (need ~200MB for Chromium)
2. Or use PDF export instead: `npm run export:pdf`
3. Or present directly from browser (no export needed)

### Playwright Not Installed
```bash
# Install Chromium for PPTX export
npm run install:chromium
# Or manually:
npx playwright install chromium
```

### Export Server Not Available
The web Export button tries to call the Slidev export API. If the server is not running:
- Use the CLI commands instead: `npm run export:pptx`
- Or export from the dev server terminal

## PPTX Export Notes

PPTX export renders each slide as an image and embeds in PowerPoint. Text is not editable in exported PPTX. For editable text, use the dev server and present from browser.
