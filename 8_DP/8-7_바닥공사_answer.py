# 4번째 경우의 수를 잘못셌었네. 12가아니라 11이었다.
n = int(input())

d = [0] * 1001

d[1] = 1  #1일때. 1
d[2] = 3  #2일때. 3
for i in range(3, n+1): #n+1까지
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796  #3일때 5, 4일때 11
    #점화식 이해 잘 못하겠음 ㅜ
    #796796으로 나누는 이유는 단지 결괏값이 굉장히 커질 수 있기 때문에 그런것. 따라서 값을 계산할 때마다 특정한 수로 나눈 나머지만 취하도록 하면된다.
print(d[n])

'''
3
5
'''
