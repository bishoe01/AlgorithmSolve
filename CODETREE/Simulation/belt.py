n, t  = map(int,input().split())
belt = [
    list(map(int,input().split()))
    for _ in range(2)
] 
for _ in range(t):
    tmp1 = belt[0][n-1]
    tmp2 = belt[1][n-1]

    for i in range(n-1,0,-1):
        belt[0][i]= belt[0][i-1]
        belt[1][i]= belt[1][i-1]
    belt[0][0] = tmp2
    belt[1][0] = tmp1
for element in belt:
    for ele in element:
        print(ele ,end=" ")
    print()