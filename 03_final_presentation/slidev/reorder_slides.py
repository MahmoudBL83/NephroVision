#!/usr/bin/env python3
"""
Slide Rearrangement Script for NephroVision Defense Presentation
Extracts all slides, reorders them logically, and writes back.
"""

import re

# Read the file
with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into slides - each slide starts with <!-- ===...=== --> and ends before the next one
# But we need to handle the front matter (first --- block) separately

lines = content.split('\n')

# Find all slide boundaries
slide_boundaries = []
for i, line in enumerate(lines):
    if re.match(r'^<!-- =+\s*$', line) and i+2 < len(lines) and 'SLIDE' in lines[i+2]:
        slide_boundaries.append(i)

# Add end boundary
slide_boundaries.append(len(lines))

# Extract each slide
slides = {}
for idx in range(len(slide_boundaries)-1):
    start = slide_boundaries[idx]
    end = slide_boundaries[idx+1]
    slide_content = '\n'.join(lines[start:end])
    
    # Extract slide number and title
    match = re.search(r'SLIDE (\d+[a-z]*): (.+)', slide_content)
    if match:
        slide_num = match.group(1)
        slide_title = match.group(2).strip()
        slides[f"{slide_num}_{slide_title}"] = slide_content
        print(f"Extracted: Slide {slide_num} - {slide_title}")

print(f"\nTotal slides extracted: {len(slides)}")

# NEW ORDER - logical defense flow
new_order = [
    # === SECTION 1: INTRODUCTION (Slides 1-5) ===
    "1_TITLE",                           # Title slide
    "2_THE CLINICAL PROBLEM",            # Problem
    "3_WHY SEGMENTATION MATTERS",        # Why it matters
    "4_PROJECT OBJECTIVE",               # What we built
    "2b_CT IMAGING FUNDAMENTALS",        # CT basics
    
    # === SECTION 2: DATASET (Slides 6-9) ===
    "5_DATASET",                         # KiTS23 overview
    "5b_DATASET STATISTICS",             # Stats
    "5c_DATA SPLIT",                     # Split
    "23b_VOXEL DISTRIBUTION",            # Class imbalance visual
    
    # === SECTION 3: BACKGROUND (Slides 10-12) ===
    "22_RELATED WORK",                   # Related work
    "22b_EVOLUTION OF MEDICAL SEGMENTATION",  # Evolution
    "6_DEVELOPMENT JOURNEY",             # Our process
    
    # === SECTION 4: METHODOLOGY - Pipeline (Slides 13-15) ===
    "7_WHAT WE BUILT",                   # Overview
    "7b_PIPELINE ARCHITECTURE",          # System diagram
    
    # === SECTION 5: METHODOLOGY - Preprocessing (Slides 16-19) ===
    "8_PREPROCESSING DECISIONS",         # Decisions
    "8b_INTENSITY DISTRIBUTION",         # HU explanation
    "8c_PREPROCESSING IMPACT",           # Before/after
    
    # === SECTION 6: METHODOLOGY - Model (Slides 20-24) ===
    "10_3D U-NET ARCHITECTURE",          # Main architecture
    "10b_NETWORK ARCHITECTURE DETAIL",   # Layer details
    "10c_SKIP CONNECTIONS",              # Skip connections
    "9_MODEL TRAINING DOCUMENTATION",    # Training
    
    # === SECTION 7: METHODOLOGY - Inference (Slides 25-28) ===
    "11_INFERENCE PIPELINE",             # Overview
    "11b_SLIDING WINDOW VISUAL",         # Sliding window
    "11c_TEST-TIME AUGMENTATION",        # TTA
    "12_POST-PROCESSING",                # Post-processing
    "12b_POST-PROCESSING EFFECT",        # Effect
    
    # === SECTION 8: CHALLENGES (Slides 29-32) ===
    "23_CLASS IMBALANCE CHALLENGE",      # Class imbalance
    "13_KEY CHALLENGE",                  # Tumor/cyst
    "14_WEB APPLICATION",                # Web app
    
    # === SECTION 9: RESULTS (Slides 33-40) ===
    "15_VALIDATION SETUP",               # Setup
    "16_RESULTS",                        # Main results
    "16b_METRIC DISTRIBUTION",           # Distribution
    "16d_DETECTION PERFORMANCE",         # Detection
    "16c_KIDNEY-TUMOR CORRELATION",      # Correlation
    "17_TARGET VS ACHIEVED",             # Targets
    "20b_BENCHMARK COMPARISON",          # Benchmark
    
    # === SECTION 10: LIMITATIONS & SAFETY (Slides 41-45) ===
    "18_FAILURE ANALYSIS",               # Failures
    "18b_FAILURE CASE GALLERY",          # Gallery
    "18c_DOMAIN SHIFT RISK",             # Domain shift
    "19_SAFETY",                         # Safety
    "20_FUTURE WORK",                    # Future
    
    # === SECTION 11: CLOSING (Slides 46-48) ===
    "24_EXPERIMENT LOG",                 # Experiment log
    "25_REPRODUCIBILITY",                # Reproducibility
    "25b_REPRODUCIBILITY ARTIFACTS",     # Artifacts
    "26_ETHICAL CONSIDERATIONS",         # Ethics
    "21_FINAL TAKEAWAY",                 # Takeaway
    "27_KEY REFERENCES",                 # References
    "28_Q&A",                            # Q&A
]

# Rebuild
output_lines = []
# Add the front matter from the original
front_matter_end = slide_boundaries[0]
output_lines.extend(lines[0:front_matter_end])

# Add slides in new order
slide_counter = 1
for key_prefix in new_order:
    # Find matching slide
    matching_keys = [k for k in slides.keys() if k.startswith(key_prefix)]
    if matching_keys:
        key = matching_keys[0]
        slide_content = slides[key]
        # Update slide numbers in the content
        slide_content = re.sub(r'SLIDE \d+[a-z]*:', f'SLIDE {slide_counter}:', slide_content)
        output_lines.append(slide_content)
        slide_counter += 1
    else:
        print(f"WARNING: Could not find slide matching '{key_prefix}'")

# Write output
output = '\n'.join(output_lines)
with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\nReordered {slide_counter-1} slides successfully!")
print("New order:")
for i, key_prefix in enumerate(new_order, 1):
    matching = [k for k in slides.keys() if k.startswith(key_prefix)]
    if matching:
        title = matching[0].split('_', 1)[1]
        print(f"  {i}. {title}")
