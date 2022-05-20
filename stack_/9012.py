#9012번 문제
k = int(input())
for _ in range(k):
    arr = []
    tmp = input()
    for element in tmp:
        if(element == "("):
            arr.append(element)
        elif(element == ")"):
            if(len(arr) == 0): ##스택이 비어있을때 Pop이 먹히지 않으므로 예외처리해줌
                print("NO")
                break
            else:
                arr.pop()
    else:            
        if(len(arr) == 0):    
            print("YES")
        else:
            print("NO")
