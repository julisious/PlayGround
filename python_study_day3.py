# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### 1. 자료 구조의 변경

# +
menu = {"커피","우유","주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
# -

# ### 2. 퀴즈

# +
# 조건 1 : 편의상 댓글은 20명이 작성, 아이디는 1~20
# 조건 2 : 댓글 내용과 상관없이 무작위 추첨 중복 불가
# 조건 3 : random모듈의 shuffle과 sample을 활용

# 출력예제
# - - 당첨자 발표 - -
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# - - 축하합니다. - -

from random import *
users = range(1,21) # 1부터 20까지 숫자 생성
users = list(users)
print(users, type(users))
shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

print("-- 당첨자 발표 --")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
# -

# ### 3.  분기(if문)  : if, elif , else

# +
weather = "우박"
if weather == "비":
    print("우산을 챙기시오")
elif weather == "미세먼지":
    print("우산을 챙기지마세요")
else :
    print("준비물 필요없어요")
    
weather = input("오늘 날씨는 어때요?")
if weather == "비":
    print("우산을 챙기시오")
elif weather == "미세먼지":
    print("우산을 챙기지마세요")
else :
    print("준비물 필요없어요")
# -

temp = int(input("기온은 어때요?"))
if temp >=30 :
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else :
    print("너무 추워요 나가지마세요.")


# ### 4. 반복문(for)

# +
# 대기손님이 100명 늘었을 경우.....?
for waiting_no in range(1,6): # range는 이상 , 미만
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}님 커피가 준비되었습니다".format(customer))
# -

# ### 5. while문 : while 문의 조건이 만족할때까지 반복해라

# +
customer = "토르"
index = 5

while index >=1 :  
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분 되었습니다.")
        
cust = "아이언맨"
index = 1
# while True:
#    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
#    index += 1 # 무한루프
    
cust = "그루트"
person = "Unknown"

while person != cust:
    print("{0}, 커피가 준비되었습니다.".format(cust))
    person = input("이름이 어떻게 되세요?")
# -

# ### 6. continue와 break

absent = [2,5] 
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue    # 아래 문장을 실행하지말고 다음 루프로 넘어가라 
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break       # 지금 상황에서 반복문을 끝내고 종료하는거
    print("{0}, 책을 읽어봐".format(student))

# ### 7. 한줄 for

# +
# 출석번호 1,2,3,4 앞에 100을 붙이기로 했음 -> 101, 102, 103, 104
student = [1,2,3,4,5]
print(student)

student = [i+100 for i in student]  # student에서 i를 불러오면서 거기에 100을 더해라는 의미
print(student)

# 학생들 이름을 길이로 바꾸는 연습
student = ["iron man","thor","groot"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 바꿈
student = ["iron man","thor","groot"]
student = [i.upper() for i in student]
print(student)
# -

# ### 8. 퀴즈

# +
# 50명의 승객, 총 탑승 승객수를 구해라
# 조건 1 : 승객별 운행 소요시간은 5~50분 사이의 난수
# 조건 2 : 소요시간 5~15분 사이의 승객만 매칭해야함

# 출력문 예제
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승승객 : 2분

from random import *


tot = 0 # 총 탑승객수
no = list(range(1,51))
for i in no :
    time = randint(5,51)
    if time >= 5 and time <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        tot +=1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))  
print("총 탑승승객 : {0}분".format(tot))
# -












