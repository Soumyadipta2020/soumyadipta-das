import re

# Remove demo links from HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'[ \t]*<a href="[^"]+" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>\n?', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Remove demo link CSS from styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'\.demo-link \{[^}]+\}\n?', '', css)
css = re.sub(r'\.demo-link:hover \{[^}]+\}\n?', '', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Demo links removed.")
