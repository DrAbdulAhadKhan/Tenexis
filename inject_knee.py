import re

html_content = """<div class="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-7xl mx-auto" id="knee-positioner-grid">
    
    <!-- Product 1: The RAMP -->
    <div class="group flex flex-col bg-white rounded-2xl p-0 shadow-xl shadow-slate-200/50 text-left relative overflow-hidden border border-slate-100 transition-all duration-500 hover:shadow-2xl hover:border-medical-200">
        <div class="p-8 lg:p-10 flex-grow">
            <div class="inline-flex items-center space-x-2 bg-medical-50 text-medical-700 px-3 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest mb-6">
                <span class="w-1.5 h-1.5 rounded-full bg-medical-500"></span>
                <span>Innovative Orthopedic Technologies</span>
            </div>
            
            <h3 class="text-3xl font-display font-bold text-slate-900 mb-4 leading-tight group-hover:text-medical-700 transition-colors duration-300">The RAMP Knee Positioning System™</h3>
            <p class="text-slate-600 leading-relaxed mb-8 text-lg">Six stable leg positions, secured to any OR table in seconds — no assembly, no sterilization.</p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-8">
                <div>
                    <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">Features</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> 6 stable positions (extension to hyper-flex)</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> 2 Velcro belts (entire setup)</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> 0 sterilization / autoclaving needed</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Reusable design with no waste</li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">Clinical Benefits</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Improved surgical ergonomics</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Hands-free stability</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Faster turnover between cases</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Lower staffing need</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="px-8 lg:px-10 pb-8 mt-auto">
            <a href="./13bed3_853367495ff546da994a456a721a14d7.pdf" target="_blank" class="w-full inline-flex items-center justify-center px-6 py-4 rounded-xl bg-slate-900 text-white font-bold text-sm uppercase tracking-widest hover:bg-medical-700 transition-colors shadow-lg">
                View Brochure
                <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </a>
        </div>
    </div>

    <!-- Product 2: TELOS Stress Device -->
    <div class="group flex flex-col bg-white rounded-2xl p-0 shadow-xl shadow-slate-200/50 text-left relative overflow-hidden border border-slate-100 transition-all duration-500 hover:shadow-2xl hover:border-medical-200">
        <div class="p-8 lg:p-10 flex-grow">
            <div class="inline-flex items-center space-x-2 bg-slate-100 text-slate-700 px-3 py-1.5 rounded-full text-xs font-bold uppercase tracking-widest mb-6">
                <span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>
                <span>Diagnostic Device</span>
            </div>
            
            <h3 class="text-3xl font-display font-bold text-slate-900 mb-4 leading-tight group-hover:text-medical-700 transition-colors duration-300">TELOS Stress Device</h3>
            <p class="text-slate-600 leading-relaxed mb-8 text-lg">A simple, precise way to X-ray test knee and ankle ligaments — before and after treatment.</p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-8">
                <div>
                    <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">How it works</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><span class="flex items-center justify-center w-5 h-5 rounded-full bg-medical-100 text-medical-700 font-bold text-[10px] mr-2 shrink-0">1</span> Position limb in the TELOS frame</li>
                        <li class="flex items-start"><span class="flex items-center justify-center w-5 h-5 rounded-full bg-medical-100 text-medical-700 font-bold text-[10px] mr-2 shrink-0">2</span> Apply calibrated, gentle force</li>
                        <li class="flex items-start"><span class="flex items-center justify-center w-5 h-5 rounded-full bg-medical-100 text-medical-700 font-bold text-[10px] mr-2 shrink-0">3</span> Take X-ray under stress</li>
                        <li class="flex items-start"><span class="flex items-center justify-center w-5 h-5 rounded-full bg-medical-100 text-medical-700 font-bold text-[10px] mr-2 shrink-0">4</span> Objective, repeatable measure</li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">Key Benefits</h4>
                    <ul class="space-y-3 text-sm text-slate-600">
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Removes guesswork from diagnosis</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Standardises pre/post comparisons</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Digital readout displays exact force</li>
                        <li class="flex items-start"><svg class="w-5 h-5 text-medical-500 mr-2 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Minimises repeat X-rays</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="px-8 lg:px-10 pb-8 mt-auto">
            <a href="./Telos%20Stress%20Device.pdf" target="_blank" class="w-full inline-flex items-center justify-center px-6 py-4 rounded-xl bg-slate-900 text-white font-bold text-sm uppercase tracking-widest hover:bg-medical-700 transition-colors shadow-lg">
                View Brochure
                <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </a>
        </div>
    </div>
</div>"""

with open('knee-positioner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the empty grid with the new one
content = re.sub(
    r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-10 items-stretch max-w-7xl mx-auto" id="knee-positioner-grid">.*?</div>\n        </div>',
    html_content + '\n        </div>',
    content,
    flags=re.DOTALL
)

with open('knee-positioner.html', 'w', encoding='utf-8') as f:
    f.write(content)
