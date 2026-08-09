import glob

banner_html = """
    <!-- Marquee Banner -->
    <div class="overflow-hidden bg-medical-900 text-white py-2.5 whitespace-nowrap flex items-center border-b border-medical-800 relative z-30">
        <style>
            @keyframes marquee-scroll {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }
            .animate-marquee-scroll {
                display: inline-flex;
                min-width: 200%;
                animation: marquee-scroll 25s linear infinite;
            }
        </style>
        <div class="animate-marquee-scroll flex space-x-12 text-[10px] sm:text-xs font-bold uppercase tracking-[0.2em] px-6">
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
            <span class="text-medical-400 opacity-50">•</span>
            <span>Osteosynthesis Solutions — Shoulder</span>
        </div>
    </div>
"""

for file in glob.glob("products*.html") + ['knee-positioner.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- Marquee Banner -->" not in content:
        content = content.replace("</nav>", f"</nav>\n{banner_html}")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Done")
