#%%
print (2**3) # 2^3=8
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

snack = '꿀꽈배기는\n너무\n맛있어요' #탈출문자로 줄바꾸기 \n
print (snack)

# %%
#list [] 사용
my_list = ['오예스','몽쉘','초코파이'] #list는 순서가보장
print (my_list[0]) #리스트내에 해당하는 값 출력
print ('몽쉘' in my_list) #리스트에 포함되어 있는지 in
print (len(my_list)) #list에 몇개가 포함
my_list[0] = '몽쉘카카오' #list 수정하기
my_list.append ('박파이') #list 에 값추가
my_list.remove ('몽쉘')  #list 에서 값빼기
del my_list ['초코파이']
your_list=['빅파이','오뜨']
print(my_list + your_list) #list와 list합치기
your_list.extend(my_list) #your list 뒤에 my list넣어서 확장시키기, your list정의가 바뀜
print (your_list)
print (your_list [2:5]) #list의 2,3,4를 보여달라, 프로그램은 실제 0에서 시작하여 numbering

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
print(A.union(B)) #순서는 보장안됨 #합집함
print(A.difference(B)) #차집합
# print(A[0]) #순서가 보장되지 않으므로 index사용해서 명령불가
A.add('닭갈비')
print (A)
A.remove('보쌈')
print(A)
A.clear() #set내의 모든 값 지우기
print (A)
del A # A set자체를 완전 삭제
print (A)

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
# list comprehension


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
def get_price (is_vip=False, is_birthday=False, is_membership=False, card=False, review=False, first_time=False)
# 여러개의 기본값들 중 한개를 바꿀때는 그 전달값만 딱 적으면 됨.
def get_price(review=True, is_birthday=True)


# %%  
import random
computer = random.randint(0,10)  #0,10 사이의 정수를 랜덤으로 뽑아서 줌.
computer

# %%
# 가변인자: 갯수가 바뀔수 있는 인자, 전달값 앞에 * 붙여주면 됨 -- tuple 형태로 받음.
def visitors (today, *customers): # 가변인자는 한 함수에 한번만 사용가능
  print (today)
  for customer in customers:
    print (customer)
visitors ('2022년 9월 1일','이필형','나정화')
    
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
