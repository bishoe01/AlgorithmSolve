from collections import deque
n , m = map(int, input().split()) 
target = list(map(int,input().split())) 
arr = deque([i for i in range(1,n+1)]) #덱에 1부터 n까지 차례대로 증가하는 원소를 넣어줌
cnt = 0  #정답 카운트

for element in target : #찾아야하는 원소들을 리스트 반복문에 넣어줄 것이다. 
    while True:
        if(arr[0] == element):
            arr.popleft() #찾으면 원소제거 후 다음 원소로 넘어가야함 
            break
        else:
            if(arr.index(element) <= len(arr)//2): #이부분이 핵심 찾을 원소가 절반기준으로 판단하여 뒤애서 앞으로 땡겨줄지, 뒤로 돌려줄지 판단
                arr.rotate(-1) #arr.append(arr.pop())  
                cnt += 1
            else:
                arr.rotate(1)  #arr.appendleft(arr.popleft()) 
                cnt+=1
print(cnt)