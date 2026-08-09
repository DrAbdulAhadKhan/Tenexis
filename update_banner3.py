import glob

for file in glob.glob("products*.html") + ['knee-positioner.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        'class="overflow-hidden bg-[#1f1f1f] text-white py-3 whitespace-nowrap flex items-center border-b border-[#1f1f1f] relative z-30"',
        'class="overflow-hidden bg-black text-white py-3 whitespace-nowrap flex items-center border-b border-black relative z-30"'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
            
print("Done")
