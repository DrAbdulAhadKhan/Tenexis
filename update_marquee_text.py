import glob

for file in glob.glob("products*.html") + ['knee-positioner.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        '<span>Osteosynthesis Solutions — Shoulder</span>',
        '<span>Newclip Technics — Osteosynthesis Solutions</span>'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
            
print("Done")
