N = input()
arr =[]
for element in N:
    arr.append(element)

arr = sorted(arr,reverse=True)
for element in arr:
    print(element,end="")