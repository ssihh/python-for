n, m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
#10이면 10까지 들어갈 수 있게 array[0]~array[10]해서 11개
for x in data:  #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
for i in range(1, m + 1):  #1부터 m까지의 각 무게에 대하여 처리
    n -= array[i]  #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  #B가 선택하는 경우의 수와 곱하기
    #array[i]에는 갯수가 들어가있음 array<=n

print(result)
'''
입력예시:
5 3
1 3 2 3 2
출력: 8
8 5
1 5 4 3 2 4 5 2
출력: 25
4 3
2 2 2 3 
출력: 3
'''
