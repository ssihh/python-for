#참고링크: https://jinho-study.tistory.com/685
x,y=map(int, input().split())

z=int((y*100)/x)
start=0
end=1000000000
#왜 start, end 값을 저렇게 해주지?
#start=1, end=x-y 해도 답나왔었는데 틀렸다고 나옴.
result=-1

while(start<=end): #조건
  mid=(start+end)//2 #1+2//2=1 
  zm=int(((y+mid)*100)/(x+mid)) 
  if z==zm:
    start=mid+1
  elif z<zm:
    end=mid-1
    result=mid
  # print(start, end, mid, z, zm, result)

print(result)
