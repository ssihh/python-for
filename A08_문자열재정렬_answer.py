data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

#숫자가 하나라도 존재하는 경우에만!! 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

#리스트를 문자열로 변환하여 출력
print(''.join(result))
'''
K1KA5CB7
결과: ABCKK13
AJDLSI412K4JSJ9D
결과: ADDIJJJKKLSS20
'''
