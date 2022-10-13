#못품.
def div5(x):
  if x%5==0 and x>1:
    return x//5

def div3(x):
  if x%3==0 and x>1:
    return x//3

def div2(x):
  if x%2==0 and x>1:
    return x//2

def min1(x):
  if x>1:
    return x-1

x=int(input())

for i in range(x):
  div5(x) #?..
