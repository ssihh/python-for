# 균형잡힌 괄호 문자열의 인덱스 반환. u,v 나눌 인덱스
def balaned_index(p):
  count=0
  for i in range(len(p)):
    if p[i]=='(':
      count+=1
    else:
      count-=1
    if count==0:
      return i #인덱스 반환

#올바른 괄호 문자열인지 판단
def check_proper(p):
  count=0
  for i in p:
    if i=='(':
      count+=1
    else:
      if count==0:
        return False #쌍이 맞지 않는 경우 
      count-=1
  return True

def solution(p):
  answer=''
  if p=='': # 1.입력이 빈 문자열
    return answer
  index=balaned_index(p) # 2. u,v 나눌 인덱스
  u=p[:index+1]
  v=p[index+1:]

  if check_proper(u): #3-1. u에 대해서 올바른 문자열이면 v에 대해 재귀
    answer=u+solution(v)
  else: #4. u 올바른 문자열아니라면
    answer+='('
    answer+=solution(v)
    answer+=')'
    # print(u)
    u=list(u[1:-1]) #4-4. 첫 번째 문자, 끝 문자 제거
    # print(u)
    for i in range(len(u)):
      if u[i]=='(':
        u[i]=')'
      else:
        u[i]='('
    answer+=''.join(u) #리스트 조인 추가?
  return answer

p='()))((()'
print(solution(p))
