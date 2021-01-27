import re

(a,b) = map(int,input().strip().split(' '))
arr = []
for _ in range(a):
    arr.append(input().replace('\n',''))

txt = ''
for m in range(b):
    for n in range(a):
        txt += arr[a][b]

txt = re.sub(r'(\w)([!@#$%& ]+)(\w)', r'\1 \3', txt)
print(txt)
