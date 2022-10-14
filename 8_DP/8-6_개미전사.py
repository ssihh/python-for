#잘못이해함 틀린풀이
n=int(input())
array=list(map(int,input().split()))

d=[0]*2

for i in range(0,n,2):
  d[0]+=array[i]
  d[1]+=array[i+1]

print(max(d))

'''
4
1 3 1 5

4
5 1 2 5
'''
