nums = list(map(int,input().split()))
ans = 1
cnt = 0
answer= []
while(True):
    if(cnt == len(nums)):
        break
    tmp = nums.copy() ## 1 ,2 , 3 ,4
    tmp.pop(cnt) # 1, 3, 4 
    for element in tmp:
        ans = ans * element  #1, 3, 4
    answer.append(ans) 
    cnt +=1
    ans = 1;
print(answer)
    