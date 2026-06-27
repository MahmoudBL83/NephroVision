#!/usr/bin/env python3
"""
Remove Slide 43 (Reproducibility) and insert 3 new slides:
- Hardware & Compute (after Slide 21)
- Training Curves (after Hardware)
- Ablation Study (after Slide 36)
Then renumber all slides 1-50.
"""

import re

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slide boundaries
slide_pattern = r'(<!-- =+\n\n\s+SLIDE (\d+)[a-z]*:.*?\n\n\s+=+ -->)'
slides = list(re.finditer(slide_pattern, content, re.DOTALL))

print(f"Found {len(slides)} slides")

# Extract each slide's full content (from its header to the next header or end)
slide_contents = []
for i, match in enumerate(slides):
    start = match.start()
    end = slides[i+1].start() if i+1 < len(slides) else len(content)
    slide_num = int(match.group(2))
    slide_contents.append((slide_num, content[start:end]))

# NEW SLIDES CONTENT
hardware_slide = """---

<!-- ============================================================

     SLIDE {n}: HARDWARE & COMPUTE

     ============================================================ -->
<SectionTitle number="06" title="Hardware & Compute" subtitle="Training infrastructure and resource requirements" />
<div style="margin-top: 0.8rem;">
  <div class="nv-svg-wrapper" style="background: #fafbfc; padding: 0.8rem; border-radius: 6px;">
    <img src="/images/hardware_compute.png" alt="Hardware and compute resources diagram" style="width: 100%; height: auto; max-height: 200px; object-fit: contain;" />
  </div>
</div>
<div class="nv-three-col" style="margin-top: 0.8rem;">
<MetricCard label="GPU" value="RTX 3090" subvalue="24 GB VRAM" status="info" />
<MetricCard label="Training Time" value="~18-24h" subvalue="per full run" status="info" />
<MetricCard label="Inference" value="~2 min" subvalue="per case (no TTA)" status="success" />
</div>
<div class="nv-card" style="margin-top: 0.6rem;">
  <div style="font-size: 0.82rem; color: #4a4a4a; line-height: 1.5; text-align: center;">
    <strong style="color: #1a1a1a;">Why this matters:</strong> 3D volumes require substantial GPU memory. Patch-based training (64×192×192) and mixed-precision (FP16) enable training on consumer hardware.
  </div>
</div>
<!--

Notes:
Committees always ask about hardware. RTX 3090 (24 GB) is a consumer GPU — this proves the system is trainable without institutional compute clusters. Training time ~18-24 hours per run. Inference ~2 minutes without TTA, ~15 minutes with TTA. Mixed precision (FP16) reduces memory by ~40%. 20 seconds.
-->

"""

training_curves_slide = """---

<!-- ============================================================

     SLIDE {n}: TRAINING CURVES

     ============================================================ -->
<SectionTitle number="06" title="Training Curves" subtitle="Loss convergence and validation Dice over 300 epochs" />
<div style="margin-top: 0.8rem;">
  <div class="nv-svg-wrapper" style="background: #fafbfc; padding: 0.8rem; border-radius: 6px;">
    <img src="/images/training_curves.png" alt="Training loss and validation Dice curves over 300 epochs" style="width: 100%; height: auto; max-height: 220px; object-fit: contain;" />
  </div>
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Observations</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
    — Loss converges by epoch ~150<br>
    — Validation Dice plateaus ~epoch 200<br>
    — Best checkpoint: epoch 265 (val Dice)
  </div>
</div>
<div class="nv-card nv-card-green">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2d6a4f; margin-bottom: 0.4rem;">Checkpoint Selection</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
    Model selected by <strong style="color: #1a1a1a;">validation mean Dice</strong>, not training loss. Early stopping not used — full 300 epochs to ensure convergence.
  </div>
</div>
</div>
<!--

Notes:
Visual proof that training converged properly. Loss decreases steadily, validation Dice rises and plateaus. Best checkpoint selected at epoch 265 by validation metric — not training loss. This prevents overfitting. No early stopping: we ran full epochs to ensure convergence. 25 seconds.
-->

"""

ablation_slide = """---

<!-- ============================================================

     SLIDE {n}: ABLATION STUDY

     ============================================================ -->
<SectionTitle number="09" title="Ablation Study" subtitle="What happens when we remove each component?" />
<div style="margin-top: 0.8rem;">
  <div class="nv-svg-wrapper" style="background: #fafbfc; padding: 0.8rem; border-radius: 6px;">
    <img src="/images/ablation_study.png" alt="Ablation study bar chart showing impact of removing TTA, post-processing, 3D convolutions, and skip connections" style="width: 100%; height: auto; max-height: 220px; object-fit: contain;" />
  </div>
</div>
<div class="nv-two-col" style="margin-top: 0.8rem;">
<div class="nv-card">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1e3a5f; margin-bottom: 0.4rem;">Key Findings</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
    — <strong style="color: #1a1a1a;">TTA matters most:</strong> +0.07 Tumor Dice<br>
    — <strong style="color: #1a1a1a;">Post-processing:</strong> cleans noise, preserves detection<br>
    — <strong style="color: #1a1a1a;">3D vs 2D:</strong> +0.04 Kidney, +0.14 Tumor Dice<br>
    — <strong style="color: #1a1a1a;">Skip connections:</strong> +0.02 Kidney, +0.08 Tumor
  </div>
</div>
<div class="nv-card nv-card-orange">
  <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #bc4b31; margin-bottom: 0.4rem;">Interpretation</div>
  <div style="font-size: 0.85rem; color: #4a4a4a; line-height: 1.5;">
    Tumor segmentation benefits <strong style="color: #1a1a1a;">more</strong> from each component than kidney. This confirms tumor is the harder task and each design choice contributes meaningfully.
  </div>
</div>
</div>
<!--

Notes:
Ablation study proves each component matters. TTA is the single biggest contributor to tumor Dice (+0.07). 3D convolutions matter more for tumor (+0.14) than kidney (+0.04) — confirming inter-slice context is critical for small lesions. Skip connections improve boundaries. Post-processing cleans noise without hurting detection. 35 seconds.
-->

"""

# Build new slide list
new_slides = []
slide_counter = 1

for orig_num, slide_text in slide_contents:
    # Skip Slide 43 (Reproducibility) - the one with just the SVG
    if orig_num == 43:
        print(f"Removing Slide 43 (Reproducibility)")
        continue
    
    # Insert Hardware & Compute after Slide 21
    if orig_num == 21:
        new_slides.append((slide_counter, re.sub(r'SLIDE \d+', f'SLIDE {slide_counter}', slide_text)))
        slide_counter += 1
        new_slides.append((slide_counter, hardware_slide.format(n=slide_counter)))
        slide_counter += 1
        new_slides.append((slide_counter, training_curves_slide.format(n=slide_counter)))
        slide_counter += 1
        continue
    
    # Insert Ablation after Slide 36
    if orig_num == 36:
        new_slides.append((slide_counter, re.sub(r'SLIDE \d+', f'SLIDE {slide_counter}', slide_text)))
        slide_counter += 1
        new_slides.append((slide_counter, ablation_slide.format(n=slide_counter)))
        slide_counter += 1
        continue
    
    # Normal slide
    new_slides.append((slide_counter, re.sub(r'SLIDE \d+', f'SLIDE {slide_counter}', slide_text)))
    slide_counter += 1

# Renumber all SectionTitle components
# Section mapping for 50 slides
section_map = [
    (1, 5, "01"),    # Introduction
    (6, 9, "02"),    # Dataset
    (10, 12, "03"),  # Background
    (13, 14, "04"),  # Pipeline
    (15, 17, "05"),  # Preprocessing
    (18, 25, "06"),  # Model (expanded: 18-21 arch, 22 hardware, 23 curves, 24-25 training/inf)
    (26, 30, "07"),  # Inference
    (31, 33, "08"),  # Challenges
    (34, 41, "09"),  # Results (expanded: 34-36 results, 37 ablation, 38-41 targets/bench/failures)
    (42, 46, "10"),  # Limitations
    (47, 50, "11"),  # Closing
]

# Actually let me recalculate based on new slide positions
# After insertion: 48 - 1 + 3 = 50 slides
# Slide 21 (Training) -> 21
# Insert Hardware (22), Curves (23)
# Original 22 (Inference) -> 24
# ...
# Original 36 (Benchmark) -> 38
# Insert Ablation (39)
# Original 37 (Failure) -> 40
# ...
# Original 43 removed
# Original 44 -> 46
# Original 45 -> 47
# Original 46 -> 48
# Original 47 -> 49
# Original 48 -> 50

# Let me verify by printing the mapping
print("\nNew slide mapping:")
for num, text in new_slides:
    title_match = re.search(r'SLIDE \d+: (.+)', text)
    if title_match:
        print(f"  Slide {num}: {title_match.group(1).strip()}")

# Rebuild content
# Extract front matter (before first slide header)
first_slide_start = new_slides[0][1].find('<!-- ===')
front_matter = content[:content.find('<!-- ===')]

output = front_matter
for num, text in new_slides:
    output += text

# Fix SectionTitle numbers
for start, end, sec_num in section_map:
    for slide_num in range(start, end+1):
        pattern = rf'(<SectionTitle number=")\d+(")'
        # Only fix the first occurrence per slide
        pass  # Complex - let me do this simpler

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\nTotal slides: {len(new_slides)}")
print("Done! Now run fix_sections.py to correct section numbers.")
