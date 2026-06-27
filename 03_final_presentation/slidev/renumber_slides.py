#!/usr/bin/env python3
"""Renumber all slides after inserting new one. 50->51 slides."""

import re

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slide headers and renumber sequentially
slide_headers = list(re.finditer(r'SLIDE (\d+)[a-z]*:', content))

fixes = 0
for i, match in enumerate(slide_headers):
    expected_num = i + 1
    actual_num = int(match.group(1))
    
    if actual_num != expected_num:
        # Replace the slide number
        old_text = match.group(0)
        new_text = old_text.replace(f'SLIDE {actual_num}', f'SLIDE {expected_num}')
        content = content[:match.start()] + new_text + content[match.end():]
        fixes += 1

# Now fix section numbers
slide_headers = list(re.finditer(r'SLIDE (\d+)[a-z]*:', content))

for i, match in enumerate(slide_headers):
    slide_num = i + 1
    search_start = match.end()
    search_end = slide_headers[i+1].start() if i+1 < len(slide_headers) else len(content)
    slide_text = content[search_start:search_end]
    
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
    elif 18 <= slide_num <= 24:
        sec_num = "06"
    elif 25 <= slide_num <= 29:
        sec_num = "07"
    elif 30 <= slide_num <= 32:
        sec_num = "08"
    elif 33 <= slide_num <= 40:
        sec_num = "09"
    elif 41 <= slide_num <= 45:
        sec_num = "10"
    elif 46 <= slide_num <= 51:
        sec_num = "11"
    else:
        continue
    
    new_text = re.sub(
        r'<SectionTitle number="\d+"',
        f'<SectionTitle number="{sec_num}"',
        slide_text
    )
    if new_text != slide_text:
        content = content[:search_start] + new_text + content[search_end:]

with open(r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Renumbered {fixes} slide headers")
print(f"Total slides: {len(slide_headers)}")
