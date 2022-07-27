from calendar import c
from dbm import ndbm
from itertools import count
from webbrowser import get


n , m, t = map(int,input().split())
grid = [[0]* (n+1)]
for _ in range(n):
    grid.append([0]+ list(map(int,input().split())))

count_arr = grid.copy()
next_count_arr = grid.copy()
def in_range(x,y):
    return 1<=x and 1<=y and x<=n and y<=n


def get_max(x,y):
    dxs,dys= [-1,1,0,0], [0,0,-1,1]

    max_num ,max_pos = 0 

    for dx,dy in zip(dxs,dys):
        next_x , next_y = x+dx,y+dy

        if(in_range(next_x,next_y) and grid[next_x][next_y] > max_num):
            max_num = grid[next_x][next_y]
            max_pos = (next_x,next_y)

    return max_pos

def move(x,y):
    next_x, next_y = get_max(x,y)
    next_count_arr[next_x,next_y] +=1

def move_all():
    for i in range(1,n+1):
        for j in range(1,n+1):
            next_count_arr[i][j] = 0 
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j] == 1:
                move(i,j)
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            count[i][j] = next_count_arr[i][j]
    
def remove_duple():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j] >=2 :
                count[i][j] = 0 