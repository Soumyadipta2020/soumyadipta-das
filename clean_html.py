import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove <div class="role-details-container"> and its closing tag
# We can do this safely by finding all <div class="role-details-container">
html = re.sub(r'[ \t]*<div class="role-details-container">\n', '', html)

# Remove the closing </div> that comes right after the button
html = re.sub(r'([ \t]*<button class="toggle-details.*?</button>\n)[ \t]*</div>\n', r'\1', html)

# Remove the button entirely
html = re.sub(r'[ \t]*<button class="toggle-details.*?</button>\n', '', html)

# Remove the second <ul> tag <ul class="role-details collapsible is-collapsed"> and combine it
# We want to replace "</ul>\n<ul class="role-details collapsible is-collapsed">" with ""
html = re.sub(r'[ \t]*</ul>\n[ \t]*<ul class="role-details collapsible is-collapsed">\n', '\n', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML cleaned")
