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

# ### 1. 자료구조 - 리스트 : 순서를 가지는 객체의 집합

# +
# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇번째 칸에 타고 있나?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 탐
subway.append("하하")  # append는 리스트 맨뒤에 추가하는 함수
print(subway)

# 정형돈을 유재석과 조세호 사이에 채움
subway.insert(1, "정형돈")   # insert는 삽입 (위치, 삽입자)
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())  # pop은 뒤에서 하나씩 뺌
print(subway)
print(subway.pop())
print(subway)

# 같은 이름인 사람이 몇명있는지 확인하기
subway.append("유재석")
print(subway.count("유재석"))
print(subway)

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()  # sort()는 오름차순으로 정렬
print(num_list)

# 역으로 정렬
num_list.reverse()  # reverse()는 역순으로 정렬
print(num_list)

# 모두 지우기
num_list.clear()  # clear는 모든 값을 삭제
print(num_list)

# 리스트는 다양한 자료형과 함께 사용가능
mix_list = ["조세호",20,True]
print(mix_list)

# 리스트 확장 
num_list.extend(mix_list)  # extend(리스트) 리스트간 추가
print(num_list)
# -

# ### 2.자료구조-사전 : 단어와설명이 나오는 사전처럼 키와 밸류를 가지고 있음

# +
cabinet = {3:"유재석", 100: "김태호"} # 사전은 중괄호 키 : 밸류 순서로 입력
print(cabinet[3])
print(cabinet[100])

# 사전에서 값을 불러오는 방법
# 1. 대괄호 : 대괄호는 값이 없으면 오류 발생 뒤의 쿼리 진행불가
print(cabinet[3])
# 2. get : get은 값이 없어도 none으로 출력하고 뒤의 쿼리 진행가능
print(cabinet.get(3))
print(cabinet.get(5,"사용가능"))  # 값이 없으면 뒤의 문자를 대신 가져옴

print(3 in cabinet) # 불리안 형태로 출력
print(5 in cabinet)

# 정수가 아닌 문자로 키를 설정
cabinet = {"a3" : "유재석", "b100" : "조세호"}
print(cabinet.get("a3"))

# 키를 추가 또는 변경
cabinet["c3"] = "김종국"
print(cabinet.get("c3"))

# 간 손님 삭제  - del 함수
del cabinet["a3"]
print(cabinet)

# 키 들만 출력
print(cabinet.keys()) 
# 밸류 들만 출력
print(cabinet.values())
# 키, 밸류 쌍으로 출력
print(cabinet.items())

# 사전 내 모든 값 삭제
cabinet.clear()
print(cabinet)
# -

# ### 3. 자료구조 - 튜플 : 리스트와 다른 내용 변경 및 추가 불가, 속도가 빠름, 변경되지 않는 목록 사용시 활용

# +
menu = ("돈까스","치즈까스") # 튜플은 괄호를 활용
print(menu[0])

name = "김종국"
age = 20
hobby = "코딩"
# 위의 값을 아래와 같은 튜플형식으로 입력 가능
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
# -

# ### 4. 세트 : 집합 - 중복이 안되고 순서가 없음

# +
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석","양세형","김태호"}
python = set(["유재석","박명수"])

# 교집합 (java와 파이썬을 모두할 수 있는 사람)
print(java & python)
print(java.intersection(python)) # 교집합 intersection

# 합집합
print(java | python) 
print(java.union(python))  # 합집합 union

# 차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어먹음
python.remove("유재석")
print(python)
# -


















