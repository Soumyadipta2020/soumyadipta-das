import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add filters HTML right above <div class="project-grid">
filters_html = """          <div class="project-filters">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="python">Python</button>
            <button class="filter-btn" data-filter="r">R</button>
            <button class="filter-btn" data-filter="shiny">Shiny</button>
            <button class="filter-btn" data-filter="streamlit">Streamlit</button>
            <button class="filter-btn" data-filter="ai">AI</button>
          </div>
          
          <div class="project-grid">"""

html = html.replace('<div class="project-grid">', filters_html)

# Add data-categories to projects
html = html.replace('<h3>AI Forecasting PyShiny</h3>', '<h3 data-category="python shiny ai">AI Forecasting PyShiny</h3>')
html = html.replace('<h3>AI Forecasting Tool</h3>', '<h3 data-category="r shiny time-series ai">AI Forecasting Tool</h3>')
html = html.replace('<h3>Multimodal AI Chatbot</h3>', '<h3 data-category="r shiny nlp ai">Multimodal AI Chatbot</h3>')
html = html.replace('<h3>AI Agent Beer Production</h3>', '<h3 data-category="python ai">AI Agent Beer Production</h3>')
html = html.replace('<h3>Airport Resource Management</h3>', '<h3 data-category="python streamlit">Airport Resource Management</h3>')
html = html.replace('<h3>India Financial Growth</h3>', '<h3 data-category="python streamlit analytics">India Financial Growth</h3>')

# Actually, the data-category should be on the <article class="project-card reveal-up">
# Since it's hard to do a simple string replace for that, let's use regex
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>AI Forecasting PyShiny</h3>)',
    r'<article class="project-card reveal-up" data-category="python shiny ai">\n\1',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>AI Forecasting Tool</h3>)',
    r'<article class="project-card reveal-up" data-category="r shiny ai time-series">\n\1',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>Multimodal AI Chatbot</h3>)',
    r'<article class="project-card reveal-up" data-category="r shiny nlp ai">\n\1',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>AI Agent Beer Production</h3>)',
    r'<article class="project-card reveal-up" data-category="python ai langchain">\n\1',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>Airport Resource Management</h3>)',
    r'<article class="project-card reveal-up" data-category="python streamlit">\n\1',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<article class="project-card reveal-up">.*?<h3>India Financial Growth</h3>)',
    r'<article class="project-card reveal-up" data-category="python streamlit analytics">\n\1',
    html, flags=re.DOTALL
)
# Cleanup duplicate tags since I just prepended the <article...>
html = re.sub(r'<article class="project-card reveal-up" data-category="([^"]+)">\n\s*<article class="project-card reveal-up">', r'<article class="project-card reveal-up" data-category="\1">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add CSS for project-filters
css_filters = """
.project-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 32px;
  justify-content: center;
}

.filter-btn {
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--muted);
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  background: var(--surface-2);
  color: var(--text);
  border-color: var(--line-strong);
}

.filter-btn.active {
  background: rgba(67, 135, 255, 0.15); /* var(--blue) with opacity */
  color: var(--blue);
  border-color: var(--blue);
}

.project-card {
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.project-card.hidden {
  display: none;
}
"""

css += css_filters

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 3. Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_filters = """
// Project Filtering Logic
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove active class from all buttons
    filterBtns.forEach(b => b.classList.remove('active'));
    // Add active class to clicked button
    btn.classList.add('active');
    
    const filterValue = btn.getAttribute('data-filter');
    
    projectCards.forEach(card => {
      const categories = card.getAttribute('data-category') || '';
      if (filterValue === 'all' || categories.includes(filterValue)) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
});
"""
js += js_filters

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Filters injected")
