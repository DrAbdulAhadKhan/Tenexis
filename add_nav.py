import os
import glob
import re

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Knee Positioner" in content:
        continue
        
    # Find desktop quality link and insert before it
    # We can match `<a href="index.html#quality"` or `<a href="#quality"`
    content = re.sub(
        r'(<a href="(?:index\.html)?#quality" class="text-slate-500)',
        r'<a href="knee-positioner.html" class="text-slate-500 hover:text-medical-600 font-semibold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Knee Positioner</a>\n                    \1',
        content
    )
    
    # Mobile quality link
    content = re.sub(
        r'(<a href="(?:index\.html)?#quality" class="text-sm font-semibold)',
        r'<a href="knee-positioner.html" class="text-sm font-semibold text-slate-600 uppercase tracking-widest">Knee Positioner</a>\n                \1',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {file}")
