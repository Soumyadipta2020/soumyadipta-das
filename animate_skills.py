import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add animation CSS
css_animation = """
@keyframes fillBar {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.skill-meter div span {
  display: block;
  height: 100%;
  background: linear-gradient(90deg, var(--teal), var(--blue));
  transform-origin: left;
  transform: scaleX(0);
}

.reveal-up.is-visible .skill-meter div span {
  animation: fillBar 1.5s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
"""

# Replace the existing .skill-meter div span block
css = re.sub(r'\.skill-meter div span \{[^}]+\}', css_animation, css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Skills graph animated")
