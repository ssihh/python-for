#틀린 풀이입니다: 최대한 많은 그룹이 구성되는 방법이어야함.
n=int(input())
k = list(map(int, input().split()))
g=0 #공포도, 모험가 수
count=0
k.sort(reverse=True)

while g<n:
  g+=k[g]
  count+=1  

print(count)

'''
입력예시1
5
2 3 1 2 2
출력예시1: 2

'''
