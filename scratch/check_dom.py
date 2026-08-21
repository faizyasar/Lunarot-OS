import re

with open('C:/Users/faizy/Downloads/standalone (1).html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('ABRAHAMIC SYMBOL MATRIX')
if idx != -1:
    print(c[max(0, idx-500):idx+100])
