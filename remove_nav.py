import glob
import re

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The desktop link looks like:
    # <a href="knee-positioner.html" class="text-slate-500 hover:text-medical-600 font-semibold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Knee Positioner</a>
    # or similar
    content = re.sub(r'<a href="knee-positioner\.html"[^>]*>Knee Positioner</a>', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

