import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Truncate at the first occurrence of '.back-to-top svg {'
# Then add the correct closing to it.
idx = content.find('.back-to-top svg {')
if idx != -1:
    content = content[:idx] + ".back-to-top svg {\n  width: 24px;\n  height: 24px;\n}\n\n/* Project Cards Enhancements */\n.impact-badge {\n  display: inline-block;\n  background: rgba(255, 255, 255, 0.1);\n  color: var(--text-primary);\n  padding: 0.25rem 0.5rem;\n  border-radius: 4px;\n  font-size: 0.75rem;\n  font-weight: 600;\n  margin-bottom: 0.75rem;\n  border: 1px solid var(--border-color);\n}\n.project-links {\n  display: flex;\n  gap: 1rem;\n  margin-top: auto;\n  align-items: center;\n  flex-wrap: wrap;\n}\n.project-card a {\n  display: flex;\n  align-items: center;\n  gap: 0.25rem;\n  font-size: 0.875rem;\n  color: var(--text-secondary);\n  text-decoration: none;\n  transition: color 0.2s;\n}\n.project-card a:hover {\n  color: var(--text-primary);\n}\n.demo-link {\n  color: var(--accent-blue) !important;\n  font-weight: 500;\n}\n.demo-link:hover {\n  color: #fff !important;\n}\n"

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed styles.css")
