year = 2023 #현재 연도
a = 10
b = 10.0
result = a + b
print(a, b, sep="\n")
print("{0}은 {1}을 잘 합니다".format("lee", "코딩"))
name = "lee"
doing = "코딩"
print(f"{name}은 {doing}을 잘 합니다")

# 윤년의 조건 - 둘 중 하나만 True 이면 True
# 1) 4의 배수이고 100의 배수가 아닌 경우
# 2) 400의 배수인 경우
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    {
        print(year, "는 윤년")
    }
else:
    {
        print(year, "는 윤년이 아님")
    }
help(input)
