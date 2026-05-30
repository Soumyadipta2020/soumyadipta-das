import os
import re
import mammoth

SOURCE_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Travel"
TARGET_DIR = r"c:\Users\user\OneDrive\Coding\Profile\soumyadipta-das\blogs"
LINKS_FILE = r"c:\Users\user\OneDrive\Coding\Profile\soumyadipta-das\travel_blogs_links.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Soumyadipta Das</title>
  <link rel="stylesheet" href="../styles.css" />
  <style>
    body {{
      background-color: #070a0f;
      color: #e2e8f0;
      font-family: 'Inter', sans-serif;
      line-height: 1.6;
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
    }}
    .blog-header {{
      margin-bottom: 2rem;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 1rem;
    }}
    .blog-header h1 {{
      font-size: 2.5rem;
      color: #f8fafc;
      margin-bottom: 0.5rem;
    }}
    .blog-content h1, .blog-content h2, .blog-content h3 {{
      color: #f8fafc;
      margin-top: 2rem;
      margin-bottom: 1rem;
    }}
    .blog-content p {{
      color: #94a3b8;
      margin-bottom: 1.5rem;
      font-size: 1.1rem;
    }}
    .blog-content ul, .blog-content ol {{
      color: #94a3b8;
      margin-bottom: 1.5rem;
      padding-left: 1.5rem;
      font-size: 1.1rem;
    }}
    .blog-content li {{
      margin-bottom: 0.5rem;
    }}
    .blog-content img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 1.5rem 0;
    }}
    .back-link {{
      display: inline-block;
      margin-bottom: 2rem;
      color: #38bdf8;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s ease;
    }}
    .back-link:hover {{
      color: #7dd3fc;
    }}
  </style>
</head>
<body>
  <a href="../index.html#writing" class="back-link">← Back to Portfolio</a>
  <article class="blog-header">
    <h1>{title}</h1>
  </article>
  <div class="blog-content">
    {content}
  </div>
</body>
</html>
"""

def slugify(value):
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    links_html = []
    
    # Process files
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.docx'):
            continue
        # Skip temp files like "~Unsupervised..."
        if filename.startswith('~'):
            continue
            
        filepath = os.path.join(SOURCE_DIR, filename)
        title = filename[:-5]
        slug = slugify(title)
        
        print(f"Processing: {title}")
        
        with open(filepath, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value
            messages = result.messages
            for msg in messages:
                print(f"[{title}] {msg}")
                
        full_html = HTML_TEMPLATE.format(title=title, content=html_content)
        
        output_filepath = os.path.join(TARGET_DIR, f"{slug}.html")
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(full_html)
            
        links_html.append(f'              <a href="blogs/{slug}.html" target="_blank">{title}</a>')
        
    # Write links snippet
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(links_html))
        
    print(f"Processed {len(links_html)} blogs. Links saved to {LINKS_FILE}")

if __name__ == "__main__":
    main()
