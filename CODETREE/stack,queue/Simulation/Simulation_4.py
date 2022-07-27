n,m,t = 4, 3, 1

arr = [[0]* (n+1)]
for _ in range(n):
    arr.append([0]* n)

count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

next_count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]




def in_range(x,y):
    return 1<=x and 1<=y and x<=n and y<=n

def max_find(x,y):
    dxs,dys = [-1,1,0,0], [0,0,-1,1]

    max_num, max_pos = 0 , (0,0)

    for dx, dy in zip(dxs,dys):
        next_x , next_y = x+dx, y+dy

        if in_range(next_x,next_y) and arr[next_x][next_y] > max_num: 
            max_num = arr[next_x][next_y]
            max_pos = (next_x,next_y)
    return max_pos

def move(x,y):
    next_x, next_y = max_find(x,y)

    next_count[next_x][next_y] +=1 


def move_all():
    #초기화
    for i in range(1,n+1):
        for j in range(1,n+1):
            next_count[i][j] = 0 

    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j] ==1 :
                move(i,j)

    for i in range(1,n+1):
        for j in range(1,n+1):
            count[i][j] =next_count[i][j]
            
def remove_doble():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(count[i][j] ==2):
                count[i][j] = 0 

def simulate():
    move_all()

    remove_doble()


for _ in range(m):
    x,y = map(int,input().split())
    count[x][y] = 1 
    