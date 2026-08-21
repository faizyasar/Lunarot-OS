const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const zlib = require('zlib');

const html = fs.readFileSync('index.html', 'utf8');

const dom = new JSDOM(html, {
    runScripts: "dangerously",
    resources: "usable"
});

const window = dom.window;

// Patch setStatus to capture the error
let capturedStatus = "";
window.setStatus = function(msg) {
    console.log("STATUS UPDATE:", msg);
    capturedStatus = msg;
};

// Listen for errors
window.addEventListener("error", (event) => {
    console.log("JSDOM UNCAUGHT ERROR:", event.error ? event.error.message : event.message);
});

// Wait for a second to see if unpacking throws
setTimeout(() => {
    console.log("Finished waiting. Final status:", capturedStatus || window.document.getElementById('root').innerHTML.substring(0, 50));
    process.exit(0);
}, 2000);
