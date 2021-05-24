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

# ### 1. 함수(function) : input, output

# +
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


# -

# ### 2. 전달값과 반환값

# +
def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)


# -

def withraw(balance, money):
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다".format(balance))
        return balance
balance = 5000
balance = withraw(balance, 2000)
print(balance)


# +
def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission

balance = 1000
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))


# -

# ### 3. 기본값

# +
#def profile(name, age, main_lang):
#    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

#profile("유재석",20,"파이썬")
#profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반 수업 : 이때 기본값을 사용
def profile(name, age =17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

# -

# ### 4. 키워드 값

# +
def profile(name, age, main_lang):
    print(name, age, main_lang)
          
profile("유재석",20,"파이썬")
profile(name = "유재석", main_lang="파이썬",age=20)


# -

# ### 5. 가변인자

# +
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end = " " 두문장을 나누지 않고 하나의 문장으로 호출
    print(lang1, lang2, lang3, lang4, lang5)
    
profile("유재석",20,"python","java","c","c++","c#")
profile("김태호",25,"kotlin","swift","","","")

# 언어가 하나 더 늘었을때.. 또는 하나 더 줄었을때.. 가변인자 활용

def profile(name, age, *language):  # *로 가변인자를 만들어 줄 수 있음
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
        
profile("김태호",25,"ㅁ","ㅠ","ㅊ","ㅇ","ㅎㅎ","ㅁㅁㅁ")

# -

# ### 6. 지역변수와 전역변수  : 지역변수(잠시만들어서 쓰다가 없어지는 변수), 전역변수(프로그램 전체에서 사용하는 변수)

# +
gun = 10

def checkpoint(soldiers):
    gun = 20    # gun 지역변수
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))

# +
gun = 10

def checkpoint(soldiers):
    global gun    # gun 전역변수 .. 전역변수는 가급적 사용하지 않는 걸 권장
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))

# +
gun  =20
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))
    return gun

gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))


# -

# ### 7. 퀴즈

# +
# 표준 체중을 구하는 프로그램을 작성
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21

# 조건 : 표준 체중은 별도의 함수내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준체중은 소숫점 둘째자리까지 표시

# 출력예제 : 키 175cm 남자의 표준체중은 67.38kg입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21
    
height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)   # round(값, 소수점자리)
print(weight)   
print("키 {0}cm 남자의 표준체중은 {1}kg입니다.".format(height, weight))
# -


