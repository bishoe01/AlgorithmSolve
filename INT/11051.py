import math
N , K = map(int,input().split())
def combine2(a,b):
    result = math.factorial(a)//(math.factorial(b)*math.factorial(a-b))
    return result%10007
print(combine2(N,K))