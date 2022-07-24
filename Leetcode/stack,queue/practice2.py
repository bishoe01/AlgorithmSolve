n = int(input())
arr = list(map(int,input().split()))
again = -1

for element in arr:
    if(element > again):
        again =element
    elif(element  again):
        again.pop(again.index(element))
if(again == null):
    print(-1)
else:
    print(max(again))