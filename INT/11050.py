import math
N , K = map(int,input().split())
def combine(a,b):
    result = math.factorial(a)//(math.factorial(b)*math.factorial(a-b))
    return result
print(combine(N,K))