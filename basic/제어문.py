# 사용자로 부터 점수를 입력 받습니다. 
# A : 100 ~81, B:80~61, C: 60~0
# score = int(input("점수를 입력하세요"))
# if score >= 81 and score <= 100:
#     print("A")
# elif score >= 61:
#     print("B")
# else:
#     print("C")

# 사용자로부터 두 수를 입력받습니다. 
# 두 중에 큰 수를 출력합니다. 
# num1 = int(input("첫번째 숫자"))
# num2 = int(input("두번째 숫자"))

# if num1 > num2 :
#     print(num1)
# elif num1 < num2 :
#     print(num2)
# else:
#     print("같음")


# 사용자로 부터 입력받은 숫자가 홀수인지 짝수인지 출력
# 6%2
# num = int(input("숫자입력"))
# if num % 2 == 0 :
#     print("짝수")
# else:
#     print("홀수")

#
id = "050104-4214555"
if id[7] == '1' or id[7] == '3':
    print("남자")
else:
    print("여자")

file = "hello.py"
print(file.split('.')[1])
if file.split('.')[1] == 'py' :
    print("파이썬파일")

# for 
# for i in [1,2,3]:
for i in range(1,3,1): #[1,2,3,4,5,6,7,8,9]
    print(i)

i = 1
while True:
    print(i)
    i = i + 1  # i+=1
    if i>3:
        break

# 짝수만..
for i in range(0, 5, 2):
    print(i)


i=0
while i<5:
    print(i)
    i = i + 2  # i += 2


i=0
while i<5:
    i = i + 1  # i += 2
    if i%2 == 1:
        continue
    print(f"continue {i}")

for i in range(1, 11):
    print(f"{i}마리 코끼리가 거미줄에 걸렸네")

dan = int(input("단을 입력하세요(2~9)"))
for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")

# 사용자한테 비밀번호 입력받으세요 
# 비밀번호가 같으면 "성공" 출력하고 종료
# 비밀번호가 다르면 "실패" 출력하고, 다시 입력
# 비밀번호 = "1234" 

while True:
    pw = input("비밀번호입력")
    if pw == "1234" : 
        print("성공")
        break
    else:
        print("실패")
        