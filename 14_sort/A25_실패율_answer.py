def solution(N, stages):
  answer=[]
  length=len(stages)

  #스테이지 번호를 1부터 N까지 증가시키며
  for i in range(1,N+1):
    count= stages.count(i) # count() 리스트 안에 특정값 개수를 반환

    if length==0: #실패율 계산. 0명이면! 못나누니까 0
      fail=0
    else: 
      fail=count/length 
      #해당 스테이지 인원수(아직 못깬사람)/스테이지에 도달한 플레이어의 수(깬사람이나 안깬사람)

    answer.append((i,fail)) #튜플로 ! (단계, 실패율)
    length-=count #사람수 빼주기 (못깬사람 빼줌)

  
  answer.sort(reverse=True, key=lambda s: s[1]) # 실패율 기준 내림차순 정렬  
  # print(answer)
  answer=[i[0] for i in answer] #정렬된 단계 출력
  return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
