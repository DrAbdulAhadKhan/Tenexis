import re

with open('vite.config.js', 'r') as f:
    content = f.read()

if "booking:" not in content:
    content = re.sub(
        r"(kneePositioner: resolve\(__dirname, 'knee-positioner\.html'\),)",
        r"\1\n        booking: resolve(__dirname, 'booking.html'),",
        content
    )

with open('vite.config.js', 'w') as f:
    f.write(content)
