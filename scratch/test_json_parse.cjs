const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf-8');

const t_start = content.indexOf('<script type="__bundler/template">') + '<script type="__bundler/template">'.length + 1;
const t_end = content.indexOf('</script>', t_start);

const templateStr = content.substring(t_start, t_end).trim();

try {
    const template = JSON.parse(templateStr);
    console.log("JSON.parse SUCCESS!");
    // check if function ip is in there
    console.log("Has function ip?:", template.includes("function ip({"));
    console.log("No unpack error should occur now.");
} catch(e) {
    console.log("JSON.parse FAILED:", e.message);
    
    // show around error
    const match = e.message.match(/position (\d+)/);
    if (match) {
        const pos = parseInt(match[1]);
        console.log("Context:");
        console.log(templateStr.substring(Math.max(0, pos-50), pos+50));
    }
}
