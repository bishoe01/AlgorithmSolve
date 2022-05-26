from collections import deque
from unittest import result
n , k = map(int,input().split())
arr = deque([])
answer = []
for i in range(n):
    arr.append(i+1)

while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    answer.append(arr.popleft())

print("<", end="")
for i in range(len(answer)-1):
    print(answer[i], end=", ")
print(answer[-1],end="")
print(">")