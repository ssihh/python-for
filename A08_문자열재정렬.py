data=input()
s=[]
n=[]
r=[]
for i in range(len(data)):
  if ord(data[i])>=65: #아스키코드 65='A'
    s.append(ord(data[i]))
  else:
    n.append(ord(data[i]))

s.sort()
sum=0

for i in range(len(s)):
  r.append(chr(s[i]))
for i in range(len(n)):
  sum+=int(chr(n[i]))

r.append(sum)
print(*r,sep='')
'''
K1KA5CB7
결과: ABCKK13
AJDLSI412K4JSJ9D
결과: ADDIJJJKKLSS20
'''
