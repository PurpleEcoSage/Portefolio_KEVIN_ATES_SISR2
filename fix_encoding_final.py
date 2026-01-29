import os

file_path = 'index.html'

replacements = {
    'Ã ': 'à ',  # Ã followed by space
    'Ã\xa0': 'à ', # Ã followed by nbsp
    'âŒ': '❌',   # Likely broken cross icon
    'âœ': '✅',   # Likely broken check icon
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for bad, correct in replacements.items():
    if bad in content:
        c = content.count(bad)
        count += c
        content = content.replace(bad, correct)
        print(f"Replaced {c} occurrences of '{bad}' with '{correct}'")

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Total replacements: {count}")
else:
    print("No encoding artifacts found to replace.")
