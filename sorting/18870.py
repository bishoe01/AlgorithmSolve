N = int(input())
arr = list(map(int,input().split()))

priority = [0]*(len(arr)) ##순위배열 

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i] > arr[j]):
            priority[i]+=1
        elif(arr[i] == arr[j]):
            continue
        else:
            priority[j]+=1

for element in priority:
    print(element,end=" ")