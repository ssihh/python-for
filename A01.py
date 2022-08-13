n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  #총 그룹의 수
count = 0  #현재 그룹에 포함된 모험가의 수

for i in data:  #공포도 낮은 것부터 하나씩 확인하며
    count += 1  #현재 그룹에 포함된 모험가를 포함시키기
    if count >= i:  #총 그룹의 수 증가시키기
        result += 1  #총 그룹의 수 증가시키기
        count = 0  #현재 그룹에 포함된 모험가의 수 초기화

print(result)
'''
입력예시
5
2 3 1 2 2
출력예시: 2

입력예시
6
2 3 1 2 2 3
출력예시: 3

'''
