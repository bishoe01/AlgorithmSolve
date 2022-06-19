#1655번 문제
import sys
import heapq
n = []
target = []
num  = int(input())
for i in range(1,num-1):
    n.append(int(sys.stdin.readline()))
    if(len(n) == 0):
        print(n[0])
    else: #길이가 1이상
        if(n[i] <= n[0]):
            