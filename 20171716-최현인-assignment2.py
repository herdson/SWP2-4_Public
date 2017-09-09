def Factorial():
    def Fact(a, b):
        if a == 0:
            return(b)
        if a > 0:
            b *= a
            return Fact(a-1, b)

    n = int(input("Enter a Number : "))
    m = 1

    if n < -1 or n == 0:
        print("양수인 정수를 입력해주세요.")
        return Factorial()

    if n == -1:
        return("종료합니다.")

    print(n,"! = ", Fact(n, m))

    return Factorial()
print("팩토리얼 계산기 입니다. 종료를 원하시면 -1을 입력해 주세요.")
print(Factorial())