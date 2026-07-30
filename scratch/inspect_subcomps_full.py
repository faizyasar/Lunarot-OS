import re

index_path = r"c:\Users\faizy\Documents\Lunarot Engine\Lunarot-Tarot-Engine-1.0\index.html"

with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

pos_f0 = content.find("function F0()")
pos_p0 = content.find("function P0()")
pos_0 = content.find("function _0()")
pos_w0 = content.find("function W0()")
pos_dollar0 = content.find("function $0()")

print("F0 pos:", pos_f0)
print("P0 pos:", pos_p0)
print("_0 pos:", pos_0)
print("W0 pos:", pos_w0)
print("$0 pos:", pos_dollar0)
