import glob
import re

for file in glob.glob("osteotomy*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'href="#"([^>]*>Products</a>)', r'href="products.html"\1', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done nav fix")
