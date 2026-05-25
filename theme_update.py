import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace variables
css = css.replace('--bg: #070a0f;', '--bg: #0a192f;')
css = css.replace('--bg-soft: #0c121b;', '--bg-soft: #112240;')
css = css.replace('--surface: #121a26;', '--surface: #172a45;')
css = css.replace('--surface-2: #172233;', '--surface-2: #1e3352;')
css = css.replace('--surface-3: #1d2a3a;', '--surface-3: #233b5c;')

# Replace orange usage with blue
css = css.replace('var(--orange)', 'var(--blue)')

# Save back
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated CSS theme")
