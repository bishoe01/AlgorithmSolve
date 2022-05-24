#FIRST IN FIRST OUT , QUEUE
import sys
from collections import deque
n = int(input())
arr = deque([])
for i in range(n):
    command = sys.stdin.readline().split()
    if(command[0] == 'push'):
        arr.append(command[1])

    elif(command[0] == 'front'):
        if(len(arr) != 0):        
            print(arr[0])
        else:
            print(-1)

    elif(command[0] == 'back'):
        if(len(arr) != 0):
            print(arr[-1])
        else:
            print(-1)

    elif(command[0] == 'pop'):
        if(len(arr) != 0):
            print(arr.popleft())
        else:
            print(-1)
    elif(command[0] == 'size'):
        print(len(arr))
    elif(command[0] == 'empty'):
        if(len(arr) == 0):
            print(1)
        else:
            print(0)