# 리스트 복사 - 얕은 복사

temps = [38, 31, 33, 35, 27, 26, 25]
values = temps

print(temps)
values[3] = 39
print(temps)
print(id(temps))
print(id(values))