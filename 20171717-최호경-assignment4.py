import time

def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)



def fnr(n):
    res = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(2,n+1):
            ko = i
            res = res*(ko)
        return res










start=time.time()
f(20)
end=time.time()
print("재귀적 팩토리얼 알고리즘의 소요시간입니다.",end-start)

interstart=time.time()
fnr(20)
interend=time.time()
print("반복문 팩토리얼 알고리즘의 소요시간입니다.",interend-interstart)

print(f(20))
print(fnr(20))