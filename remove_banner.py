import re
import glob

files_to_clean = ['index.html', 'booking.html', 'products.html', 'knee-positioner.html']

pattern = r'\s*<!-- Static Banner -->\s*<div class="bg-black text-white py-3 flex items-center justify-center border-b border-black relative z-30 px-4">.*?</div>\s*</div>'

for file in files_to_clean:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed banner from {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

