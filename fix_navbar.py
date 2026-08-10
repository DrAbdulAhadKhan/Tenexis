import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the navbar block
    # We want to specifically replace max-w-7xl in the navbar's first div.
    # Alternatively, we can just find id="navbar" and replace the next max-w-7xl
    def replacer(match):
        nav_part = match.group(1)
        # replace max-w-7xl with max-w-[1920px] in this block
        new_nav = nav_part.replace('max-w-7xl', 'max-w-[1920px] 2xl:px-16')
        return new_nav + match.group(2)

    new_content = re.sub(r'(<nav[^>]*id="navbar"[^>]*>.*?<div class="[^"]*)max-w-7xl([^"]*">)', 
                         r'\1max-w-[1920px] 2xl:px-16\2', content, flags=re.DOTALL)
    
    # Also fix header in booking.html which is <header class="...">
    new_content = re.sub(r'(<header[^>]*>.*?<div class="[^"]*)max-w-7xl([^"]*">)', 
                         r'\1max-w-[1920px] 2xl:px-16\2', new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

