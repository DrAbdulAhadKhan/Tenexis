import glob

for file in glob.glob("products*.html") + ['knee-positioner.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace bg-medical-900 with bg-black
    content = content.replace(
        'class="overflow-hidden bg-medical-900 text-white py-2.5 whitespace-nowrap flex items-center border-b border-medical-800 relative z-30"',
        'class="overflow-hidden bg-[#1a1a1a] text-white py-2.5 whitespace-nowrap flex items-center border-b border-black relative z-30"'
    )
    content = content.replace('bg-medical-900 text-white py-2.5 whitespace-nowrap', 'bg-[#1a1a1a] text-white py-2.5 whitespace-nowrap')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
            
print("Done")
