N = int(input())
arr = []
for i in range(N):
    arr.append(input())
arr = set(arr)
newarr= list(arr) ##중복없애주기 

newarr.sort(key=lambda x:(len(x),x))

for element in newarr:
    print(element)