

#N W E S
dx= [0,-1, 1, 0]
dy =[-1, 0 ,0, 1]

n = int(input())
ans = -1
x,y = 0, 0
t = 0 #카운팅

def move(move_dir, dist):
    global x,y    
    global ans, t 

    for _ in range(dist):
        x,y = x 