#가장작은 것을 선택하는! 선택정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index=i # 0. 가장 작은 원소의 인덱스
  
  for j in range(i+1, len(array)): # 1~10
    if array[min_index]>array[j]: # [0]>[1] 7>5
      min_index=j #[1] 해서 첫 사이클에 0의 인덱스 3을 min_index에
  array[i], array[min_index]=array[min_index], array[i] #스와프

print(array)
  
