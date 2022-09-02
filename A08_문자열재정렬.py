data = input()
s = []
n = 0
r = []
for i in range(len(data)):
    if ord(data[i]) >= 65:  #아스키코드 65='A'
        s.append(ord(data[i]))
    else:
        n += int(data[i])

s.sort()

for i in range(len(s)):
    r.append(chr(s[i]))

r.append(n)
print(*r, sep='')
'''
K1KA5CB7
결과: ABCKK13
AJDLSI412K4JSJ9D
결과: ADDIJJJKKLSS20
'''
