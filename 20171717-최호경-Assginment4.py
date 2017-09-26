import time

def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1)+f(n-2)
def fnr(n):
    if n==1 or n==2:
        return 1
    elif n>=3:
        sum=0
        Aone=1
        Atwo=1
        for i in range(n-2):
            sum=Aone+Atwo
            Atwo=Aone
            Aone=sum
        return sum






start=time.time()
f(7)
end=time.time()
print("재귀적 피보나치 함수의 소요시간입니다.",end-start)

interstart=time.time()
fnr(7)
interend=time.time()
print("반복문 피보나치 함수의 소요시간입니다.",interend-interstart)
