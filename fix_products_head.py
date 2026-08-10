import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('head.html', 'r', encoding='utf-8') as f:
    head_content = f.read()

# Modify title in head_content
head_content = head_content.replace('<title>Tenexis Medical - Precision Engineered Orthopedic Solutions</title>', '<title>Explore Products - Tenexis Medical</title>\n    <meta name="description" content="Explore our Knee Osteotomy Portfolio and Positioning Devices.">')

content = re.sub(r'<head>.*?</head>', head_content, content, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
