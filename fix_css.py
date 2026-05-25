import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will find the malformed block:
# .back-to-top:focus-visible {\n  transform: translateY(-3px);\n  box-shadow: 0 8px 24px rgba(255, 122, 26, 0.4);\n\n\n/* Scroll Reveal Animations */
malformed_block = """.back-to-top:hover,
.back-to-top:focus-visible {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(255, 122, 26, 0.4);


/* Scroll Reveal Animations */"""

fixed_block = """.back-to-top:hover,
.back-to-top:focus-visible {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(255, 122, 26, 0.4);
}

/* Scroll Reveal Animations */"""

css = css.replace(malformed_block, fixed_block)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS fixed")
