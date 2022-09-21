#적절한 위치에 삽입하는! 삽입정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1): #i부터 -1하면서 
    if array[j]<array[j-1]: # [1]<[0], 5<7
      array[j], array[j-1]=array[j-1], array[j] #스와프
    else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break
      
print(array)
  
