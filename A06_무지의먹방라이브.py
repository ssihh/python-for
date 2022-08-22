def solution(food_times, k):
    answer = 0  #몇번 음식부터 섭취할지
    while k != 0:  #푸드가 남아있을 동안. 0 되면 끝
        if food_times[answer % 3] != 0:
            food_times[answer % 3] -= 1
            answer += 1
            k -= 1
            #print('answer+1 %d'%answer, 'k: %d'%k, 'food:', food_times)
        else:
            answer += 1
            #print('answer: %d'%answer, 'k: %d'%k)
    answer = (answer % 3) + 1
    if max(food_times) == 0:  #푸드가 남아있지 않으면
        #print('남은 음식이 없을때 출력되는 문구입니다')
        answer = -1
    return answer


food_times = list(map(int, input().split()))
k = int(input())
#print(max(food_times))
print(solution(food_times, k))
'''
3 1 2 
5
출력: 1
'''
