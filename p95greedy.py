n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

#가장 큰수가 더해지는 횟수 계산
count = int(m/(k+1))*k #나눈 몫에서 k곱해주기
count += m%(k+1) #나눈 나머지

result = 0
result += count*first #가장 큰 수 더하기. 횟수만큼
result += (m-count)*second 
#두번째로 큰수 더하기. 전체횟수에서 카운트빼기

print(result)
