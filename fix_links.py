import glob
import re

for file in glob.glob("osteotomy*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace pagination links
    content = re.sub(r'href="products\.html"', r'href="osteotomy.html"', content)
    content = re.sub(r'href="products-2\.html"', r'href="osteotomy-2.html"', content)
    content = re.sub(r'href="products-3\.html"', r'href="osteotomy-3.html"', content)
    content = re.sub(r'href="products-4\.html"', r'href="osteotomy-4.html"', content)
    content = re.sub(r'href="products-5\.html"', r'href="osteotomy-5.html"', content)

    # But we want the navbar "Products" to point to the NEW products.html!
    # Wait, the navbar link is text "Products". In osteotomy.html, the pagination links are just numbers or arrows,
    # except maybe breadcrumbs?
    # Let's fix the navbar link back to products.html
    # In the navbar, the link is usually like: <a href="osteotomy.html" ...>Products</a>
    content = re.sub(r'href="osteotomy\.html"([^>]*>Products</a>)', r'href="products.html"\1', content)
    content = re.sub(r'href="osteotomy\.html"([^>]*>Product</a>)', r'href="products.html"\1', content) # footer link

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

