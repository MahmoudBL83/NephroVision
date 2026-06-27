#!/usr/bin/env python3
"""Fix section numbers after slide rearrangement"""

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Define section mapping: slide number range -> section number and name
sections = [
    (1, 5, "01", "Introduction"),
    (6, 9, "02", "Dataset"),
    (10, 12, "03", "Background"),
    (13, 14, "04", "Pipeline Overview"),
    (15, 17, "05", "Preprocessing"),
    (18, 25, "06", "Model"),
    (26, 30, "07", "Inference"),
    (31, 33, "08", "Challenges"),
    (34, 41, "09", "Results"),
    (42, 46, "10", "Limitations & Future"),
    (47, 50, "11", "Closing"),
]

# Find all slides and their positions
slide_matches = list(re.finditer(r'SLIDE (\d+)[a-z]*:', content))

fixes = 0
for i, match in enumerate(slide_matches):
    slide_num = int(match.group(1))
    # Find which section this slide belongs to
    for start, end, sec_num, sec_name in sections:
        if start <= slide_num <= end:
            # Find the SectionTitle in this slide
            # Look for <SectionTitle number="..." after this match
            search_start = match.end()
            search_end = slide_matches[i+1].start() if i+1 < len(slide_matches) else len(content)
            slide_text = content[search_start:search_end]
            
            # Replace section number
            new_text = re.sub(
                r'<SectionTitle number="\d+"',
                f'<SectionTitle number="{sec_num}"',
                slide_text
            )
            if new_text != slide_text:
                content = content[:search_start] + new_text + content[search_end:]
                fixes += 1
            break

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {fixes} section numbers")
