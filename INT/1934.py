from cgitb import reset


def gcd(x,y):
    if( y== 0 ):
        return x;
    else:
        return gcd(y,x%y)

def lcm(x,y):
    result = (x*y) // gcd(x,y)
    return result

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    print(lcm(a,b))