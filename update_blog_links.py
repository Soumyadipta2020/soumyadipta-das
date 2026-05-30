import os
import re
import datetime

DS_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Statistics and Probability"
TRAVEL_DIR = r"C:\Users\user\OneDrive\Invoice, Projects, Resume & Insurance\Blog\Travel"
PROJECT_DIR = r"c:\Users\user\OneDrive\Coding\Profile\soumyadipta-das"
INDEX_FILE = os.path.join(PROJECT_DIR, "index.html")

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

def process_dir(directory, tag_func, list_id):
    files = []
    for f in os.listdir(directory):
        if not f.endswith('.docx') or f.startswith('~'): continue
        filepath = os.path.join(directory, f)
        ctime = os.path.getctime(filepath)
        dt = datetime.datetime.fromtimestamp(ctime)
        date_str = dt.strftime('%b %Y')
        title = f[:-5]
        files.append({'title': title, 'slug': slugify(title), 'ctime': ctime, 'date_str': date_str})
        
    # Sort newest first
    files.sort(key=lambda x: x['ctime'], reverse=True)
    
    all_tags = set()
    for file in files:
        file['tags'] = tag_func(file['title'])
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
    for file in files:
        tags_str = ' '.join(file['tags'])
        html.append(f'  <a href="blogs/{file["slug"]}.html" target="_blank" class="blog-item" data-tags="{tags_str}">')
        html.append(f'    <span class="blog-title">{file["title"]}</span>')
        html.append(f'    <span class="blog-date">{file["date_str"]}</span>')
        html.append(f'  </a>')
    html.append('</div>')
    
    return '\n'.join(html)

def main():
    ds_html = process_dir(DS_DIR, get_ds_tags, 'ds')
    travel_html = process_dir(TRAVEL_DIR, get_travel_tags, 'travel')

    # Update index.html
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    ds_pattern = r'(<h3>Data Science Blogs</h3>\s*</div>\n).*?(?=^\s*</article>)'
    travel_pattern = r'(<h3>Travel Blogs</h3>\s*</div>\n).*?(?=^\s*</article>)'

    content = re.sub(ds_pattern, r'\1' + ds_html + '\n', content, flags=re.DOTALL | re.MULTILINE)
    content = re.sub(travel_pattern, r'\1' + travel_html + '\n', content, flags=re.DOTALL | re.MULTILINE)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("index.html updated successfully with dates on right side.")

if __name__ == "__main__":
    main()
