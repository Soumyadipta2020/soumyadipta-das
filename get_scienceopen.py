import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://www.scienceopen.com/', 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
)
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    svgs = re.findall(r'<svg[^>]*>.*?</svg>', html, re.DOTALL | re.IGNORECASE)
    for svg in svgs:
        if 'science' in svg.lower() or 'logo' in svg.lower():
            print("FOUND SVG:", svg)
except Exception as e:
    print(e)
