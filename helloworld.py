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

#     #퀴즈 2
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
# # print(python.index("java"))             #원하는 값이 없으면 오류가 출력되어 버린다. 그리고 프로그램이 종료 되어 버린다.
# print(python.count("n"))                  #n이 몇번 찍히는지 출력한다.

#문자열 포맷
# print("a" + "b")       #이러한 방법 말고
# print("a", "b")        #이러한 방법 말고

#     #방법 1   이런식으로 %d는 숫자 %s는 문자로 사용 가능하다. 
# print("나는 %d 살입니다." % 20)                    #integer 정수만 가능
# print("나는 %s을 좋아해요" % "파이썬")               #string 문자열만 가능
# print("Apple 은 %c로 시작해요." % "A")             #char 문자만 가능
# print("나는 %s 색과 %s 색을 좋아해요." % ("파란", "삘긴"))

#     #방법 2 {} 사용하는 방법
# print("나는 {} 살입니다." .format(20))
# print("나는 {}색과 {} 색을 좋아해요." .format("파란", "빨간"))            
# print("나는 {0}색과 {1} 색을 좋아해요." .format("파란", "빨간"))         #순서 지정 기능
# print("나는 {1}색과 {0} 색을 좋아해요." .format("파란", "빨간"))         #순서 지정 기능

#     #방법 3
# print("나는 {age} 살이며, {color} 색을 좋아해요." .format(age = 20, color="빨간"))
# print("나는 {age} 살이며, {color} 색을 좋아해요." .format(color="빨간", age = 20))

#     #방법 4 (python v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age} 살이며, {color} 색을 좋아해요.")       #오 신기하다 age랑 color 변수를 알아서 찾아 쓰네

#탈출 문자
# print("백문이 불여일견 \n백견이 불여일타")
#     # 저는 "나도 코딩" 입니다.  이렇게 출력을 하고 싶다면
# print('저는 "나도 코딩" 입니다.')                       #이렇게 하면 된다. 
# print("저는 \"나도코딩\" 입니다.")                      #혹은 이렇게 \" 으로 감싸주면 되는군
# print('저는 \"나도 코딩\" 입니다.')

# print("저는 '나도 코딩' 입니다.")
# print('저는 \'나도 코딩\' 입니다.')
# print("저는 \'나도 코딩\' 입니다.")

#     # \\ :  문장 내에서 \ 하나로 취급한다. 
# print("c:\\User\\Desktop\\huya")                   #c:\User\Desktop\huya    이렇게 출력된다. 

#     # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPineWa ")                          # \r을 만나면 맨 앞으로 커서가 이동하여 거기서 부터 다시 출력을 하는 것
#                                                      # 실행 결과는 PineWa le 이다.

#     # \b : 백스페이스 (한 글자 삭제)
# print("Redd\b Apple")                                #d 하나가 삭제된다.

#     # \t : 탭 기능
# print("Red\tApple")                                    #Red와 Apple 사이에 탭을 누른 효과를 나타냄

    #퀴즈 3 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하기오
    # 예) http://naver.com
    #규칙1: http://부분은 제외 => naver.com
    #규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
    #규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
    #           (nav)              (5)           (1)        (!)
    #예) 생성된 비밀번호 : nav51!

#     #나의 풀이
# site = "http://naver.com"
# print(site[7:10] +  str(site.index(".") - 7) + str(site.count("e")) + "!")

#     #수업에서의 풀이

# url = "http://naver.com"
# my_str = url.replace("http://", "")    #규칙1 : 앞 부분 삭제
# my_str = my_str[:my_str.index(".")]    #규칙2 : my_str[0:5] naver만 따오게 된것
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트 

# subway = ["유재석", "조세호", "박명수"]           
# print(subway)                                #결과는 ['유재석', '조세호', '박명수']

#     #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))                  #결과는 1

#     #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")                          #append는 더하는 기능이다.
# print(subway)                                 #결과는 ['유재석', '조세호', '박명수', '하하'] 

#     #정형돈씨를 유재석씨와 조세호씨 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

#     #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)                                    #여기까지 하면 배열이 텅 비어버린다.
# subway.pop()                                     #여기서 부터는 오류가 발생하게 된다 아무것도 없는데 빼야하기 때문
# print(subway)

#     #같은 이름의 사람이 몇명 있는지 확인하기
# subway.append("유재석")                            #중복된 이름을 위해 유재석 추가
# print(subway)          
# print(subway.count("유재석"))                      #유재석이라는 이름이 몇번 중복되었는가?

#     #순서 정렬도 가능
# num_list = [5,4,3,2,1]
# num_list.sort()                                      #1,2,3,4,5 로 정렬
# print(num_list)

#     #순서 뒤집기도 가능
# num_list.reverse()
# print(num_list)                                      #5,4,3,2,1 로 정렬

#     #다양한 자료형과 함께 사용 가능
# mix_list = ["조세호", 20, True]                       #자료형의 형태와 상관 없이 섞어서 사용 가능
# print(mix_list)     

#     # 리스트 확장 (두 리스트를 합치는 기능) -.extend-
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list)                             #[5, 2, 4, 3, 1, '조세호', 20, True] 두 리스트를 묶음
# print(num_list)

# 사전
# cabinet = {3: "유재석", 100:"김태호"}                      #3번 열쇠를 유재석씨가 받고 100번 열쇠를 김태호씨가 받는다고 생각해보자
# print(cabinet[3])                                       #3번 열쇠를 출력하면 유재석이 출력되게 된다. 
# print(cabinet[100])                                     #100번 열쇠를 출력하면 김태호가 출력되게 된다.

# print(cabinet.get(3))                                   #print(cabinet[3])과 같은 결과
# print(cabinet.get(100))                                 #print(cabinet[100])과 같은 결과

# print(cabinet[5])                                       #cabinet안에 5라는 키가 없기 때문에 오류 발생 프로그램 멈춤
# print(cabinet.get(5))                                   #이번의 경우에는 오류 발생 없이 None이라고 출력됨.
# print(cabinet.get(5, "사용가능"))                         #None 출력 대신 다른 언급을 하고 싶을 경우?

# print(3 in cabinet)                                     #3이라는 열쇠가 cabinet 안에 있으면 true 출력
# print(5 in cabinet)                                     #5라는 열쇠가 cabinet 안에 없기 때문에 false 출력

#     #또한 string도 키로 사용가능
# cabinet = {"A-3": "유재석", "B-100":"김태호"} 

#     #만일 새손님이 왔다면
# print(cabinet)
# cabinet["C-20"] = "조세호"                                 #원래 부터 없었다면 새로 추가 원래 있던 키였으면 업데이트
# cabinet["A-3"] = "김종국"                                  #원래 부터 없었다면 새로 추가 원래 있던 키였으면 업데이트

# print(cabinet)

#     #손님이 간 경우
# del cabinet["A-3"]
# print(cabinet)

#     #key들만 출력하고 싶은 경우
# print(cabinet.keys())

#     #value들만 출력하고 싶은 경우
# print(cabinet.values())

#     #key, value 쌍으로 출력하고자 하는 경우
# print(cabinet.items())

#     #cabinet 비우기
# cabinet.clear()
# print(cabinet)                                           #다 비어 있기 때문에 {}으로 출력된다.
# print(cabinet.clear())                                   #None으로 출력된다. (차이점이 뭘까..?)

# 튜플 (배열과 같은 기능)
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

#     # 단 menu.add("생선까스")와 같이 add 기능은 없다.
#     # 선언 방식에 대하여
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
# (name,age,hobby) = ("김종국",20,"코딩")                      #위처럼 하나하나 변수 선언 해서 할 수도 있지만 이 처럼 한번에 다 지정할 수 있다.
# print(name, age, hobby)

# 집합 (set)
# 특징 : 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3}                                        # 중복이 되지 않는다.
# print(my_set)                                               # 따라서 3이 반복 출력되지 않는다.

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

#     #교집합 (java와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

#     # 합집합 (java를 할 수 있거나 python도 할 수 있는 개발자)
# print(java | python)                                        # {'박명수', '김태호', '유재석', '양세형'} 순서는 보장되지 않는다.
# print(java.union(python))                                   # {'박명수', '김태호', '유재석', '양세형'} 순서는 보장되지 않는다.

#     # 차집합(java는 할 줄 알지만 python을 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))

#     # python을 할 줄 아는 사람이 늘어남 python에 추가하고 싶은 경우
# python.add("김태호")
# print(python)

#     # java를 잊었어요 java의 원소 중 하나를 제거하고 싶을 때
# java.remove("김태호")
# print(java)

# #자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))                                   #set이므로 {  }로 표현됨.

# menu = list(menu)                                         #menu의 타입을 list로 만듬
# print(menu, type(menu))                                   #list이므로 [  ]로 표현됨.

# menu = tuple(menu)                                        #menu의 타입을 tuple로 만듬
# print(menu, type(menu))                                   #tuple이므로 (  )로 표현됨.

# menu = set(menu)                                          #menu의 타입을 set으로 만듬
# print(menu,type(menu))

# #퀴즈
# #문제 풀이 (아직 나는 갈길이 멀었구나...)
# from random import *
# users = range(1,21)
# users = list(users)
# shuffle(users)
# winners = sample(users, 4)
# print("치킨 당첨자 {0}".format(winners[0]))
# print("커피 당첨자 {0}".format(winners[1:4]))