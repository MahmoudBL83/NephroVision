import re

path = r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix: remove blank lines between consecutive HTML tags inside the same block
# Pattern: </div>\n\n\s*<div  → </div>\n\s*<div
# This preserves blank lines between top-level slide sections

def fix_html_blocks(content):
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        result.append(lines[i])
        # Check if current line ends with </div> and next lines are blank then another tag
        if i + 2 < len(lines) and lines[i].strip().endswith('</div>'):
            # Check if next line is blank or whitespace-only
            if lines[i+1].strip() == '' and lines[i+2].strip().startswith('<'):
                # Skip the blank line
                i += 1
                continue
        i += 1
    return '\n'.join(result)

text = fix_html_blocks(text)

# Also fix: blank lines between <div...> and its first child
def fix_html_blocks2(content):
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        result.append(lines[i])
        # Check if current line starts with <div and next line is blank
        if i + 2 < len(lines) and lines[i].strip().startswith('<div') and '>' in lines[i]:
            if lines[i+1].strip() == '' and lines[i+2].strip().startswith('<'):
                # Skip the blank line if it's inside an HTML block (indented or child tag)
                i += 1
                continue
        i += 1
    return '\n'.join(result)

text = fix_html_blocks2(text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed HTML blank lines')
