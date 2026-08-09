with open('products.html', 'r', encoding='utf-8') as f:
    p1 = f.read()

with open('products-2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

# The pagination section in products.html starts after the grid closes.
# It looks like:
#            </div>
#            <div class="flex justify-center items-center mt-16 space-x-2 relative z-10">
pagination_start = p1.find('<div class="flex justify-center items-center mt-16 space-x-2 relative z-10">')
if pagination_start != -1:
    pagination_end = p1.find('</div>', pagination_start) + 6
    pagination_code = p1[pagination_start:pagination_end]
    
    # We need to adapt the pagination code for page 2
    # In products.html:
    # 1 is active (bg-medical-600 text-white)
    # 2 is a link
    
    p_code = """
            <div class="flex justify-center items-center mt-16 space-x-2 relative z-10">
                <a href="products.html" class="w-10 h-10 flex items-center justify-center rounded-full border border-slate-300 text-slate-600 hover:border-medical-500 hover:text-medical-600 transition-colors" aria-label="Previous Page">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                </a>
                <a href="products.html" class="w-10 h-10 flex items-center justify-center rounded-full font-bold text-sm bg-white text-slate-600 border border-slate-300 hover:border-medical-500 hover:text-medical-600 transition-colors">1</a>
                <span class="w-10 h-10 flex items-center justify-center rounded-full font-bold text-sm bg-medical-600 text-white shadow-md">2</span>
                <a href="products-3.html" class="w-10 h-10 flex items-center justify-center rounded-full font-bold text-sm bg-white text-slate-600 border border-slate-300 hover:border-medical-500 hover:text-medical-600 transition-colors">3</a>
                <a href="products-4.html" class="w-10 h-10 flex items-center justify-center rounded-full font-bold text-sm bg-white text-slate-600 border border-slate-300 hover:border-medical-500 hover:text-medical-600 transition-colors">4</a>
                <a href="products-5.html" class="w-10 h-10 flex items-center justify-center rounded-full font-bold text-sm bg-white text-slate-600 border border-slate-300 hover:border-medical-500 hover:text-medical-600 transition-colors">5</a>
                <a href="products-3.html" class="w-10 h-10 flex items-center justify-center rounded-full border border-slate-300 text-slate-600 hover:border-medical-500 hover:text-medical-600 transition-colors" aria-label="Next Page">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                </a>
            </div>
"""

    # Add Pipeline Innovations section as well
    pipeline_start = p1.find('<div class="mt-24 text-center mb-12">')
    if pipeline_start != -1:
        pipeline_end = p1.find('</section>', pipeline_start)
        pipeline_code = p1[pipeline_start:pipeline_end]
        
        # Now find where to insert in products-2.html
        # We need to find the end of the grid:
        grid_close = '</div>\n        </div>\n    </section>'
        grid_close_idx = p2.rfind(grid_close)
        
        if grid_close_idx != -1:
            # We want to insert the pagination right after the grid items, before the </div>\n        </div>
            # Wait, the grid is just one div, we close the grid, then add pagination, then close the section?
            # Let's see how it's structured in products.html
            
            # In products.html:
            # ... product 11 ...
            # </div> (closes grid)
            # <div class="flex justify-center items-center mt-16 ..."> (pagination)
            # <div class="mt-24 text-center mb-12"> (pipeline)
            # <div class="grid ..."> (pipeline grid)
            # </div> (closes pipeline grid)
            # </div> (closes max-w-7xl mx-auto px-4...)
            # </section>
            
            # So in products-2.html we can just replace the end of the section with the new stuff.
            
            replacement = '</div>\n' + p_code + pipeline_code + '</section>'
            
            # Actually, let's just find the closing grid tag in products-2.html. 
            # In products-2.html we appended: grid_close = """\n            </div>\n        </div>\n    </section>\n"""
            # Let's replace that.
            
            new_p2 = p2.replace('            </div>\n        </div>\n    </section>\n', replacement)
            
            with open('products-2.html', 'w', encoding='utf-8') as fw:
                fw.write(new_p2)
            print("Successfully inserted pagination and pipeline into products-2.html")
        else:
            print("Could not find grid close in products-2.html")
            
