# ===================== Q1.  배수 구하기 =========================
# input 으로 입력값 A와 B를 받아옵니다.
# for 과 while 을 활용해 1이상 B 이하에서 A의 배수를 출력하세요,
# * 한 코드에서 두 문법을 모두 사용하는 것이 아닌 for 로 만든 코드, while 로 만든 코드 두 개를 만듭니다
# * 항상 B > A 입니다.

# 예시)
# 입력값 10 , 200
# for 에서 출력값 10,20,30,40... 200
# while 에서 출력값 10,20,30,40.... 200

a = int(input("a의 값을 입력해주세요>"))
b = int(input("b의 값을 입력해주세요>"))
temp = 0
result = 0
for i in range(1,b+1):
    if i*a > b:
        break
    print(i*a)
while a * temp < b:
    temp += 1
    result = a * temp
    print(result)

# ===================== Q2. 난수 =====================
# 길이 7의 리스트을 지정하고 안에 랜덤한 숫자를 넣습니다.
# 리스트 안에 있는 값들을 모두 출력합니다.
# 다음 줄에서 리스트에 있는 값들의 합을 출력합니다.
# 그 다음 줄에서 리스트의 최소값, 최대값을 출력합니다
# 마지막으로 리스트에 값의 평균을 출력합니다.
# 리스트 안의 값x 는 0 < x < 100을 만족합니다 .

# 예시
# 입력 없음
# 출력
# 21 23 74 56 23 85 25
# 307
# 21 85
# 43.8

import random
seven_list = []
temp = 0
for k in range(7):
    seven_list.append(random.randrange(1, 100))
seven_list.sort()
print(seven_list)
for h in range(7):
    temp += seven_list[h-1]
print(temp)
print(f"최솟값: ", seven_list[0], "최댓값: ", seven_list[-1])
print(temp/7)

# ===================== Q3. 요일 찾기 =====================
# 변수 3개를 입력 받아옵니다. (x년, y월, z일)
# 서기 1년 1월 1일이 월요일일 때 입력 받아온 날짜의 요일을 구하시오
# 요일을 구할 떄에는 윤년을 고려해야 합니다

# 윤년을 구하는 공식

# - 4로 나누어지는 해는 윤년이다.
# - 100으로 나누어지는 해는 윤년이 아니다.
# - 400으로 나누어지는 해는 윤년이다.

# * datetime 모듈을 사용하지 않고 스스로 만들어야 합니다!!!

# 예시
# 입력값, 2022 04 01
# 출력값 금요일

x = input("연도를 입력해주세요>")
y = input("월을 입력해주세요>")
z = input("일을 입력해주세요>")
count = 0
leap = 0
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for m in range(1,int(x)):
    if m % 4 == 0:
        if m % 400 == 0:
            count += 366

        elif m % 100 == 0:
            count += 365
        else:
            count += 366
    else:
        count += 365

if int(x) % 4 == 0:
    if int(x) % 400 == 0:
        leap = 1

    elif int(x) % 100 == 0:
        leap = 0
    else:
        leap = 1
else:
    leap = 0

for n in range(int(y)):
    count += days[n]

if leap == 1: # 윤달은 2월 29일 추가 이므로 지정된 날짜가 3월 이후인 경우 하루 추가되어야한다
    if int(y) > 2:
        count += 1

count += int(z)
temp = count % 7

if temp == 1:
    print('월요일')
elif temp == 2:
    print('화요일')
elif temp == 3:
    print('수요일')
elif temp == 4:
    print('목요일')
elif temp == 5:
    print('금요일')
elif temp == 6:
    print('토요일')
else:
    print('일요일')