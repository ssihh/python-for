n=int(input(),16) #B 입력을 16진수로 변환..............하는거엿어
for i in range(1,16):
  print('%X'%n,'*%X'%i, '=%X'%(n*i), sep='')
