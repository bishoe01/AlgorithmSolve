from collections import deque
n, m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
def in_range(x,y):
    return 0<=x and 0<=y and x<n and y<m

def can_go(x,y):
    if(not in_range(x,y)):
        return False
    if(grid[x][y] == 0  or visited[x][y] ==1 ):  #뱀 있어요?
        return False
    return True
def push(x,y,s):
    step[x][y] = s
    visited[x][y] = 1
    q.append((x,y))

def bfs():

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx,dy in zip(dxs,dys):
            next_x,next_y =x + dx, y+dy
            
            if(can_go(next_x,next_y)):
                push(next_x,next_y,step[x][y]+1)

push(0,0,0)
bfs()

print(step[n-1][m-1])