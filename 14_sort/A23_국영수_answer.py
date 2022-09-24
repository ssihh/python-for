n=int(input())
students=[]

for _ in range(n):
  students.append(input().split())

students.sort(key=lambda x: (-int(x[1]),int(x[2]), -int(x[3]),x[0])) #람다식 활용. 여기서 int씌워주네
 
for student in students:
  print(student[0])
