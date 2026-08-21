const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\faizy\\Downloads\\Lunarot-OS-v6.8-Standalone-mobile-login (1).html', 'utf8');
const startMatch = content.match(/<script type="__bundler\/template">\s*/);
const start = startMatch.index + startMatch[0].length;
const end = content.indexOf('</script>', start);
const jsonStr = content.substring(start, end).trim();

try {
  JSON.parse(jsonStr);
  console.log('JSON is valid in downloaded file!');
} catch (e) {
  console.log('JSON error in downloaded file:', e.message);
}
