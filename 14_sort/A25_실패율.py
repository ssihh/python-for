#실패 까뷩
def solution(N, stages):
  answer = [ 0 for _ in range(N+2)]
  stages.sort()
  for i in stages:
    answer[i]+=1
    
  sum=0
  result=[]
  for i in range(1,len(answer)):
    sum+=answer[i-1]
    if (len(stages)-sum)!=0:
      test=round(answer[i]/(len(stages)-sum),3)
    # print(len(stages))
    result.append(test)
    # print(sum)
  # print(result)
  re=result[:N] #n개 5개로 추려주고
  print(re)
  for i in range(1,len(result)):
    print(re.index(max(re))+1) #큰값 출력해야되는데
    
  
  return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
