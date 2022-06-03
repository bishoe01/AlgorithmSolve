import sys
import heapq
N = int(sys.stdin.readline()) #input보다 훨씬 처리속도가 빠름 
heap = [] #heap 생성 
for i in range(N):
    k = int(sys.stdin.readline()) 
    if( k !=0 ):
        heapq.heappush(heap, -k) #pop해줄때 작은값을 구해주기 때문에 넣어줄 때 -를 곱해서 넣어준다. 
    else: #0일 때
        if(len(heap)!=0):
            print(-1 * heapq.heappop(heap))  #pop해줄때는 -가 곱해진 값에서 다시한번 -를 빼줘서 양수로 나와주게 한다. 
        else:
            print(0)
