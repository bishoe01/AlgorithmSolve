n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
def cnt_grid(row,row_e,col,col_e):
    num_of_gold = 0
    for i in range(row,row_e+1):
        for j in range(col,col_e+1):
            num_of_gold += grid[i][j]
    return num_of_gold;
max_gold = 0

for row in range(n-2):
    for col in range(n-2):
        num_of_gold = cnt_grid(row,row+2,col,col+2)

        max_gold = max(num_of_gold,max_gold)

print(max_gold)
