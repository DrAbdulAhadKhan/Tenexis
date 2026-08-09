import re

with open('vite.config.js', 'r') as f:
    content = f.read()

# Insert kneePositioner into input object
content = re.sub(
    r"(products5: resolve\(__dirname, 'products-5\.html'\),)",
    r"\1\n        kneePositioner: resolve(__dirname, 'knee-positioner.html'),",
    content
)

with open('vite.config.js', 'w') as f:
    f.write(content)
