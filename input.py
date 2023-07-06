name = input("이름을 입력하세요 : ")
print(name)
#age = input("나이를 입력하세요 : ")
#print(age + 1) #input은 문자열로 받으므로 에러 발생.

#나이를 int로 변환하면 문자를 입력했을 때 에러가 생길 수 있음.
try:
    age = int(input("나이를 입력하세요 : "))
    print(age + 1) #int 형으로 받기 때문에 처리 가능
except: #예외 처리 부분
    print("문제 발생!")


try:
    numbers = input("숫자를 , 로 구분해서 입력해주세요").split(", ")
    for number in numbers:
        print(number)
except:
    print("에러 발생")

print("프로그램 종료")