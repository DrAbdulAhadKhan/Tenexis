import re

with open('knee-positioner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Title
content = re.sub(r'<title>.*?</title>', '<title>Knee Positioner | Tenexis Medical</title>', content)

# Fix Nav active state
# Products is currently class="text-slate-900 font-bold ...", change to text-slate-500 font-semibold
# Knee Positioner is currently class="text-slate-500 hover:text-medical-600 font-semibold ...", change to text-slate-900 font-bold ...
# First fix Products
content = re.sub(
    r'<a href="#" class="text-slate-900 font-bold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Products</a>',
    r'<a href="products.html" class="text-slate-500 hover:text-medical-600 font-semibold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Products</a>',
    content
)
# Then fix Knee Positioner
content = re.sub(
    r'<a href="knee-positioner\.html" class="text-slate-500 hover:text-medical-600 font-semibold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Knee Positioner</a>',
    r'<a href="#" class="text-slate-900 font-bold text-xs tracking-widest uppercase transition-colors whitespace-nowrap">Knee Positioner</a>',
    content
)

# Replace the hero section text
content = re.sub(
    r'<h1 class="text-4xl lg:text-5xl lg:leading-[1\.1] font-display font-bold text-slate-900 mb-6">.*?</h1>',
    r'<h1 class="text-4xl lg:text-5xl lg:leading-[1.1] font-display font-bold text-slate-900 mb-6">Knee Positioner</h1>',
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'<p class="text-lg text-slate-600 font-light leading-relaxed mb-8 max-w-xl">.*?</p>',
    r'<p class="text-lg text-slate-600 font-light leading-relaxed mb-8 max-w-xl">Advanced knee positioners offering stability and precision.</p>',
    content,
    flags=re.DOTALL
)

# Clear the grid
# Find the start of the grid
grid_start = content.find('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10 items-stretch max-w-7xl mx-auto">')
if grid_start != -1:
    # Find the end of the pipeline grid, wait, we can just replace everything from grid_start to the end of pipeline section
    # Let's find <div class="mt-24 text-center mb-12"> (pipeline start)
    # The grid ends where pagination starts.
    # We can just use string search to find the end of the section
    section_end = content.find('</section>', grid_start)
    if section_end != -1:
        # replace everything from grid_start to section_end with an empty grid
        new_grid = """<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10 items-stretch max-w-7xl mx-auto" id="knee-positioner-grid">
                <!-- Content will be added here -->
            </div>
        </div>
        """
        content = content[:grid_start] + new_grid + content[section_end:]

with open('knee-positioner.html', 'w', encoding='utf-8') as f:
    f.write(content)

