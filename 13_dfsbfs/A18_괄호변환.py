#뭐징 못품.

def solution(p):
    answer = ''
    if p=='':
        return ''
    
    count=0
    u=''
    v=''
    for i in p:
        if i=='(':
            count+=1
            u.append(i) 
        else:
            count-=1
            u.append(i)
        if count==0: #문자열u 만들고 탈출.
            break
            
    return answer
