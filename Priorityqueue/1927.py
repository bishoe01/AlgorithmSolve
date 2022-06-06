import sys
import heapq
n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if(k != 0):
        heapq.heappush(heap, k)
    
    else:
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap))
