import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fonts display swap (already has display=swap in my previous regex? Let's check original)
# wait, original already has &display=swap. Let's just make sure.

# 2. SEO Meta tags
content = re.sub(r'<meta property="og:image" content="https://lh3.googleusercontent.com/.*?" />', '<meta property="og:image" content="https://soumyadipta2020.github.io/soumyadipta-das/hero-bg.webp" />', content)
content = re.sub(r'<meta name="twitter:image" content="https://lh3.googleusercontent.com/.*?" />', '<meta name="twitter:image" content="https://soumyadipta2020.github.io/soumyadipta-das/hero-bg.webp" />', content)
content = re.sub(r'<link rel="icon"', '<meta property="og:url" content="https://soumyadipta2020.github.io/soumyadipta-das/" />\n    <link rel="canonical" href="https://soumyadipta2020.github.io/soumyadipta-das/" />\n    <link rel="icon"', content, count=1)
content = content.replace('"url": "https://sites.google.com/view/soumyadipta-das"', '"url": "https://soumyadipta2020.github.io/soumyadipta-das/"')

# 3. Hero image
content = re.sub(r'style="--hero-image: url\(\'https://lh3.googleusercontent.com/.*?\'\);', 'style="--hero-image: url(\'hero-bg.webp\');', content)

# 4. Hero buttons (Add Resume)
hero_btns_replacement = '''              <a class="button button-primary" href="#projects" data-tab-target="projects">
                <i data-lucide="line-chart"></i>
                View Projects
              </a>
              <a class="button" href="mailto:soumyadipta_das@consultant.com">
                <i data-lucide="mail"></i>
                Contact
              </a>
              <a class="button" href="resume.pdf" target="_blank" rel="noopener">
                <i data-lucide="download"></i>
                Resume
              </a>'''
content = content.replace('''              <a class="button button-primary" href="#projects" data-tab-target="projects">
                <i data-lucide="line-chart"></i>
                View Projects
              </a>
              <a class="button" href="mailto:soumyadipta_das@consultant.com">
                <i data-lucide="mail"></i>
                Contact
              </a>''', hero_btns_replacement)

# 5. Experience Collapsibles
def collapse_role(match):
    full_ul = match.group(0)
    lis = re.findall(r'<li>.*?</li>', full_ul, flags=re.DOTALL)
    if len(lis) <= 2:
        return full_ul
    visible_lis = ''.join(lis[:2])
    hidden_lis = ''.join(lis[2:])
    return f'''<div class="role-details-container">
                <ul class="role-details">
                  {visible_lis}
                </ul>
                <ul class="role-details collapsible is-collapsed">
                  {hidden_lis}
                </ul>
                <button class="toggle-details button button-ghost button-sm">View Details</button>
              </div>'''

content = re.sub(r'<ul class="role-details">.*?</ul>', collapse_role, content, flags=re.DOTALL)

# 6. Projects updates
# Map project titles to impact labels and live demo links
project_updates = {
    'AI Forecasting PyShiny': {'impact': 'Strategic Planning', 'demo': 'https://github.com/Soumyadipta2020/forecasting_tool_pyshiny'},
    'AI Forecasting Tool': {'impact': 'Forecasting Workflow', 'demo': 'https://soumyadipta2020.shinyapps.io/forecasting_tool/'},
    'Multimodal AI Chatbot': {'impact': 'AI Assistant', 'demo': 'https://github.com/Soumyadipta2020/Chatbot_with_R'},
    'AI Agent Beer Production': {'impact': 'Conversational AI', 'demo': 'https://github.com/Soumyadipta2020/ai_agent_beer_production'},
    'Airport Resource Management': {'impact': 'Dashboard for Planners', 'demo': 'https://github.com/Soumyadipta2020/Airport-Resource-Management'},
    'India Financial Growth': {'impact': 'Financial Analytics', 'demo': 'https://github.com/Soumyadipta2020/financial_growth_app'}
}

for title, data in project_updates.items():
    impact = data['impact']
    demo = data['demo']
    
    # Add impact badge after <h3>
    content = re.sub(
        f'(<h3>{title}</h3>)',
        f'\\1\\n              <span class="impact-badge">{impact}</span>',
        content
    )
    
    # Add live demo link
    repo_link_pattern = re.compile(f'<a href="[^"]+" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>')
    
    def repl_links(match):
        repo_link = match.group(0)
        demo_link = f'<a href="{demo}" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>'
        return f'<div class="project-links">{repo_link}\\n{demo_link}</div>'
    
    # wait, this pattern will replace all of them if not careful, I need to do it per project block.
    
def replace_project_block(match):
    block = match.group(0)
    for title, data in project_updates.items():
        if f'<h3>{title}</h3>' in block:
            impact = data['impact']
            demo = data['demo']
            block = block.replace(f'<h3>{title}</h3>', f'<h3>{title}</h3>\\n              <span class="impact-badge">{impact}</span>')
            block = re.sub(r'<a href="([^"]+)" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>', 
                           r'<div class="project-links">\\n                <a href="\1" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>\\n                <a href="' + demo + r'" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>\\n              </div>', block)
    return block

content = re.sub(r'<article class="project-card reveal-up">.*?</article>', replace_project_block, content, flags=re.DOTALL)

# 7. Add Contact Section
contact_section = '''
      <section class="contact-section reveal-up" aria-label="Contact">
        <div class="contact-inner">
          <h2>Let's Connect</h2>
          <p>Open to high-impact conversations, consulting, or full-time opportunities in Analytics and AI.</p>
          <div class="contact-actions">
            <a class="button button-primary" href="mailto:soumyadipta_das@consultant.com">
              <i data-lucide="mail"></i> Email Me
            </a>
            <a class="button" href="https://www.linkedin.com/in/soumyadipta-das/" target="_blank" rel="noopener">
              <i data-lucide="linkedin"></i> LinkedIn
            </a>
            <a class="button button-ghost" href="resume.pdf" target="_blank" rel="noopener">
              <i data-lucide="download"></i> Download Resume
            </a>
          </div>
        </div>
      </section>
'''
content = content.replace('    </main>', f'{contact_section}    </main>')

# 8. Lazy load images
content = content.replace('<img src="https://www.google.com/', '<img loading="lazy" src="https://www.google.com/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
