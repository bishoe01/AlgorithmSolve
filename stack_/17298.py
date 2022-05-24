n = int(input())
arr = list(map(int,input().split()))
tmp = 0;
result = []

for i in range(n):
    if(i == n-1 ):
        result.append(-1)
        break
    for k in range(i+1,n):
        if(arr[i] < arr[k]):
            tmp = arr[k]
            break
        else:
            continue
    if(tmp != 0):
        result.append(tmp)
    else:
        result.append(-1)

for element in result:
    print(element,end=" ")