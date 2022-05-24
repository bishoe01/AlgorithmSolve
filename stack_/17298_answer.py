n = int(input())
arr = list(map(int, input().split()))
result = [-1]*n
stack = []
for i in range(n):
    while(len(stack) != 0 and arr[stack[-1]] < arr[i]):
        result[stack[-1]] = arr[i]
        print(stack[-1], "stack[-1]")
        stack.pop()
    stack.append(i)
    print(*stack)
print(*result)
