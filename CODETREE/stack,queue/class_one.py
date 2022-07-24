
n = int(input())

dx, dy= [-1,0,0,1],[0,-1,1,0]

D = {"W": 0, "S": 1, "N":2, "E":3}

x,y = 0 , 0 
for _ in range(n):
    direction , move = input().split()
    
    dir_num = D[direction]
    
    x += dx[dir_num] * int(move)
    y += dy[dir_num] * int(move)
print(x,y)