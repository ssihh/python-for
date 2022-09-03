#들여쓰기에 tap이랑 스페이스랑 섞여들어가면 안됨.
#설명 링크: https://unie2.tistory.com/669
def solution(s):
  answer = len(s)
  for step in range(1, len(s) // 2 + 1):  #1개 단위(step)부터 압축 단위를 늘려가며 확인. 1부터 절반까지
    compressed = '' 
    prev = s[0:step]  #제일 앞(0)에서부터 step 만큼의 문자열 추출. 문자열을 제일 앞부터 정해진 길이만큼 잘라야 한다고 함.
    count = 1 #prev, count 상태 초기화
    for j in range(step, len(s), step):  #단위(step) 크기만큼 증가시키며 이전 문자열과 비교
      if prev == s[j:j + step]:  #이전 상태와 동일하다면 압축 횟수(count) 증가
        count += 1
      else:  #다른 문자열이 나왔다면(더이상 압축하지 못하는 경우라면)
        compressed += str(count) + prev if count >= 2 else prev # true값 if 조건문 else 값. 1번만 나타난 경우는 prev만 count가 2 이상일땐 2a
        prev = s[j:j + step]  #다시 prev, count 상태 초기화 prev=b
        count = 1
    compressed += str(count) + prev if count >= 2 else prev  #남아있는 문자열에 대해서 처리
    answer = min(answer, len(compressed))  #만들어지는 압축 문자열이 가장 짧은 것이 정답
  return answer
s = input()
print(solution(s))
'''
aabbaccc
7
ababcdcdababcdcd
9
'''
