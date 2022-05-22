n = int(input())
arr = list(map(int, input().split()))

result = [-1]*n
stack = []

for i in range(n):
    while(len(stack) != 0 and arr[stack[-1]] < arr[i]):
        result[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*result)




n = int(input())
arr = list(map(int, input().split()))

result = [-1]*n
stack = []

for i in range(n):
    while(len(stack) != 0 and arr[stack[-1]]< arr[i]):
        result[stack[-1]] = arr[stack[-1]]
        stack.pop()
    stack.append(i)

for element in result:
    print(element,end=" ")