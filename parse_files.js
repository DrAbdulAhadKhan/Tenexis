const fs = require('fs');
const mammoth = require('mammoth');

async function parse() {
    try {
        let docx1 = await mammoth.extractText({path: 'RAMP Knee Positioning System Summary.docx'});
        console.log('--- RAMP Knee Positioning System Summary.docx ---');
        console.log(docx1.value);
        
        let docx2 = await mammoth.extractText({path: 'TELOS Stress Device OnePager.docx'});
        console.log('--- TELOS Stress Device OnePager.docx ---');
        console.log(docx2.value);
    } catch(e) {
        console.error(e);
    }
}
parse();
