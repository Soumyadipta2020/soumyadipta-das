with open("travel_blogs_links.html", "r", encoding="utf-8") as f:
    links = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

target = """              <a href="#writing/gomukh-tapovan-guide" data-blog-id="gomukh-tapovan-guide">
                Discovering the Mystical Beauty of Gomukh and Tapovan
              </a>
              <a href="#writing/kedarnath-guide" data-blog-id="kedarnath-guide">
                Kedarnath: Abode of Shiva in the Majestic Himalayas
              </a>
              <a href="#writing/tunganath-guide" data-blog-id="tunganath-guide">
                Exploring Tunganath: A Complete Travel Guide
              </a>
              <a href="#writing/rudranath-guide" data-blog-id="rudranath-guide">
                Rudranath: A Hidden Gem in the Himalayas
              </a>"""

# Wrap links in a scrollable div
links_html = f'''<div style="max-height: 500px; overflow-y: auto; display: flex; flex-direction: column; gap: 0.5rem; padding-right: 1rem;">
{links}
</div>'''

content = content.replace(target, links_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html for travel blogs")
