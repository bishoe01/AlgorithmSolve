def gcd(a,b):  ##gcd를 통해서 최소공배수를 구해준다.
    if( a== 0 ):
        return b;
    else:
        return gcd(a,a%b)

def lcm(x,y): ##lcm을 통해서 최대공약수 구해주기
    result = (x*y) // gcd(x,y)
    return result

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    print(lcm(a,b))