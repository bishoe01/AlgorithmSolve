n , m = map(int, input().split())
answer = [[0 for _ in range(m)] for _ in range(n)]

index = 0
for col in range(m):
    if(col % 2 == 0):
        for row in range(n):
            answer[row][col] = index
            index +=1
    else:
        for row in range(n-1, -1, -1):
            answer[row][col] = index
            index+=1

for element in answer:
    for ele in element:
        print(ele,end=" ")
    print()