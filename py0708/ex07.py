# 튜플/ 딕셔너리(비정형데이터) / 세트

#튜플 - 변경 불가 - ()
fruits = ("apple", "banana", "grape")
print(fruits)
print(fruits[0])
for f in fruits:
    print(f, end=", ")

#튜플을 리스트로
myTuple = (1, 2 ,3, 4)
myList = list(myTuple)
print()
print(myList)

#세트 - 중복 불가 - {}
numbers = {1, 2, 3}
print("set = ", numbers)

numbers = set([1,2,2,3,4,5,5]) # 리스트로는 그냥 출력 되겠지만 set은 중복 허용 불가
print("set= ", numbers)

#세트 함축 연산
aList = [1,2,3,4,5,1,2]
result = {x for x in aList if x % 2 == 0}
print("x=%2", result)

# 세트 - 교집합/ 합집합 / 차집합
A = { "apple", "banana", "grape"}
B = { "apple", "banana", "kiwi"}
C = A & B
D = A | B
E = A - B
print("교집합 = ", C)
print("합집합 = ", D)
print("차집합 = ", E)