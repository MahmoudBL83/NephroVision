#!/usr/bin/env python3
"""Fix all SectionTitle numbers for 50 slides."""

import re

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slides and their positions
slide_matches = list(re.finditer(r'SLIDE (\d+)[a-z]*:', content))

fixes = 0
for i, match in enumerate(slide_matches):
    slide_num = int(match.group(1))
    
    # Determine correct section
    if 1 <= slide_num <= 5:
        sec_num = "01"
    elif 6 <= slide_num <= 9:
        sec_num = "02"
    elif 10 <= slide_num <= 12:
        sec_num = "03"
    elif 13 <= slide_num <= 14:
        sec_num = "04"
    elif 15 <= slide_num <= 17:
        sec_num = "05"
    elif 18 <= slide_num <= 23:
        sec_num = "06"
    elif 24 <= slide_num <= 28:
        sec_num = "07"
    elif 29 <= slide_num <= 31:
        sec_num = "08"
    elif 32 <= slide_num <= 39:
        sec_num = "09"
    elif 40 <= slide_num <= 44:
        sec_num = "10"
    elif 45 <= slide_num <= 50:
        sec_num = "11"
    else:
        continue
    
    # Find the SectionTitle in this slide
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

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {fixes} section numbers")
