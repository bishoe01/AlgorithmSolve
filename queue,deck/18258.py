#FIRST IN FIRST OUT , QUEUE
import sys
n = int(input())
arr = []
for i in range(n):
    command = sys.stdin.readline().split()
    if(command[0] == 'push'):
        arr.append(command[1])
    elif(command[0] == 'front'):
        if(len(arr) == 0):        
            print(-1)
        else:
            print(arr[0])
    elif(command[0] == 'back'):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])
    elif(command[0] == 'pop'):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr.pop(0))
    elif(command[0] == 'size'):
        print(len(arr))
    elif(command[0] == 'empty'):
        if(len(arr) == 0):
            print(1)
        else:
            print(0)