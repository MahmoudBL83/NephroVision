import re

path = r'C:\mahmoud\graduation\nephrovision-final-defense\03_final_presentation\slidev\slides.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
i = 0
while i < len(lines):
    result.append(lines[i])
    # If current line is an HTML tag line (starts with < after stripping)
    curr_stripped = lines[i].strip()
    if curr_stripped.startswith('<') and not curr_stripped.startswith('<!--'):
        # Check if next line is blank and line after is also an HTML tag
        if i + 2 < len(lines) and lines[i+1].strip() == '':
            next_stripped = lines[i+2].strip()
            if next_stripped.startswith('<') and not next_stripped.startswith('<!--'):
                # Skip the blank line - it's inside an HTML block
                i += 1
                continue
    i += 1

text = ''.join(result)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Removed {len(lines) - len(result)} blank lines between HTML tags')
