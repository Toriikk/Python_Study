# 리스트 추가 방법에 따른 시간 테스트
import time

SIZE = 50000

start_time = time.time() # 현재 시간을 stattime으로 줌
myList = []
for i in range(SIZE):
    myList = myList + [i*i]  # i*i를 50000번 돌림, 대입연산자 사용 -> 재설정 그래서 시간 많이 걸림 
print("수행시간 = ", time.time() - start_time)

start_time = time.time()
myList = []
for i in range(SIZE):
    myList.append(i*i)  # i*i를 50000번 돌림, append()함수 사용 -> 단순 추가 그래서 시간 적게 걸림
print("수행시간 = ", time.time() - start_time)
