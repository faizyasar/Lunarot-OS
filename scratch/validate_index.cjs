const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const startMatch = content.match(/<script type="__bundler\/template">\s*/);
const start = startMatch.index + startMatch[0].length;
const end = content.indexOf('</script>', start);
const jsonStr = content.substring(start, end).trim();
try {
  JSON.parse(jsonStr);
  console.log('JSON is valid in index.html!');
} catch (e) {
  console.log('JSON error in index.html:', e.message);
}
