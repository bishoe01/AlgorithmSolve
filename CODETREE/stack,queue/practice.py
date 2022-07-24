from math import ceil
n = int(input())
customer = input().split()
L , F = input().split()
L , F = int(L), int(F)
answer = len(customer) #최소 팀장 수 

for element in customer:
    if(L >=element):
        continue
    else: #(팀장 담당할 수 있는 손님보다 손님이 많을 떄)
        element -=L
        tmp = ceil(element/F)
        answer = answer + tmp


print(answer)
