import math
N = int(input())
def combine(b,a): ##0<N <= M < 30 이라고 나와있으므로 a,b 위치를 변경해주었다.
    result = math.factorial(a)//(math.factorial(b)*abs(math.factorial(a-b)))
    return result

for _ in range(N):  
    num1, num2 = map(int,input().split())
    print(combine(num1,num2)) 