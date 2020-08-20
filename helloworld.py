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
# from random import *

# # print(random()) #0.0 ~ 1.0 미만의 랜덤한 값을 출력한다.
# # print(random() * 10) # 0.0 ~ 10.0 미만의 값 생성

# #     #만일 소수점을 보기 싫을 때
# # print(int(random() * 10)) # 0 ~ 10 미만의 값을 생성

# #     # 만일 숫자 0을 보기가 싫다?
# # print(int(random() * 10 +1))

# #     #만일 로또 처럼 1~45까지의 숫자들을 랜덤으로 뽑아 내고 싶다면?
# # print(randrange(1,46)) # 1~45 이하의 값들 중 랜덤한 값을 출력한다. 46을 포함하지 않는다.
# # print(randint(1,45))   # 1~45 이하의 값들 중 랜덤한 값을 출력한다. 45를 포함한다. 

#     #퀴즈
# print("오프라인 스터디 모임 날짜는 매월" ,randrange(4,29), "일로 선정되었습니다.")
# print("오프라인 스터디 모임 날짜는 매월" ,randint(4,28), "일로 선정되었습니다.")

# 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 어려워요 ㅠㅠ
# """
# print(sentence3)

#슬라이싱
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  # 0부터 2직전 까지 즉 0과 1을 의미한다. 
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) #처음부터 6직전까지의 값을 의미한다. 
# print("뒤 7자리 : " + jumin[7:14])
# print("뒤 7자리 : " + jumin[7:]) #7번째 부터 마지막까지의 값을 의미한다.  
# print("뒤 7자리 : " + jumin[-7:]) #가장 뒤에 숫자가 -1번째 이다. 즉 맨뒤에서 7번째 부터 출력

#문자열 처리 함수
# python = "python is Amazing"
# print(python.lower())                     #전부 대문자로 출력
# print(python.upper())                     #전부 소문자로 출력
# print(python[0].isupper())                #0번째가 대문자인가
# print(len(python))                        #python 이라는 변수의 길이는 몇인가
# print(python.replace("python", "java"))   #python 이라는 단어를 java로 변경

# index = python.index("n")                 #n이 처음 나오는 위치를 찾는다.
# print(index)                              #5출력
# index = python.index("n", index + 1)      #n이 처음 나오는 위치를 찾는데 index + 1인 값 부터 시작 즉 index = 5이고 + 1이므로 6부터 시작하여 n이 있는 위치 출력
# print(index)                              #15출력

# print(python.find("java"))                #원하는 값이 없으면 -1 출력. 뒤에 계속 다른 것들이 나오면 프로그램은 계속 돌아간다. 
# # print(python.index("java"))               #원하는 값이 없으면 오류가 출력되어 버린다. 그리고 프로그램이 종료 되어 버린다.
# print(python.count("n"))                  #n이 몇번 찍히는지 출력한다.



