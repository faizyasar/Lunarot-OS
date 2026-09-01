import re
import os
import json

transcript_path = r'C:\Users\faizy\.gemini\antigravity-ide\brain\fcc4dae8-da7e-4ef0-8d6d-a4daa9fe4f66\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if 'sonic-gameboy-cartridge' in line:
            obj = json.loads(line)
            # Find the long string in obj
            def get_longest_str(o):
                longest = ""
                if isinstance(o, str):
                    return o
                elif isinstance(o, dict):
                    for v in o.values():
                        s = get_longest_str(v)
                        if len(s) > len(longest): longest = s
                elif isinstance(o, list):
                    for item in o:
                        s = get_longest_str(item)
                        if len(s) > len(longest): longest = s
                return longest
            
            s = get_longest_str(obj)
            print(f"Line {idx}: longest string length = {len(s)}")
            if '<!DOCTYPE html>' in s and '__bundler/manifest' in s:
                p_start = s.find('<!DOCTYPE html>')
                html = s[p_start:]
                out_path = r'C:\Users\faizy\Desktop\HTMLS\Sonic Gameboy Cartridge.html'
                with open(out_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(html)
                print("Saved Sonic Gameboy Cartridge.html! Length:", len(html))
                break
