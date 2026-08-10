import re

with open('knee-positioner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Knee Positioner from nav
content = re.sub(r'<a href="#"[^>]*>Knee Positioner</a>\s*', '', content)

# But we should highlight "Products" instead!
content = re.sub(r'<a href="products\.html" class="text-slate-500 hover:text-medical-600 font-semibold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Products</a>', r'<a href="products.html" class="text-slate-900 font-bold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Products</a>', content)
content = re.sub(r'<a href="products\.html" class="text-sm font-semibold text-slate-600 uppercase tracking-widest">Products</a>', r'<a href="products.html" class="text-sm font-bold text-slate-900 uppercase tracking-widest">Products</a>', content)

with open('knee-positioner.html', 'w', encoding='utf-8') as f:
    f.write(content)

