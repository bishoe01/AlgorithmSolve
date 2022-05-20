while True:
    arr = []
    tmp = input()

    if(tmp == "."):
        break
    
    for element in tmp:
        if(element == '(' or element == '['):
            arr.append(element)
        elif(element == ')'):
            if(len(arr) != 0 and arr[-1] == "("):
                arr.pop()
            else:
                arr.append(')')
                break
        elif(element == ']'):
            if(len(arr) != 0 and arr[-1] == "["):
                arr.pop()
            else:
                arr.append(']')
                break
    if(len(arr) == 0):
        print("yes")
    else:
        print("no")