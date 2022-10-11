#파라메트릭 서치 유형의 문제
#보통 주어진 범위 내에서 특정한 조건을 만족하는 가장 큰 값을 찾는 것이 파라메트릭 서치 문제라고 한다.
# 참고링크: https://techblog-history-younghunjo1.tistory.com/280
# 참고링크: https://youtu.be/Wbhwlf4stfY
#가장 왼쪽부터 시작, 거리차를 탐색
n,c=map(int, input().split())
array=[int(input()) for _ in range(n)]
array.sort()

start = array[1]-array[0] #집의 좌표 중에 가장 작은 값
end = array[-1]-array[0] #집의 좌표 중에 가장 큰 값
result=0

while(start<=end): #조건
  #mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
  mid=(start+end)//2 #4 / 1+3=2 / 3+3=3 (start<=end)
  value=array[0] #1
  count=1
  #현재의 mid값을 이용해 공유기를 설치
  for i in range(1,n): #앞에서부터 차근차근 설치
    if array[i]>=value+mid: #8>=1+4 = 5 / 4>=1+2, 8>=4+2 
      value=array[i] #8 / 4, 8 
      count+=1 #2 / 2, 3
  if count>=c: #C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    start=mid+1 # 3
    result=mid #최적의 결과를 저장 /2
  else: #C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    end=mid-1 #3

print(result)
