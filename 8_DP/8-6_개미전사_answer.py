#DP는 점화식을 찾아야하네 앞을 내다봐야하는 신기하다
n=int(input())
array=list(map(int,input().split()))

d=[0]*100

d[0]=array[0] #1개일때. 5
d[1]=max(array[0],array[1]) #2개일때. 5
for i in range(2,n): 
  d[i]=max(d[i-1],d[i-2]+array[i]) #d[2]=(5,7). d[3]=(7,d[1]+4=9) 

print(d[n-1]) #9

'''
4
1 3 1 5

4
5 1 2 4
'''
