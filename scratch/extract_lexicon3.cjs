const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\faizy\\Downloads\\standalone (1).html', 'utf-8');

const match = content.match(/D1=(\[\{.*?\}\])/);
if (match) {
    let D1;
    eval('D1 = ' + match[1]);
    fs.writeFileSync('scratch/lexicon_dump.json', JSON.stringify(D1, null, 2));
    console.log("Successfully dumped lexicon to scratch/lexicon_dump.json");
} else {
    console.log("Could not find D1= array in the file");
}
