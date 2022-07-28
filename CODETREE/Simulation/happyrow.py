n , m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
tmp = [ 0 for _ in range(n)]

def is_happy():
    max_cnt, continue_cnt = 1,1
    for i in range(1,n):
        if(seq[i-1] == seq[i]):
            continue_cnt +=1
        else:  #연속이 끊김 
            continue_cnt = 1
    
    max_cnt = max(max_cnt,continue_cnt)
    return max_cnt>=m
    

answer_cnt = 0

#행만 판단 row
for i in range(n):
    seq = grid[i][:]
    if(is_happy()):
        answer_cnt+=1


for i in range(n):
    for j in range(n):
        seq[j] = grid[j][i]
    
    if(is_happy()):
        answer_cnt+=1
print(answer_cnt)





