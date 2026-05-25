import re

clean_grid = """          <div class="project-grid">
            <article class="project-card reveal-up">
              <div class="project-icon blue"><i data-lucide="sparkles"></i></div>
              <p>Python + PyShiny</p>
              <h3>AI Forecasting PyShiny</h3>
              <span class="impact-badge">Strategic Planning</span>
              <span>AI-integrated forecasting app for planning workflows, built around PyShiny and forecasting interactions.</span>
              <div class="project-meta">
                <span>Python</span>
                <span>Shiny</span>
                <span>Forecasting</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/forecasting_tool_pyshiny" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://github.com/Soumyadipta2020/forecasting_tool_pyshiny" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
            <article class="project-card reveal-up">
              <div class="project-icon teal"><i data-lucide="activity"></i></div>
              <p>R Shiny + AI</p>
              <h3>AI Forecasting Tool</h3>
              <span class="impact-badge">Forecasting Workflow</span>
              <span>Forecasting app for time-series and non-time-series data, combining visualization, modeling, and AI support.</span>
              <div class="project-meta">
                <span>R</span>
                <span>Shiny</span>
                <span>Time-Series</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/forecasting_tool" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://soumyadipta2020.shinyapps.io/forecasting_tool/" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
            <article class="project-card reveal-up">
              <div class="project-icon gold"><i data-lucide="bot"></i></div>
              <p>R + AI</p>
              <h3>Multimodal AI Chatbot</h3>
              <span class="impact-badge">AI Assistant</span>
              <span>R-based chatbot project exploring multimodal AI workflows with Shiny, JavaScript, and Hugging Face integration.</span>
              <div class="project-meta">
                <span>R</span>
                <span>Shiny</span>
                <span>NLP</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/Chatbot_with_R" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://github.com/Soumyadipta2020/Chatbot_with_R" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
            <article class="project-card reveal-up">
              <div class="project-icon red"><i data-lucide="brain"></i></div>
              <p>Python + LangChain</p>
              <h3>AI Agent Beer Production</h3>
              <span class="impact-badge">Conversational AI</span>
              <span>Intelligent conversational AI agent built to discuss, query, and analyze monthly beer production data in Austria.</span>
              <div class="project-meta">
                <span>Python</span>
                <span>AI Agent</span>
                <span>LangChain</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/ai_agent_beer_production" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://github.com/Soumyadipta2020/ai_agent_beer_production" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
            <article class="project-card reveal-up">
              <div class="project-icon violet"><i data-lucide="sliders"></i></div>
              <p>Python + Streamlit</p>
              <h3>Airport Resource Management</h3>
              <span class="impact-badge">Dashboard for Planners</span>
              <span>Interactive dashboard and resource planning application designed for airport operational planners.</span>
              <div class="project-meta">
                <span>Python</span>
                <span>Streamlit</span>
                <span>Planning</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/Airport-Resource-Management" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://github.com/Soumyadipta2020/Airport-Resource-Management" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
            <article class="project-card reveal-up">
              <div class="project-icon cyan"><i data-lucide="bar-chart-3"></i></div>
              <p>Streamlit + Dashboard</p>
              <h3>India Financial Growth</h3>
              <span class="impact-badge">Financial Analytics</span>
              <span>Interactive dashboard tracking India's financial growth indicators, built with Python, pandas, and Streamlit.</span>
              <div class="project-meta">
                <span>Python</span>
                <span>Streamlit</span>
                <span>Analytics</span>
              </div>
              <div class="project-links">
                <a href="https://github.com/Soumyadipta2020/financial_growth_app" target="_blank" rel="noopener">Open repo <i data-lucide="external-link"></i></a>
                <a href="https://github.com/Soumyadipta2020/financial_growth_app" class="demo-link" target="_blank" rel="noopener">Live Demo <i data-lucide="play"></i></a>
              </div>
            </article>
          </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start and end of project-grid
start_idx = html.find('<div class="project-grid">')
# The section ends with </section>\n\n        <section class="tab-panel" id="writing-panel"
end_marker = '        </section>\n\n        <section class="tab-panel" id="writing-panel"'
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + clean_grid + "\n" + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Project grid fixed successfully.")
else:
    print("Could not find start or end markers.")
