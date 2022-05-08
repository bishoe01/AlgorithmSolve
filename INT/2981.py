import sys

def gcd(a,b):  ##gcd를 통해서 최소공배수를 구해준다.
    if( a== 0 ):
        return b;
    else:
        return gcd(a,a%b)
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for _ in range(n)])

result = []
for i in range(1, len(a)):
    result.append(abs(a[i]-a[i-1]))

