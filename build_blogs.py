import os
import re
import datetime
import mammoth

DS_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Statistics and Probability"
TRAVEL_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Travel"
PROJECT_DIR = r"c:\Users\user\OneDrive\Coding\Profile\soumyadipta-das"
TARGET_DIR = os.path.join(PROJECT_DIR, "blogs")
INDEX_FILE = os.path.join(PROJECT_DIR, "index.html")

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
      padding: 40px 20px;
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
      margin-top: 2rem;
      margin-bottom: 0.75rem;
      font-weight: 700;
      line-height: 1.2;
    }}
    .blog-article-body p {{
      color: #c6d4e5;
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 1rem;
    }}
    .blog-article-body p:empty {{
      display: none;
    }}
    .blog-article-body ul, .blog-article-body ol {{
      margin-top: 0;
      margin-bottom: 1rem;
      padding-left: 1.5rem;
    }}
    .blog-article-body li {{
      color: #c6d4e5;
      font-size: 1.1rem;
      line-height: 1.7;
      margin-bottom: 0.5rem;
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
    
    <div class="blog-article-head">
      <p>{category}</p>
      <h3>{title}</h3>
    </div>
    
    <div class="blog-article-body">
      {content}
    </div>
    
  </div>
</body>
</html>
"""

def slugify(value):
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def get_ds_tags(title):
    tags = []
    title_lower = title.lower()
    if 'ai' in title_lower or 'artificial intelligence' in title_lower: tags.append('ai')
    if 'machine learning' in title_lower or 'ml' in title_lower: tags.append('machine-learning')
    if 'time series' in title_lower: tags.append('time-series')
    if 'statistics' in title_lower or 'statistical' in title_lower or 'statistic' in title_lower: tags.append('statistics')
    if 'forecasting' in title_lower: tags.append('forecasting')
    if 'generative ai' in title_lower or 'genai' in title_lower or 'llm' in title_lower or 'large language models' in title_lower: tags.append('generative-ai')
    if 'clustering' in title_lower: tags.append('clustering')
    if 'deep learning' in title_lower or 'neural network' in title_lower: tags.append('deep-learning')
    if not tags: tags.append('data-science')
    return tags

def get_travel_tags(title):
    tags = []
    title_lower = title.lower()
    if 'himalaya' in title_lower: tags.append('himalayas')
    if 'ladakh' in title_lower: tags.append('ladakh')
    if 'uttarakhand' in title_lower or 'kedarnath' in title_lower or 'tungnath' in title_lower or 'rudranath' in title_lower or 'gomukh' in title_lower or 'kalpeshwar' in title_lower or 'madhyamaheshwar' in title_lower: tags.append('uttarakhand')
    if 'himachal' in title_lower or 'spiti' in title_lower or 'sangla' in title_lower or 'kinnaur' in title_lower or 'chitkul' in title_lower or 'kalpa' in title_lower or 'sarahan' in title_lower: tags.append('himachal')
    if 'spiritual' in title_lower or 'shiva' in title_lower or 'kailash' in title_lower or 'monastery' in title_lower or 'gompa' in title_lower: tags.append('spiritual')
    if not tags: tags.append('travel')
    return tags

def extract_real_title(html_content, fallback_title):
    match = re.search(r'^(<p>|<h1>)(.*?)(</p>|</h1>)', html_content)
    if match:
        extracted_html = match.group(2)
        # Strip internal tags
        clean_text = re.sub(r'<[^>]+>', '', extracted_html).strip()
        # Decode some basic entities if needed, though mammoth mostly outputs UTF-8 chars directly
        clean_text = clean_text.replace('&nbsp;', ' ')
        
        # Check if it's likely a title
        if clean_text and len(clean_text) < 150 and not clean_text.startswith('Welcome to'):
            new_content = html_content[match.end():].strip()
            return clean_text, new_content
            
    return fallback_title, html_content

def process_directory(source_dir, category_name, tag_func, list_id):
    files_metadata = []
    
    for filename in os.listdir(source_dir):
        if not filename.endswith('.docx') or filename.startswith('~'):
            continue
            
        filepath = os.path.join(source_dir, filename)
        fallback_title = filename[:-5]
        slug = slugify(fallback_title)
        mtime = os.path.getmtime(filepath)
        dt = datetime.datetime.fromtimestamp(mtime)
        date_str = dt.strftime('%b %Y')
        
        with open(filepath, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            raw_html = result.value
            
        real_title, cleaned_html = extract_real_title(raw_html, fallback_title)
        
        full_html = HTML_TEMPLATE.format(
            title=real_title, 
            content=cleaned_html,
            category=category_name
        )
        
        output_filepath = os.path.join(TARGET_DIR, f"{slug}.html")
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(full_html)
            
        files_metadata.append({
            'title': real_title,
            'slug': slug,
            'mtime': mtime,
            'date_str': date_str,
            'tags': tag_func(fallback_title) # use fallback title for tags to match previous behavior
        })
        
    # Generate Links HTML
    files_metadata.sort(key=lambda x: x['mtime'], reverse=True)
    
    all_tags = set()
    for file in files_metadata:
        all_tags.update(file['tags'])
    all_tags = sorted(list(all_tags))
    
    html = []
    html.append(f'<div class="blog-filters" id="filter-{list_id}">')
    html.append('  <button class="tag-chip active" data-tag="all">All</button>')
    for tag in all_tags:
        display_name = tag.replace('-', ' ').title()
        if display_name == 'Ai': display_name = 'AI'
        if display_name == 'Ml': display_name = 'ML'
        if display_name == 'Llm': display_name = 'LLM'
        html.append(f'  <button class="tag-chip" data-tag="{tag}">{display_name}</button>')
    html.append('</div>')
    
    html.append(f'<div class="blog-list" id="list-{list_id}" style="max-height: 500px; overflow-y: auto; display: flex; flex-direction: column; gap: 0.5rem; padding-right: 1rem;">')
    for file in files_metadata:
        tags_str = ' '.join(file['tags'])
        html.append(f'  <a href="blogs/{file["slug"]}.html" target="_blank" class="blog-item" data-tags="{tags_str}">')
        html.append(f'    <span class="blog-title">{file["title"]}</span>')
        html.append(f'    <span class="blog-date">{file["date_str"]}</span>')
        html.append(f'  </a>')
    html.append('</div>')
    
    return '\n'.join(html), len(files_metadata)

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    print("Extracting real titles and rebuilding everything...")
    ds_html, ds_count = process_directory(DS_DIR, "Data Science & AI", get_ds_tags, 'ds')
    travel_html, travel_count = process_directory(TRAVEL_DIR, "Travel & Exploration", get_travel_tags, 'travel')
    
    # Update index.html
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    ds_pattern = r'(<h3>Data Science Blogs</h3>\s*</div>\n).*?(?=^\s*</article>)'
    travel_pattern = r'(<h3>Travel Blogs</h3>\s*</div>\n).*?(?=^\s*</article>)'

    content = re.sub(ds_pattern, r'\1' + ds_html + '\n', content, flags=re.DOTALL | re.MULTILINE)
    content = re.sub(travel_pattern, r'\1' + travel_html + '\n', content, flags=re.DOTALL | re.MULTILINE)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Finished! Processed {ds_count} Data Science blogs and {travel_count} Travel blogs.")
    print("index.html has been updated with real titles.")

if __name__ == "__main__":
    main()
