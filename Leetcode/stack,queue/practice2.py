import math
from collections import Counter
a, b = map(int,input().split())
standard = [ ]
#나눈 값  # 나눈 몫 



while True:
    std = a%b
    a = a//b
    standard.append(std)
    if(a == 0 ):
        break
print(standard)

print(list(set(standard)))
# C = Counter(standard)
# print(C[2]) 

##카운터에 저장을 해놓고 중복을 제거한 뒤, 원소 반복문 돌려서 곱해줌