n,x,y = map(int,input().split())
grid = [[0] * (n+1)]
for _ in range(n):
    grid.append([0] + list(map(int,input().split())))

answer  = []

def in_range(x,y):
    return 1<=x and 1<=y and x<=n and y<=n

def can_go(x,y,current_num):
    return in_range(x,y) and grid[x][y] > current_num


def simulate():
    global x,y 
    dxs,dys= [-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        next_x, next_y = x+dx, y+dy

        if(can_go(next_x,next_y,grid[x][y])):
            x,y= next_x, next_y
            return True
    return False
answer.append(grid[x][y])

while True:
    answer_value = simulate()

    if(not answer_value):
        break
    
    answer.append(grid[x][y])

for element in answer:
    print(element, end=' ')