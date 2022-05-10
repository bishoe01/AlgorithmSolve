num = int(input())

for _ in range(n):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input())
    if n>1 :
        for i in range(n-1):
            cnt_0[i] = cnt_1[-1]
            cnt_1[-1] = cnt_0[-1] + cnt_1[-1]
