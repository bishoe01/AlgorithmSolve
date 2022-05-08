import sys

N = int(input())
arr = [0]*10001
for i in range(N):
    tmp = int(sys.stdin.readline())
    arr[tmp] +=1

for i in range(len(arr)):
    if(arr[i] !=0):
        for j in range(arr[i]):
            print(i)
