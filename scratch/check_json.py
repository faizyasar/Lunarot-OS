import json
with open('scratch/old_index.html', encoding='utf-16le') as f:
    content = f.read()

tag = '<script type="__bundler/template">'
t_start = content.find(tag) + len(tag)
# We know from HTML that the script tag ends at </script>
t_end = content.find('</script>', t_start)
temp = content[t_start:t_end].strip() # strip the leading/trailing newlines

try:
    j = json.loads(temp)
    print("Original parses! Type:", type(j))
except Exception as e:
    print("Original DOES NOT parse:", e)
