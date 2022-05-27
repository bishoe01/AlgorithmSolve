from collections import deque
n = int(input())
deck = deque()
priority = 0
for _ in range(n):
    num , target = map(int,input().split())
    deck.append(map(int,input().split()))
    while(True):
        