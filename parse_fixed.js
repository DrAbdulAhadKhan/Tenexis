const fs = require('fs');
const pdf = require('pdf-parse');
const mammoth = require('mammoth');

async function parse() {
    console.log("=== DOCX 1 ===");
    let d1 = await mammoth.extractRawText({path: "RAMP Knee Positioning System Summary.docx"});
    console.log(d1.value.substring(0, 500));
    
    console.log("=== DOCX 2 ===");
    let d2 = await mammoth.extractRawText({path: "TELOS Stress Device OnePager.docx"});
    console.log(d2.value.substring(0, 500));
    
    console.log("=== PDF 1 ===");
    let p1 = await pdf(fs.readFileSync("13bed3_853367495ff546da994a456a721a14d7.pdf"));
    console.log(p1.text.substring(0, 500));
    
    console.log("=== PDF 2 ===");
    let p2 = await pdf(fs.readFileSync("Telos Stress Device.pdf"));
    console.log(p2.text.substring(0, 500));
}
parse();
