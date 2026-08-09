import glob

for file in glob.glob("products*.html") + ['knee-positioner.html', 'index.html', 'booking.html']:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace text-[10px] sm:text-xs with text-[8px] sm:text-[10px]
        content = content.replace(
            'text-[10px] sm:text-xs font-bold uppercase tracking-[0.2em] px-6',
            'text-[9px] sm:text-[10px] font-bold uppercase tracking-[0.2em] px-6'
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        pass
            
print("Done")
