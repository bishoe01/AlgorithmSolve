N , M = map(int,input().split())

arr = []
cnt =[]
for i in range(N):
    arr.append(input())

for i in range(N-7):
    for j in range(M-7):
        B_first = 0
        W_first = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(k+l)%2==0: 
                    if(arr[k][l]=="B"): B_first+=1
                    if(arr[k][l]=="W"): W_first+=1
                else:
                    if(arr[k][l]=="W"): B_first+=1
                    if(arr[k][l]=="B"): W_first+=1
        cnt.append(B_first)
        cnt.append(W_first)

print(min(cnt))


