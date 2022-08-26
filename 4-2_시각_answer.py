h = int(input())

count=0
for i in range(h+1): # +1 해줘야함
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i)+str(j)+str(k): #신기...이게되구나 
        count +=1

print(count)
