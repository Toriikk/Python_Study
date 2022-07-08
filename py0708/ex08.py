# 딕셔너리 - key/value - {}
capitals = {"Korea":"Seoul", "USA":"Washington", "UK":"London"}
print(capitals["Korea"])
print(capitals["USA"])

for key in capitals: # 키 출력
    print(key, end=" ")

print()
for key in capitals: # 값 출력 - 배열로 집어 넣어
    print(capitals[key], end=" ")

print()
for key in capitals: #키와 값 출력
    print(key,":", capitals[key], end=" ")

print()
# 딕셔너리 함축
values = [1,2,3,4,5,6]
dic = {x : x**2 for x in values if x%2 == 0}
print(dic)