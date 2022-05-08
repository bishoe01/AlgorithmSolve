N = int(input())
B = []
for i in range(1,N+1):
    w,h = map(int,input().split())    
    B.append((w,h))  #튜플리스트 작성까지는 옳았다. 
for i in B: 
    rank = 1
    for j in B:
        if (i[0]< j[0] and i[1]<j[1]):
            rank+=1
    print(rank,end=" ")