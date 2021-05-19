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

# ### 1. 숫자 자료형

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*5)
print(2**5)
print(3*(4+1))

# ### 2. 문자 자료형

print('풍선')
print("나비")
print("ㅋㅋㅋㅋ")
print("ㅋ"*9)

# ### 3. boolean ( True or False )

print(5>6)
print(True)
print(False)
print(not True)
print(not (5>10))

# ### 4. 변수

# +
# 애완동물을 소개해주세요~

name = '해피'
animal = '고양이'
age = 4
hobby = '낮잠'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요.')
hobby = '공놀이'
print(name, '는 ' ,age, '살이며,' ,hobby,'을 좋아합니다.')
# print(name +'는 ' + str(age) +'살이며,' + hobby +'을 좋아합니다.')
print(name +'는 어른일까요? ' + str(is_adult))
# -

# ### 5. 주석

# +
# 이렇게 하면 여러 문장이 주석처리 됩니다
# cntl + /
# -

# ### 6. 퀴즈

# +
station1 = '사당'
station2 = '신도림'
station3 = '인천공항'

print(station1, '행 열차가 들어오고 있습니다.')
print(station2, '행 열차가 들어오고 있습니다.')
print(station3, '행 열차가 들어오고 있습니다.')
# -

# ### 7. 연산자

# +
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**3) # 제곱
print(5%3) # 나머지
print(5//3) # 몫
print(10 < 3)
print(4 <= 7)
print(4 <= 4)
print(3 == 3) # 앞의 값과 뒤의 값이 같다 
print(4 == 2)
print(3+4+5 == 12)

print(3 != 3) # 앞의 값과 뒤의 값이 같지 않다
print(not(1!=4))
print((3>0) and (3<5))
print((3>0) & (3<5))

print((3>0) or (3>5)) # 둘 중 하나라도 맞으면 True 반환
print((3>0) | (3>5))

print((5>4 >3))
print(5>4>7)
# -

# ### 8. 수식

# +
print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number + 2
print(number)

number += 2
print(number)
number *= 2
print(number)
number -= 2 
print(number)
number /=2 
print(number)
number %= 5
print(number)
# -

# ### 9. 숫자처리함수

# +
print(abs(-5))
print(pow(4,2)) # 승
print(max(5,12)) # max
print(min(1,3)) # min
print(round(3.25)) # 반올림

from math import * # math라이브러리의 모든 패키지를 쓰겠다
print(floor(4.555)) # 내림
print(ceil(4.55)) # 올림
print(sqrt(16)) # 제곱근
# -

# ### 10. 랜덤함수

from random import *

# +
print(random()) # 0과 1사이 임의의 값을 생성
print(random()*10) # 0과 10사이의 값을 생성
print(int(random()*10)) # 0과 10 사이의 정수값을 생성
print(int(random()*10) +1 ) # 1 ~ 10 이하의 임의의 값을 생성

# 로또값 출력
print(int(random()*45) +1)
print(randrange(1,45)) # 1~ 45 미만의 임의의 값을 생성
print(randrange(1,46))
print(randint(1,45)) # 1~45 이하의 값을 생성
# -

# ### 11. 퀴즈

# +
# 3번은 온라인 1번은 오프라인
# 조건 1 : 랜덤으로 날짜
# 조건 2 : 월별 날짜는 다름을 감안하여 28이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비 제외

# 오프라인 스터티 모임 날짜는 매월 x일로 선정되었습니다.
from random import *

date = randint(4,28)
print('오프라인 스터디 모임 일자는 매월', date, '일로 선정되었습니다')
# -

# ### 12. 문자열

sentence = '나는 소년입니다'
print(sentence)
sentence1 = "파이썬은 쉬워요"
print(sentence1)
sentence2 = '''나는 소년이고 파이썬은 쉬워요'''
print(sentence2)

# ### 13. 슬라이싱

jumin = '990123-1234567'
print("성별 : " , jumin[7])
print("연도 : ", jumin[0:2]) # 0부터 2 직전까지 (0,1) 값만 가져온다
print("월 : ", jumin[2:4]) # 2부터 4직전까지 값을 가져온다
print("일 : ", jumin[4:6])
print("생년월일 : ", jumin[0:6])
print("생년월일 : ", jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : ", jumin[7:14])
print("뒤 7자리 : ", jumin[7:])
print("뒤 7자리 : (뒤에서부터)", jumin[-7:]) # 뒤는 -1부터 시작, 앞은 0부터 시작

# ### 14. 문자열 처리 함수

python = 'Python is Amazing'
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) #대문자임?
print(len(python)) # 길이 반환
print(python.replace("Python","java")) # 문자 변환
index = python.index("n")
print(index)
index = python.index("n", index + 1) # index("문자", 시작위치)
print(index)
print(python.find("java")) #  find는 값이 포함되지 않는 경우 -1 반환
# print(python.index("java")) # index의 경우에는 오류 발생 
print(python.count("n")) # 문자가 몇번 나왔는지 카운트

# ### 15. 문자열 포맷

# +
# 방법1
print("나는 %d살입니다." % 20) # %뒤의 값을 받아옴 d는 정수만 입력가능
print("나는 %s을 좋아합니다." % "python") # %뒤의 값을 받아옴 s는 문자
print("Apple 은 %c로 시작해요." % "A") # C 는 문자1개를 받아옴
# 보통 %S로 다 커버 가능

print("나는 %s색과 %s색을 좋아해요." % ("검정","파랑")) # 괄호로 2개의 값을 가져올 수 있음

# 방법2
print("나는 {}살입니다.".format(20)) # 중괄호의 경우 format을 사용해서 값을 입력
print("나는 {}색과 {}색을 좋아해요.".format("파란","검정"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","검정"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","검정"))

# 방법3
print("나는 {age}살이며 {color}색을 좋아해요.".format(age = 20, color="빨강"))
print("나는 {color}살이며 {age}색을 좋아해요.".format(age = 20, color="빨강"))

# 방법4
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # python v 3.4 이상 가능
# -

# ### 16. 탈출문자

# +
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\" 입니다.")

# \\ : 문장내에서 하나로 인식
# \r 커서를 맨앞으로 이동
print("Red Apple\rPine") # 맨앞으로 이동해서 Red 공백만큼 자리 차지
# \b : 백스페이스(한글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")
# -

# ### 17. 퀴즈

# +
# 사이트별 비번 생성
# http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 :  남은 글자 중 처음 세자리 + 글자갯수 + 글자내 'e'; 갯수 + "!"로 구성
# 예 :  생성된 비밀번호 - nav51!

site = "http://naver.com"
my_str = site.replace("http://", "") # replace로 문자열 대체 
print(my_str)
my_str = my_str[:my_str.index(".")] # 숫자 대신 index로 "."의 위치 반환
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print(password)
print("{0}의 비밀번호는 {1}입니다.".format(site, password))
