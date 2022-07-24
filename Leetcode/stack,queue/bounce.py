n,t = map(int,input().split())
x,y,d  = input().split()

dx = [1 ,0 ,0, -1]
dy = [0, 1,-1, 0]


cmd = {
    "D": 0,
    "R": 1,
    "L": 2,
    "U": 3
}
x,y,direction= int(x), int(y), cmd[d]

for _ in range(t):
    nx,ny = x + dx[direction], y+ dy[direction]
    if(1<=nx and nx<=n and 1<=ny and ny<=n):
        x,y = nx,ny
    else:  
        direction = 3-direction

print(x,y)