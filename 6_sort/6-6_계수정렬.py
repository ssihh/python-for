#계수 정렬

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1) #범위 포함 0~9까지 10개

for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)): #0~9
  for j in range(count[i]): #i=0일때 2
    print(i, end=' ')
