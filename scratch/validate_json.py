import json

content = open('index.html', encoding='utf-8').read()
start_match = content.find('__bundler/template')
start = content.find('"', start_match)
end = content.find('</script>', start)
jsonStr = content[start:end].strip()

try:
    json.loads(jsonStr)
    print('JSON is valid!')
except Exception as e:
    print('JSON error:', e)
