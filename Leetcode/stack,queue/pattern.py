import sys
N , M = map(int,sys.stdin.readline().split())
box = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    box[x][y] = 1 
    if(x == 1 or x== N):  #첫줄과 네번째 줄
        if(y==1 and y ==N):
            print(0)
        else: #y가 2부터
            if(x==1):
                if(box[x+1][y] == 1 and box[x][y-1] ==1 and box[x][y-1] ==1 ):
                    print(1)
                else:
                    print(0)
            elif(x==N):
                if(box[x-1][y] == 1 and box[x][y-1] ==1 and box[x][y+1] ==1 ):
                    print(1)
                else:
                    print(0)

    elif(x>1 and x<N):
        if(y==1 and y ==N):
            if(y==1):
                if(box[x-1][y] == 1 and box[x+1][y] ==1 and box[x][y+1] ==1 ):
                    print(1)
                else:
                    print(0)
            elif(y==N):
                if(box[x-1][y] == 1 and box[x+1][y] ==1 and box[x][y-1] ==1):
                    print(1)
                else:
                    print(0)
        else:
            if((box[x-1][y] + box[x+1][y] + box[x][y-1] + box[x][y+1])==3):
                print(1)
            else:
                print(0)
        

                    
            
        