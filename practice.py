#%%
print (2**3) # 2^3=8
print (10/2)  # 정수끼리 나누어도 float로 결과가 나옴
print (10//2)  #정수로 결과를 얻고 싶으면 
print (5%3) # 5 나누기 3의 나머지=2
print (10%3) # 10 나누기 3의 나머지=1
print (5//3)  # 5나누기 3의 몫=1
print (10//3) #10나누기3의 몫=3
print (4>=7) #False
print (5>=5) #True
print (3==3) # 앞 뒤 가 완전히 똑같다; True
print (2+3 ==5) #True
print (1!=3) # 앞 뒤 가 같지 않다; True
print (not (1!=3)) # not은 괄호안의 반대를 표시; False
print ((3>0) and (3<5)) #두가지 모두 만족해야 True; True
print ((3>0) & (3<5)) # and와 & 는 같은 의미; True
print ((3>0) or (3>5)) #둘 중 하나만 만족하면 True; TRue
print ((3>0) | (3>5)) # or 와 | 는 같은 의미; True
print (5>4>3) # True
print (5>4>7) # False
print (round (3.14 *5,2)) #round함수는 소수점 끊어서 출력할 때 사용, 소수점 2째자리
print (abs (-3))  #절대값
print (divmod(7,2))  #나누었을때 몫과 나머지 한꺼번에 구하기
pow(2,3) #거듭제곱 함수
ord ("A")  # ASCII code 에 따라 숫자로 변경
chr (65) # ASCII에 따라 알파벳, 또는 다른 표시로 변경
-3 % 26  #파이썬에서는 나머지가 양수가 되도록 (-3+26)%26 의 형태로 계산됨.

#%%
#eval() 함수, string으로 된것을 연산으로 바꿔주는 기능
print (eval ('1+2'))
print (eval (input ()))

import random

num1, num2 = random.randint(1, 9), random.randint(1, 9)
op = random.choice(("+", "-", "*", "//"))
print (eval (''f'{num1}{op}{num2}''')) #eval 함수내에 변수 사용할때 주의.


import math
math.gcd(18, 24)  # 최대공약수를 구할 수 있습니다. 함수이름 gcd는 the greatest common divisor에서 왔습니다.

# %%
#Embedding values in strings
myscore =1000
message = "I scored %s points"
print (message % myscore)
nums = 'What did the number %s say to the number %s? Nice belt!!'
print (nums % (0,8))

# %%
a='hello'
b='     '
c=''

#boolean (참/거짓)
print(bool(a))
print(bool(b))
print(bool(c))
      
fruit = 'apple'
print (fruit[0:2])
print (fruit[:])
print (fruit[-5:])

letter = "how are YOU?"
print (letter.upper())
print (letter.lower())
print (letter.capitalize())
print (letter.title())
print (letter.swapcase())
print (letter.split())
print (letter.count('how'))

# %%
s='나도고등학교'
print(s.startswith('나도'))
print(s.endswith('초등학교'))
d='...나도고등학교...'
print(d.strip('.')) #문자빼기
q=d.replace('고등학교','초등학교')
print(q)
print(q.center(120,'-')) #q를 center에 두고 앞뒤에 -를 넣어서 총 120자에 해당하는 문자열 만들기

# %%
python ='파이썬'
java='자바'
print(python+java)
print(python+' '+java)
print(python,java) #,는 자동 띄우기
print('개발 언어에는 {}, {}등이 있어요'.format (python, java)) #format -중간에 문자 끼워넣기
print('개발 언어에는 {1}, {0}등이 있어요'.format (python, java)) #format 순서정하기
print(f'개발 언어에는 {python}, {java} 등이 있어요') #f.string
print("{a},{b},{c}" .format (a="Apple", b="Banana", c="Cherry"))
print("{a},{a},{a}" .format (a="Apple", b="Banana", c="Cherry"))

snack = '꿀꽈배기는\n너무\n맛있어요' #탈출문자로 줄바꾸기 \n
print (snack)

# %%
#list [] 사용
my_list = ['오예스','몽쉘','초코파이'] #list는 순서가보장, 가변변수임.
print (my_list[0]) #리스트내에 해당하는 값 출력
print ('몽쉘' in my_list) #리스트에 포함되어 있는지 in
print (len(my_list)) #list에 몇개가 포함

my_list [0] = '몽쉘카카오' #list 수정하기
print (my_list)

my_list.append ('박파이') #list 에 값 추가
print (my_list)

my_list.remove ('몽쉘')  #list 에서 값빼기
print (my_list)

# del my_list ['초코파이']
print (my_list)

your_list=['빅파이','오뜨']
print(my_list + your_list) #list와 list합치기
your_list.extend(my_list) #your list 뒤에 my list넣어서 확장시키기, your list정의가 바뀜
print (your_list)
print (your_list [2:5]) #list의 2,3,4를 보여달라, 프로그램은 실제 0에서 시작하여 numbering

his_list= [1,2,3]
p = his_list.pop (0)  # my_list의 0 index에 있는 아이템하나를 가지고 옴. my_list의 list에서는 없어짐. 
print (p)
print (his_list)

# 만약 reverse 된 새로운 리스트를 만들고 싶다면?
my_list = ["A","B","C","D","E"]
new_list = my_list [::-1]
print (new_list)

my_list = ["1", "234", "567"]
"|".join(my_list) #join 함수는 list 합칠때 사이사이에 원하는 문자를 넣어줌

# %%list comprehension
my_list = [x**2 for x in range (1,11)]  #for문을 사용해서 
[x**2 for x in [x**2 for x in range (11)]] #이터러블 자리에 리스트 컴프리헨션을 사용할 수도 있음.
[x for x in range (11) if x%2 ==0] # 조건문과 함께 사용할 수 있음.

combinations = []
for x in [1,2]:
    for y in ["A","B"]:
        combinations.append((x,y))
combinations  #이렇게 2중 for문을 사용하는것 보다 아래 list comprehension을 사용하면 간편

[(x,y) for x in [1,2] for y in ["A","B"]] #리스트내에 2중 for문으로 튜플을 만들수 있음.

[(x,y) for x in range (1,7) for y in range(1,7)  if x+y =6]  #조건문걸수도 

vec = [-4,-2,0,2,4]
[abs(x) for x in vec if x <0.0 ] #함수와 같이 사용가능

my_fruits = ['  banana', '  loganberry ', 'passion fruit  ']
[fruit.strip().upper()   for fruit in my_fruits] #strip은 문자 빼기

nested_list = [[1,2,3], [4,5,6], [7,8,9]] #중첩 list를 풀기
[num for sub_list in nested_list for num in sub_list]

#%%
#set comprehension
{v*v for v in [1,2,3]}
#Dict comprehension
{key:val for key,val in enumerate ('ABCD') if val not in 'CB'}
#tuple은 반드시 앞에 tuple을 표시해줘야 한다.
tuple (v*v for v in [1,2,3])  # tuple 표시를 해주지 않으면 generator 형태로 만들어짐.


# %%

# 정렬 sort() 메써드 사용,ㅡ  크기 순서대로 정렬함.
my_list = [3,1,4,1,5,9,2]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print (my_list)

# 문자열을 정렬한다면? 대문자가 먼저, 알파벳순서로
my_list =['Python','Beyond','hello','comilers','apple','Apple']
my_list.sort()
print(my_list)

my_list = ["A", "B", "D", "E"]
my_list.insert(2, "C")  #위치 지정하지 않으면 오류
print (my_list)

#문자열 위치 정렬
#  :<   또는 ljust() 왼쪽 정렬 
#  :^ 또는 center () 가운데 정렬
#  :> 또는 rjust() 우측 정렬
#  :-^ 공백을 -로 채움

# %%
#tuple () 사용, 읽기 전용임. 수정,추가,삭제 불가
my_tuple = ('오예스','몽쉘','초코파이') #패킹
(pie1, pie2,pie3)=my_tuple #언패킹, my_tuple내의 있는 것들을 pie1-3로 지정함.
numbers =(1,2,3,4,5,6,7,8,9,10)
(one,two,*others) = numbers #others에 나머지가 리스트 형태로 지정
(one,*others,two) = numbers 
print(my_tuple)
print(others)

# %%
#set, 순서/중복 허용안됨. 하지만 추가,삭제는 가능
A={'돈까스','보쌈','제육덮밥'}
B={'짬뽕','초밥','제육덮밥'}
print(A.intersection(B)) #교집합
print(A|B)

print(A.union(B)) #순서는 보장안됨 #합집함
print(A&B)

print(A.difference(B)) #차집합
print (A-B)

print(A.symmetric_difference(B)) #대칭차집합 (합집합 - 교집합)
print (A^B)

# print(A[0]) #순서가 보장되지 않으므로 index사용해서 명령불가
A.add('닭갈비')  #집합은 순서 유지해주지 않는다  #리스트는 .append 명령문임.
print (A)
A.remove('보쌈')
print(A)
A.clear() #set내의 모든 값 지우기
print (A)
del A # A set자체를 완전 삭제


# %%
#dictionary 또는 map {key1:value1, key2:value2} #표를 상상 #수정/추가/삭제 가능
person = {
  '이름':'이필형',
  '나이': 44,
  '키' : 172,
  '몸무게' : 69
}
print(person['이름'])
del person ['나이'] #해당 key:value삭제,  person.pop('나이') 로 해도됨.
print (person)
person ['이름'] = '나정화' #key에 해당하는 value replace
print (person)
person ['성격'] = '착함' #새로운 key와 value추가
print (person)
person.update ({'키':173, '몸무게': 70}) #여러개 value 바꾸기
print (person)
print (person.keys()) #어떤 key 들이 있는지 확인
print (person.values()) #어떤 value 들이 있는지 확인
print (person.items ()) # ,로 구분된 모든 data 확인
person.clear() #dic안의 모든 자료 삭제
print (person)


# %%
#tuple에 값추가하기: list로 바꾼다음 값 추가하고 다시 tuple로
my_tuple=("몽쉘","오예스")
my_list=list(my_tuple)
my_list.append("쵸코파이")
my_tuple=tuple(my_list)
print(my_tuple)

# %%
# list에 있는 중복값 제거하기: 중복값 허용하지 않는 set이용
my_list= ('몽쉘', '오예스', "쵸코파이",'쵸코파이','쵸코파이')
my_set=set (my_list)
my_list=list(my_set)
print(my_list)

# %%
# 다만 set는 순서가 random이기 때문에 순서가 중요하다면 dict이용
# dict는 순서를 보장하면서 key의 중복 허용안함.
my_list= ('몽쉘', '오예스', "쵸코파이",'쵸코파이','쵸코파이')
my_dict=dict.fromkeys (my_list) #value는 모두 none임
print (my_dict)
my_list=list(my_dict) #key value만 뽑아서 list로 만듬
print(my_list)


# %%
# if, else, elif. if중첩
yellow_card=0  #이 값에 따라 최종 print다름
foul=True  #False로도 해보자
if foul:
  yellow_card+=1  # += 또는 -=은 yellow_card에서 1을 더하거나 빼서 다시 yellow_card로정의
  if yellow_card ==2:
    print ("경고누적퇴장")
  else:
    print ('휴, 조심해야지')
else:
  print ('주의')


my_dict = {"기차": "기차는 길어", "바나나": "바나나는 맛있어"}
word = input ()
print (my_dict.get (word, "알 수 없습니다.")) # get() 메써드의 기본값이 else: 역할을 합니다.
  
# %%
# string을 number로 바꾸기
age ='10' # string값으로 지정함
converted_age = int(age)  #int는 정수(interger)만 변환함.

age1 = 10
converted_age1 = str(age1) #str은 number를 string으로

age2 = 10.5
converted_age2 = float(age2) #float는 소수점 포함한 실수로 변환

print (age, converted_age, converted_age1, converted_age2)

# %%
# 반복문 (loop) for 변수 in 대상 또는 반복범위
# 형태는 다음과 같다.
#for 변수 in 이터러블-객체:
 #   반복할 명령문들
#else:
 #   반복이 (break없이) 끝나면 실행될 명령문들

for x in range (10):
  print(f'팔벌려 뛰기 {x}회 해') #range (10)이면 0 - 9 까지 의미
for num in range (15):
  print(f'음료쿠폰- 입장번호{num+1}')
# range (x,y,z) x부터 y 미만까지 지정, z step만큼
for n in range (1,22,10):
  print(f'{n}번 학생이 {n}번부터 {n+9}번 학생꺼까지 걷어주세요')
  
  
# %% # 반복문은 list,tuple,disct, 문자 모두 가능
my_list=[1,2,3,4]
my_tuple=(1,2,3,4)
for x in my_list:
  print(x)
for y in my_tuple:
  print(y)
person={'이필형':'90점', '나정화': '95점', '박인근': '55점', '이제인': '100점'}
for k in person.keys():
  print (k)
for v in person.values():
  print (v)
for a,b in person.items():
  print (a,b)
for c,d in person.items():
  print (d,c)
fruit='apple'
for e in fruit:
  print (e)
# %%
# while문
max=25
weight=0
item=3
while weight+item <=max:
  weight+=item
  print ('짐을 추가합니다')
print (f'최대 무게는 {weight}입니다')
# %%
# break : 반복문 탈출, continue : 반복문 건너뛰기 계속 진행
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
  if x == '시즌3':
    print ('재미없대, 그만보자')
    break
  print (f'{x}시청') #이 명령문이 어디에 위치하느냐에 따라 결과 달라짐. loop의 진행순서대로
  
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
  if x == '시즌3':
    print ('재미없대, 그만보자')
    continue  #아래 print 명령어 건너뛰고 다시 위로
  print (f'{x}시청')

for x in range (10):
  if x %2 ==1:
    continue
  print (x)
# %% 퀴즈
ingredients = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
a=1
for x in ingredients:
  print (a, x)
  a=a+1


# %%
#list comprehension
products=['JOA-2020','JOA-2021','SIRO-2020','SIRO-2021']
recall=[] #SIRO 제품 모두 recall하는 새로운 list 만들기
for p in products:
  if p.startswith('SIRO'):
    recall.append(p)
print(recall)

#위에 코드를 간단히 list comprehension으로 정리하면
recall1=[p for p in products if p.startswith('JOA')]
print(recall1)

country_list=['korea','English','france']
new_list=[x.upper()  for x in country_list if 'a' in x]
new_list


# %% ASCII art https://ascii.co.uk/art/
print ('''
                                     -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
       
       ''')


# %%  input은 사용자에게 값을 받을 때, 숫자를 입력받아도 문자로 인식
name= input("이름을 적어주세요")  
print(name+"님 안녕하세요") #문자이기 때문에 + 사용가능
print(name,"의 세계에 오신것을 환영합니다.") #,사용하면 띄어쓰기

# %%
print ("사과 1개는 500원입니다.")
count = int (input ("사과 몇개를 드릴까요")) #숫자를 입력받아도 문자로 인식하기 때문에 int()함수로 숫자로 변환
print ("총 금액은", count*500 , "원 입니다.") # +는 문자를 합칠때에만 사용가능, 숫자문자 조합은 ,로 이어주어야함.
print (f"총 금액은 {500*count}원 입니다.") #count 함수를 숫자로 바꿔주었기 때문에 계산 가능

# %%
# split() 입력받은 값을 space를 기준으로 두개로 나누는 기능
a,b = input ("곱셈할 두 수를 입력해 주세요. 예) 10 4 \n").split() # escape \n 엔터키 역할 -- 여기서도 입력값이 문자로 인식
print (f"곱셈의 결과는 {int(a)*int(b)})입니다")

# %%
# 함수: 어떤 동작을 수행하는 코드들의 묶음. 여러곳에서 사용되는 코드는 하나의 함수로. 함수는 전달값(parameter) 사용가능
def show_price():
  print ('커트 가격은 10000원입니다')
show_price()   #함수 호출

def get_price(customer): #전달값 사용
  print (f"{customer}고객님")
  print ('커트 가격은 10000원입니다')
customer1 = '이필형'
get_price(customer1)
customer2 = '나정화'
get_price(customer2)

# %%
#반환값; return 
def got_price(is_vip):
  if is_vip==True:
    return 10000
  if is_vip==False:
    return 15000
price=got_price(True)
print (f'커트 가격은 {price}원입니다".')
price1=got_price(False)
print (f'커트 가격은 {price1}원입니다".')
# %%
# 함수에서 전달값의 기본값을 지정할 수 있음. def(전달값 = 기본값)의 형태
def got_price(is_vip=False):  #False가 기본값임.
  if is_vip==True:
    return 10000
  if is_vip==False:
    return 15000
price=got_price() #전달값이 없어도 False가 기본값
print (f'커트 가격은 {price}원입니다".')
price1=got_price(True) # 기본값 외에는 적어줘야
print (f'커트 가격은 {price1}원입니다".')

# %%
# 전달값은 여러개 가능, 이때는 기본값으로 설정하는것이 편함
def get_price (is_vip=False, is_birthday=False, is_membership=False, card=False, review=False, first_time=False):
# 여러개의 기본값들 중 한개를 바꿀때는 그 전달값만 딱 적으면 됨.
def get_price(review=True, is_birthday=True):
# 기본값이 없는 매개변수는 왼쪽에 와야 함. 아니면 오류
def repeat_print (message, count=1):



# %%  
import random
computer = random.randint(0,10)  #0이상, 10이하 난수의 생성. 
computer

random.randrange (1,7,2)  #1,3,5 중 하나를 랜덤하게 발생
random.random() # 0.0 이상 1.0 미만의 float형 난수
random.uniform(0.0, 1.0) # 0.0이상 1.0 이하의 float형 균일 분표
random.gauss(0.5, 0.01) # 평균이 0.5이고 표준편차가 0.01인 정규 분포
random.choice(("+", "-", "*", "//")) # 시퀀스중 하나를 랜덤으로 골라줌.


# %%
# 가변인자: 갯수가 바뀔수 있는 인자, 전달값 앞에 * 붙여주면 됨 -- tuple 형태로 받음.
# 즉, 한개의 변수가 들어가는 자리에 여러갯수를 넣고 싶다면
def visitors (today, *customers): # 가변인자는 한 함수에 한번만 사용가능
  print (today)
  for customer in customers:
    print (customer)
visitors ('2022년 9월 1일','이필형','나정화')


#** 두개 붙이면 disct 형태로 받음.
def print_many(**keywords):
    print(type(keywords))
    for k in keywords:
        print(k, ":", keywords[k])
print_many (a=65,b=66)  #단 등로를 붙여서 지정

#%%
#unpacking: 연산자를 이터러블 앞에 사용하면 하나의 이터러블 객체로 묶여 있는 여러개의 아이템들을 여러개의 객체로 풀어줌.
my_list = [1, 2, 3]
print(my_list)  # print([1, 2, 3])
print(*my_list)  # print(1, 2, 3)

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list = [*my_list1, *my_list2]
your_list = [my_list1, my_list2]
print (my_list)
print (your_list)

def add_three(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    return a + b + c
add_three (*[1,2,3])  #add_three (1,2,3)

#*연산자로 사전을 언팩하면 키만 전달됩니다.
def add_three(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    return a + b + c
add_three (*{"A":1, "B":2, "C":3})

{**{"a": 1, "b": 2}, "c": 2}

def add_three(a, b, c):

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    return a + b + c
add_three (**{"a":1, "b":2, "c":3})
#add_three (a=1,b=2,c=3) 과 동일

# %%
# 함수내에서는 지역변수로, 함수밖에서는 전역변수
# 함수내에서 전역변수를 지정, 정의하려면 global 붙여주면 됨.
message ='나는 전역변수'
print (message) #전역변수 출력
def no_secret():
  message='이러면 지역변수' # 함수내의 지역변수가 새로지정됨
  print (message) #지역변수가 출력
no_secret()

def yes_secret():
  global message # 전역변수 사용하겠음. 없으면 여기서 새로 만들겠음. 이런의미
  message ='전역변수임 속았지'
  print (message) #전역변수가 새로 바뀌어서 출력
yes_secret()
# %%
import time
print (time.asctime()) #현재 시간을 string으로 보여줌
import sys
print(sys.stdin.readline()) # 입력자가 입력한 string을 읽는 기능

# %%
# 파일을 읽거나 쓰거나, open (파일명,열기모드, encoding='인코딩')
f=open ('list.txt','w',encoding='utf8') #utf8은 한글
f.write ('김일성\n')
f.write ('이필형\n')
f.close() # 파일 닫기

f=open ('list.txt','r',encoding='utf8')
contents = f.read() #파일내용 다 읽어오기
# for line in f:
#    print (line, end="")  #end는 문장 끝내는 것 처리
print (contents)
f.close() 

with open ('list.txt','r',encoding='utf8') as f: # with를 사용하면 자동으로 파일 닫힘.
contents = f.read()
print (contents)
# %%
get clone https://github.com/deeplearningzerotoall/PyTorch.git


# %% class (설계도[객체]와 설명서[기능]를 합친 개념)
class BlackBox:  #class명을 대소문자 섞어서
  pass # 구현해야 하는 걸 잠시 미루는 명령어
b1=BlackBox() # b1이 BlackBox class 로 선언
b1.name='까망이'
print(b1.name)
print(isinstance(b1, BlackBox))  #b1이 BlackBox class의 instance가 맞는지 확인


# %%
class BlackBox:
  def __init__(self, name, price): #클래스내에 사용되는 함수를 method라고 함. 반드시 처음전달겂은 self
    self.name=name  #멤버변수, self.name 처럼 해야 함.
    self.price=price
b1=BlackBox('까망이', 200000) #객체
print(b1.name, b1.price)
b2=BlackBox('노랑이', 100000) #객체
print(b2.name, b2.price)
b2.nickname='1호'   #class내의 각 객체는 독립적이고, 각 객체는 다른 수의 변수를 가질수 있음.
print(b2.name, b2.price, b2.nickname)

# %%
class BlackBox:
  def __init__(self, name, price):
    self.name=name  
    self.price=price
  def set_travel_mode (self, min):
    print (f'{self.name} {min}분 동안 여행모드 ON')
b1=BlackBox('까망이', 200000) 
b2=BlackBox('노랑이', 100000) 
b1.set_travel_mode (20) #아래와 같은 결과
BlackBox.set_travel_mode (b1, 20)  #위와 같은 결과

# %%  class 의 상속
#기본 BlackBox
class BlackBox:
  def __init__(self, name, price):
    self.name=name  
    self.price=price
#여행모드지원 블랙박스
class TravelBlackBox(BlackBox): # BlackBox의 method를 그대로 상속받음.
  def set_travel_mode (self, min):
    print(str(min) +'분 동안 여행모드 ON')
  
b1=BlackBox('까망이', 200000) 
b2=TravelBlackBox('노랑이', 100000)
b2.set_travel_mode (20)

# %% class 의 상속
class BlackBox:
  def __init__(self, name, price):
    self.name=name  
    self.price=price
class TravelBlackBox(BlackBox): # BlackBox의 method를 그대로 상속받고 추가 객체삽입.
  def __init__(self, name, price, sd):
    super().__init__(name, price) # 이때 super(). 을 사용 (부모class라는 의미), self는 필요없음.
    self.sd=sd #추가 sd 객체에 대한 정의만 지정

  def set_travel_mode (self, min):
    print(str(self.sd)+'GB SD카드에', str(min) +'분 동안 여행모드 ON')
b2=TravelBlackBox ('노랑이', 100000, 128)
b2.set_travel_mode (20)

# %% class의 다중상속, 
class BlackBox:
  def __init__(self, name, price):
    self.name=name  
    self.price=price
class VideoMaker:
  def make(self):
    print ('추억용 여행영상제작')
class MailSender:
  def send(self):
    print ('메일 발송')
class TravelBlackBox(BlackBox, VideoMaker, MailSender): #다중상속 
  def __init__(self, name, price, sd):
    super().__init__(name, price) 
    self.sd=sd 
  def set_travel_mode (self, min):
    print(str(self.sd)+'GB SD카드에', str(min) +'분 동안 여행모드 ON')

b2=TravelBlackBox ('노랑이', 100000, 128)
b2.make()
b2.send()

# %% class내 method overriding
class BlackBox:
  def __init__(self, name, price):
    self.name=name  
    self.price=price
class VideoMaker:
  def make(self):
    print ('추억용 여행영상제작')
class MailSender:
  def send(self):
    print ('메일 발송')
class TravelBlackBox(BlackBox, VideoMaker, MailSender): #다중상속 
  def __init__(self, name, price, sd):
    super().__init__(name, price) 
    self.sd=sd 
  def set_travel_mode (self, min):
    print(str(self.sd)+'GB SD카드에', str(min) +'분 동안 여행모드 ON')
class AdvancedTravelBlackBox (TravelBlackBox):
  def set_travel_mode (self, min):     #method의 정의를 새로 지정해주면 부모 class의 method 덮어쓰기가 됨.
    print(str(self.sd)+'GB SD카드에', str(min) +'분 동안 여행모드 ON')
    self.make()
    self.send()
b2=AdvancedTravelBlackBox ('노랑이', 100000, 128)
b2.set_travel_mode (20)
b1=TravelBlackBox ('하양이', 200000, 64) #결과가 다름
b1.set_travel_mode (10)

# %%  문자열 편집 (format)
# .ljust() 메써드는 모자르는 글자수 만큼 빈칸을 넣어줍니다.
# 줄을 맞춰주기 위해서 .ljust()를 이용해서 빈칸을 넣어줍니다.

print("ABCDEFG".ljust(10))
print("ABCDEFGH".ljust(10))
print("ABC".ljust(10))


print("ABCDEFG".ljust(10), "HIJKLMN".ljust(10))
print("AB".ljust(10), "HI".ljust(10))  #한글에서는 글자간 간격이 달라 작동하지 않는다)
print ('나는 %s를 좋아합니다.' % '피자')
print ('원주율은 %s 입니다' % 3.141592)
print ('원주율은 %d 입니다' % 3.141592) # %d 는 정수
print ('원주율은 %f 입니다' % 3.141592) # %f 는 float
print ('원주율은 %.2f 입니다' % 3.141592) # float 소수점 2자리까지
print ('원주율은 %.4f 입니다' % 3.141592)

print ("{0}|{1}".format("Name", "Count"))
print ("{0:8}|{1:7}".format("Name", "Count"))
print ("{0:8}|{1:7}".format("Mango", 5))
print ("{0:8}|{1:7}".format("Banana", 7))

# <, ^, > : left, center, right
print ("{0:<10}|{1:^10}|{2:>10}" .format ("Left","Center","Right") )  #print 내의 ""내에서는 띄어쓰기도 다 반영됨.
print ("{0:<10}|{1:^10}|{2:>10}" .format ("Lemon","Cherry","Raison") )
# padding character  #빈칸에 채워짐
print ("{0:t<10} | {1:*^10} | {2:_>10}" .format ("Left","Center","Right") )  
print ("{0:=<10} | {1:^10} | {2:.>10}" .format ("Lemon","Cherry","Raison") )

# float precision
# 총 10글자가 되도록 빈칸 추가, 소수점 아래 자리가 4개가 되도록 절삭
print ("The result if {0:10.4f}" .format (123.456789))
print ("The result if {0:10.4f}" .format (1.456789))

# float 정밀도 조절에서 .format()과 f-string의 사용법이 약간 달라요
num = 123.56789
print(str(num))
print("계산 결과:{0:10.4f}".format(num))  # 4는소수점 이하
print(f"계산 결과:{num:{10}.{6}}")  # 10은 빈칸 포함 총 글자수, 6은 출력되는 숫자수
# 요약: f-string에서는 {width}.{precision} 형식으로 float 출력을 조절할 수 있습니다.
print(f"계산 결과:{num:{10}.{7}}")

#%% 바다코끼리 연산자 :=
# 대입과 동시에 그 자체를 '값'으로 사용할 수 있습니다.
(word := "Hello")

#%%
import turtle as t
t.shape ('turtle')
t.forward (100)
t.right(90)
t.forward (100)

#%%
# calendar와 date, time등을 계산하는 calendar, datetime, time module
import calendar
print (calendar.month (2024,2))
for week in calendar.Calendar().monthdayscalendar(2024,2): # 주 단위로 list로 생성, (월요일이 0, 화요일이 1 ...)
    print (week)
  
import datetime
# 현재 날짜와 시간을 출력하고 싶을 경우
print (datetime.datetime.now())

# 날짜와 시간을 따로따로 다룰 수도 있어요
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
print (year, month, day, hour, minute, second)

print (datetime.date (2021,2,28) + datetime.timedelta (days =10))
print (datetime.date (2022,10,30) - datetime.date.today ())
print (datetime.date (2022,9,29) - datetime.date (2022,8,12))

import time
start_time = time.time ()
time.sleep (1.5)  #얼마나 걸리는지 시간을 재고 싶은 일을 여기서 함.
end_time = time.time()
elapsed_time = end_time - start_time
print (elapsed_time)

import datetime  #time과 사용법이 약간 다름
import time
start_time = datetime.datetime.now()
time.sleep (1.5)
end_time = datetime.datetime.now()
print (type (end_time))
elapsed_time = end_time - start_time
print (type(elapsed_time))
print (elapsed_time.total_seconds())



    
# %%
# 숫자 맞추기 게임.
import random

num = random.randint(1, 100)

try_count = 0

while True:
    a = int(input("1부터 100까지의 숫자 중에 하나를 입력하세요"))
    try_count += 1
    if a > num:
        print (f"{a}보다 작습니다")
    elif a < num:
        print (f"{a}보다 큽니다")
    elif a == num:
        print (f"{num}을(를) {try_count}번 만에 맞췄습니다.")
        break
      

#%% 음석인식과 예외처리
import speech_recognition as sr  #python 버전 3.9

# 인식기(Recognizer) 객체를 만듭니다.
r = sr.Recognizer()

# 마이크 객체를 만듭니다. 
# microphone = sr.Microphone(device_index=2)
microphone = sr.Microphone() # 대부분의 경우 device_index 생략 가능합니다.


# 마이크로 음성을 녹음합니다.
# with microphone as source는 microphone 객체를 사용할 준비를 시키고 
# with-블럭 안에서 source라는 이름으로 사용하겠다는 의미입니다.
# 어떤 자료형의 객체가 with문과 같이 사용될 수 있는지 아닌지는 
# 미리 정해져 있기 때문에 보통 예제 코드를 참고해서 사용합니다.
while True:
    with microphone as source:
        r.adjust_for_ambient_noise(source) # 배경 소음을 측정합니다.
        print("음성 인식 대기중")
        audio = r.listen(source) # 일정 크기 이상의 소리가 들리면 녹음합니다.

# with-as 블럭 안에서 정의한 변수인 audio를 블럭 밖에서도 사용할 수 있습니다.
    try:
        text = r.recognize_google(audio, language="ko")
    except sr.UnknownValueError:
        print ("인식할 수 없습니다.") 
    except sr.RequestError as e:
        print ("인식에 문제가 있습니다.", e)
    else:
        print("인식 결과:", text)
        if text =="종료":
            break

#%%  [참고] ```r.reconrd()```를 이용해서 정해진 시간 동안 녹음을 할 수도 있습니다.
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("앞으로 5초 동안 녹음합니다.")
    audio_data = r.record(source, duration=5)

print("녹음이 완료되었습니다. 인식을 시작합니다.")
try:
    text = r.recognize_google(audio_data, language="ko")
except:  # 다양한 예외들을 통틀어서 except 하나로 처리할 수도 있습니다.
    print("음성이 인식되지 않았습니다.")
else:
    print(text)
    
#%%[참고] 아래와 같이 ```sr.AudioFile()```을 이용해서 음성 파일을 읽어들여서 인식할 수도 있습니다.

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("audio_sample.wav") as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language="ko")
except:
    print("음성이 인식되지 않았습니다.")
else:
    print(text)
    
#%% 음성합성 음성을 mp3파일로 저장한후 읽어서 재생
import gtts
from pydub import AudioSegment 
from pydub.playback import play

# 텍스트를 음성으로 바꿉니다.
tts = gtts.gTTS ("안녕하세요? 인공지능입니다.", lang ="ko")

# mp3 파일로 저장합니다.
tts.save ("temp.mp3")

# mp3 파일을 다시 읽어들입니다.
my_sound = AudioSegment.from_mp3 ("temp.mp3")

# 컴퓨터로 재생합니다.
play (my_sound)

#%% 음성합성2 음성을 메모리에 저장후 읽어서 재생
import gtts
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

# 텍스트를 음성으로 바꿉니다.
tts = gtts.gTTS ("안녕하세요? 이제인아빠 이필형입니다.", lang ="ko")
tts1 = gtts.gTTS ("Hi! I am an artificial intelligence.", lang ="ko")

# mp3 오디오 데이터를 메모리에 저장합니다.
fp = BytesIO()
tts.write_to_fp(fp)
fp = BytesIO(fp.getvalue())

# 오디오 데이터를 메모리로부터 가져옵니다.
my_sound = AudioSegment.from_file (fp, format = "mp3")
# 컴퓨터로 재생합니다.
play (my_sound)

#github로 올리기