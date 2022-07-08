# 슬라이스 응용

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white',  'blue', 'red']
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]  # 전체에 대해서 2씩 증가하는 부분에 99 넣어라...
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = [ ]  # 전체에 대해서 공백 주기
print(lst)

# 출력식 : 입력리스트
squares = [ x * x for x in range(10)]
print("=>", squares)

# 출력식 : 입력리스트 : 조건식
squares = [ x * x for x in range(10) if x %2 == 0]
print("%2=>", squares)
