N = int(input())
arr = []
#좌표를 받아야함 
for i in range(N):
    x, y = map(int,input().split()) 
    arr.append((x,y))
    # 좌표값 저장 튜플리스트

arr.sort(key=lambda x:(x[1],x[0]))

for i in arr:
    print(i[0], i[1])  

                
