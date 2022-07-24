n = int(input())

arr = [ list(map(int,input().split())) for _ in range(n)]
dxs = [0,0,-1,1]
dys = [1,-1,0,0]
ans = 0 

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in zip(dxs,dys):
            x = i + dx
            y = j + dy
            if (0<= x and x<n and 0 <= y and y < n):
                cnt += arr[x][y]
        if cnt>=3:
            ans += 1

print(ans)