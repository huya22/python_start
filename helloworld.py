# print(5.3+2.1)
# print(5*2)
# print(3*(3+1))
# print('아니 나보고 어쩌라고')
# print("개빡치네 진짜")
# print("ㅋ"*9)
# print(5>10)
# print(5>1)
# print(not True)
# print (not (5>10))

# #애완 동물을 소개해 주세요~     
# animal="강아지"
# name ="연탄이"
# age = 1 
# hobby = "산책"
# is_adult = age >= 3

# print("우리집" , animal , "의 이름은 " , name , "이에요")              # +는 문자형만 출력된대
# print(name + "이는 " ,age , "살이며, " + hobby + "을 아주 좋아해요")    # ,는 구별 없이 전부 가능 단 띄어쓰기가 기본적으로 하나 포함 되어 있어
# print(name + "는 어른일까요?" + str(is_adult))


# #주석처리
#     '''
#     여러 
#     문장에 대해
#     주석 처리
#     하는 방법
#     '''
#     #한문장 한문장 주석 처리 하는 방법

# station = "사당"
# print(station, "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station, "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station, "행 열차가 들어오고 있습니다. ")

#연산자
# print(not (1 != 3))
#     #print(!(1 != 3))은 틀린 문법이다. 

# print((3 > 0) and (3 < 5))
#     #print((3 > 0) & (3 < 5))와 같은 문법이다. 

# print((3 > 0) or (3 > 5))
#     #print((3 > 0) | (3 > 5))

# print(5 > 4 > 3) #5 > 4이고 4 > 3 이므로 True가 출력 된다!! 신기하네

#간단한 수식

#숫자 처리 함수
#     #절대값
# print(abs(-5))  #5
# print(pow(4,2)) #4^2 = 4*4 =16
#     # print(4**2) 이랑 똑같은 결과를 나타내네
# print(max(5,12)) #최대값 출력
# print(min(5,12)) #최소값 출력
# print(round(3.14)) # 3 반올림
# print(round(4.99)) # 5 반올림

# from math import *  #math 라이브러리의 모든 것들을 불러 오겠다
# print(floor(4.99)) # 4 내림
# print(ceil(3.14))  # 4 올림
# print(sqrt(16))   # 4 제곱근

#랜덤 함수
from random import *

# print(random()) #0.0 ~ 1.0 미만의 랜덤한 값을 출력한다.
# print(random() * 10) # 0.0 ~ 10.0 미만의 값 생성

#     #만일 소수점을 보기 싫을 때
# print(int(random() * 10)) # 0 ~ 10 미만의 값을 생성

#     # 만일 숫자 0을 보기가 싫다?
# print(int(random() * 10 +1))

#     #만일 로또 처럼 1~45까지의 숫자들을 랜덤으로 뽑아 내고 싶다면?
# print(randrange(1,46)) # 1~45 이하의 값들 중 랜덤한 값을 출력한다. 46을 포함하지 않는다.
# print(randint(1,45))   # 1~45 이하의 값들 중 랜덤한 값을 출력한다. 45를 포함한다. 

    #퀴즈
print("오프라인 스터디 모임 날짜는 매월" ,randrange(4,29), "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월" ,randint(4,28), "일로 선정되었습니다.")
