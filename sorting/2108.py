import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)
arr = sorted(arr)
result = Counter(arr)
if(len(arr)>1):
    if(result.most_common(2)[0][1] == result.most_common(2)[1][1]):
        mostcommontInt = result.most_common(2)[1][0]
    else:
        mostcommontInt = result.most_common(2)[0][0]
else:
    mostcommontInt = arr[len(arr)-1]    


print(round(sum(arr)/N)) #산술평균
print(arr[len(arr)//2])
print(mostcommontInt) # 최빈값


print(max(arr)-min(arr)) #범위