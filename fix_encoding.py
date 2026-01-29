import os

file_path = 'index.html'

# Map of double-encoded sequences (latin-1 decoded UTF-8) to correct char
# We construct them by encoding the correct char to utf-8, then decoding as latin-1 to get the Mojibake
replacements = {
    'é': 'Ã©',
    'è': 'Ã¨',
    'ê': 'Ãª',
    'â': 'Ã¢',
    'ô': 'Ã´',
    'î': 'Ã®',
    'ï': 'Ã¯',
    'û': 'Ã»',
    'ù': 'Ã¹',
    'ç': 'Ã§',
    'œ': 'Å“',
    'É': 'Ã‰',
    'À': 'Ã€',
    'à': 'Ã ', # Ã + nbsp
    "'": 'â€™',
    "–": 'â€“',
    "•": 'â€¢',
    # Add more if needed
}

# The file uses UTF-8, but contains the mojibake CHARACTERS.
# So we read as UTF-8, find 'Ã©', and replace with 'é'.

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for correct, bad in replacements.items():
    if bad in content:
        c = content.count(bad)
        count += c
        content = content.replace(bad, correct)
        print(f"Replaced {c} occurrences of {bad} with {correct}")

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Total replacements: {count}")
else:
    print("No encoding artifacts found to replace.")
