list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

while(len(list1) >0):
    list2.append(list1.pop())

print(sorted(list2))