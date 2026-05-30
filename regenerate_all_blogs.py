import os
import re
import mammoth

DS_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Statistics and Probability"
TRAVEL_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Travel"
TARGET_DIR = r"c:\Users\user\OneDrive\Coding\Profile\soumyadipta-das\blogs"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Soumyadipta Das</title>
  <link rel="stylesheet" href="../styles.css" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;800&display=swap" rel="stylesheet">
  <style>
    body {{
      background-color: #05080d;
      font-family: 'Inter', sans-serif;
      padding: 40px 20px;
      margin: 0;
    }}
    .blog-container {{
      max-width: 900px;
      margin: 0 auto;
    }}
    .back-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 2rem;
      color: #11baf2;
      text-decoration: none;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 800;
      text-transform: uppercase;
      transition: color 0.2s ease;
    }}
    .back-link:hover {{
      color: #4387ff;
    }}
    
    /* Enhance mammoth output to match theme */
    .blog-article-body h1, .blog-article-body h2, .blog-article-body h3 {{
      color: #e6f1ff;
      margin-top: 2.5rem;
      margin-bottom: 1rem;
      font-weight: 700;
      line-height: 1.2;
    }}
    .blog-article-body p, .blog-article-body li {{
      color: #c6d4e5;
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 1.5rem;
    }}
    .blog-article-body img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 2rem 0;
      border: 1px solid rgba(41, 56, 75, 0.72);
      box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
    }}
    .blog-article-body a {{
      color: #11baf2;
      text-decoration: none;
    }}
    .blog-article-body a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="blog-container">
    <a href="../index.html#writing" class="back-link">← Back to Portfolio</a>
    
    <div class="blog-reader">
      <div class="blog-article-head">
        <p>{category}</p>
        <h3>{title}</h3>
      </div>
      
      <div class="blog-article-body">
        {content}
      </div>
    </div>
    
  </div>
</body>
</html>
"""

def slugify(value):
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def process_directory(source_dir, category_name):
    count = 0
    for filename in os.listdir(source_dir):
        if not filename.endswith('.docx') or filename.startswith('~'):
            continue
            
        filepath = os.path.join(source_dir, filename)
        title = filename[:-5]
        slug = slugify(title)
        
        with open(filepath, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value
                
        full_html = HTML_TEMPLATE.format(
            title=title, 
            content=html_content,
            category=category_name
        )
        
        output_filepath = os.path.join(TARGET_DIR, f"{slug}.html")
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(full_html)
        count += 1
    return count

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    print("Regenerating all blogs with new theme...")
    ds_count = process_directory(DS_DIR, "Data Science & AI")
    travel_count = process_directory(TRAVEL_DIR, "Travel & Exploration")
    
    print(f"Finished! Regenerated {ds_count} Data Science blogs and {travel_count} Travel blogs.")

if __name__ == "__main__":
    main()
