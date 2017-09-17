def factorial(x):
    if x < 1:
        return 1
    else:
        return x * factorial(x - 1)  # Recursive


def factorial2(x):
    k = 1
    for i in range(1, x + 1):
        k *= i
    return k  # for loop

# Main Program
x = int(input("Enter a number : "))

while x != -1:
    if x <= -2:
        print("Error")
        x = int(input("Enter a number : "))
    else:
        print("%d! = %d" % (x, factorial(x)))
        x = int(input("Enter a number : "))
