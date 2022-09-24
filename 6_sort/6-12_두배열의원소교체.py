n, k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

#print(a,b)

for i in range(k):
  if min(a)<max(b):
    ai, bi=a.index(min(a)), b.index(max(b))
    a[ai], b[bi]= b[bi], a[ai]
    #print(a,b)
print(sum(a))
'''
5 3
1 2 5 4 3
5 5 6 6 5
결과: 26
'''
