#바닥 설치만....

def solution(n, build_frame):
  answer = [[]]
  for i in build_frame: # 프레임 명령 수 만큼
    print(i)
    data=[i[0],i[1],i[2]]
    if i[3]==1: #설치하는거면
      if i[2]==0: #기둥 설치면
        #확인을해 기둥 설치할 수 있는건지
        #1. 이미 기둥이 설치되어있진 않은지, 바닥인지 or 보끝에있는지 or 기둥 위인지
        for j in answer: #answer 안에 설치되어있는 기둥있는지 확인
          if j==data: 
            print('same')
            break #탈출
          else:
            if i[1]==0: #바닥에 설치하는 거일때
              answer.append(data)
              print('append')
              break

  return answer


frame1 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1],
          [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(5, frame1))
