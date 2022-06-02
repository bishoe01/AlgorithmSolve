import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for i in range(N):
    k = int(sys.stdin.readline())
    if( k !=0 ):
        heapq.heappush(heap, -k)
    else: #0일 때
        if(len(heap)!=0):
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
