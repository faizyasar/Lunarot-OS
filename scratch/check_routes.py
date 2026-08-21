import re
with open('lexicon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Instead of extracting paths, let's just make the click more robust by waiting for hydration.
# Also we can check if it's an issue with exact text matches.
print("Re-injecting script to wait 1 second before clicking...")
