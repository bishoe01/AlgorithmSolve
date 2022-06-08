import sys
import heapq
n = int(sys.stdin.readline())
heap = [] 
for i in range(n):
    k = int(sys.stdin.readline())
    if( k == 0 ):
        if(len(heap) == 0):
            print(0)
        else : 
            print(heapq.heappop(heap)[1])
    else: #0이 아닌 값이 들어온 경우
        heapq.heappush(heap, (abs(k), k))