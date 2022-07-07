#리스트 최소/ 최대값 및 정렬
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("min = ", min(values))
print("max = ", max(values))

#정렬1 - 자기 자신
a = [3, 2, 1, 5, 4]
a.sort()
print(a)

#정렬2 - 받아서 변환
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
ascending_number = sorted(numbers)
print(numbers) #원래값 
print(ascending_number)