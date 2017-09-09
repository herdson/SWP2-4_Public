def RecurFactorial(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return a*RecurFactorial(a-1)

a = int(input("Input some integer here"))

while a !=-1:
    if a < -2:
        a = int(input("Wrong number. Type again: "))
    else:
        result = RecurFactorial(a)
        print(result)
        a = int(input("Plz input another integer"))
