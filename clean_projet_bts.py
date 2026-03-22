import re

with open('projet-bts.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make all href="#..." point to "index.html#..." EXCEPT href="#projet-bts"
def repl_href(m):
    anchor = m.group(1)
    if anchor == 'projet-bts':
        return 'href="#projet-bts"' # we are already on projet-bts.html
    elif anchor == 'missions':
        return 'href="index.html#missions"'
    else:
        return f'href="index.html#{anchor}"'

html = re.sub(r'href="#([a-zA-Z0-9_-]+)"', repl_href, html)

# Also fix the desktop links that might have been changed to href="projet-bts.html" in the header
# Although wait, since we copied index.html, those are already 'projet-bts.html' and should probably stay #projet-bts
html = html.replace('href="projet-bts.html"', 'href="#projet-bts"')

# Find <main> and </main>
match = re.search(r'<main>.*?</main>', html, flags=re.DOTALL)
if match:
    main_content = match.group(0)
    # Extract only the #projet-bts section
    bts_match = re.search(r'(<!-- Projet BTS -->\s*<section class="portfolio" id="projet-bts">.*?</section>)', main_content, flags=re.DOTALL)
    if bts_match:
        bts_section = bts_match.group(1)
        # Create a new main block with some margin to compensate for hero section removal
        new_main = '<main style="padding-top: 100px;">\n' + bts_section + '\n    </main>'
        html = html[:match.start()] + new_main + html[match.end():]

# change title
html = html.replace('<title>Kevin Ates - Portfolio BTS SIO SISR</title>', '<title>Kevin Ates - Projet BTS</title>')

with open('projet-bts.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done extracting projet-bts.html!")
