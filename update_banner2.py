import glob

for file in glob.glob("products*.html") + ['knee-positioner.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace bg-[#1a1a1a] with bg-black if necessary, or let's just make it bg-black
    content = content.replace(
        'class="overflow-hidden bg-[#1a1a1a] text-white py-2.5 whitespace-nowrap flex items-center border-b border-black relative z-30"',
        'class="overflow-hidden bg-[#1f1f1f] text-white py-3 whitespace-nowrap flex items-center border-b border-[#1f1f1f] relative z-30"'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
            
print("Done")
