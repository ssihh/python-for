# 1.sorted
array1=[7,5,9,0,3,1,6,2,4,8]

result1=sorted(array1) #리스트반환
print(result1)

# 2.sort
array2=[7,5,9,0,3,1,6,2,4,8]
array2.sort() #내부정렬
print(array2)

# 튜플 key활용
array3=[('바나나',2),('사과',5),('당근',3)]
def setting(data):
  return data[1] #0,1. 두번째기준 정렬

result3=sorted(array3, key=setting)
print(result3)
