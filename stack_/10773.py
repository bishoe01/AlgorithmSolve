k = int(input())
arr = []
for _ in range(k):
    tmp = int(input())
    if(tmp == 0):
        arr.pop()
    else:
        arr.append(tmp)

print(sum(arr))