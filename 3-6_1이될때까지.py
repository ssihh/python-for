#100억 이상의 큰수가 되는 경우를 가정했을 때에도 빠르게 동작하려면,
#N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식으로 소스코드를 작성
n, k = map(int, input().split())
result = 0

while 1:
  target =(n//k)*k # target: n이 k로 나누어 떨어지는 가장 가까운 수가 어떤것인지
  result+=(n-target) #result: 1을빼는 연산을 몇번 수행할지 한번에 계산해서 넣어줌
  n=target #n이 target이 되도록함
  if n<k: #n이 k이하면 탈출 10//5 연상해봐
    break
  result+=1
  n//=k

result+=(n-1) #n이 1보다 크다면, 1이 되기위해 남은 수에 대해서 1씩 빼는 연산을 한번에 계산
print(result)
'''
입력예시1
25 5
출력예시1: 2

입력예시2
25 3
출력예시2: 6
'''
