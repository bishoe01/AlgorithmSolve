from collections import deque
n , m = map(int, input().split())

target = list(map(int,input().split()))
arr = deque([i for i in range(1,n+1)])
cnt = 0 

for element in target:
    while True:
        if(arr[0] == element):
            arr.popleft()
            break
        else:
            if(arr.index(element) <= len(arr)//2):
                arr.rotate(-1)
                cnt += 1
            else:
                arr.rotate(1)
                cnt+=1

print(cnt)