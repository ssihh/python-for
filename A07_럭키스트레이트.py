data = input()
# print(data[1])
num =[]
# print(num)
for i in range(len(data)):
    num.append(int(data[i]))
  
h=(int(len(data) / 2))
result = 0
left, right = 0, 0
for j in range(h):
    left += num[j]
for k in range(-1,-h-1,-1):
  right+=num[k]

if left==right:
  print('LUCKY')
else:
  print('READY')

