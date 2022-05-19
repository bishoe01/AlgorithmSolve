k = int(input())
for _ in range(k):
    arr = []
    tmp = input()
    for element in tmp:
        if(element == "("):
            arr.append(element)
        elif(element == ")"):
            if(len(arr) == 0):
                print("NO")
                break
            else:
                arr.pop()
    else:            
        if(len(arr) == 0):    
            print("YES")
        else:
            print("NO")
