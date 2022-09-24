n=int(input())
a=list(map(int,input().split()))

a.sort()

an=(len(a)-1)//2

print(a[an])
