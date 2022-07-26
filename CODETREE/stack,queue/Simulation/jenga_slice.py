n = int(input())
arr = [int(input()) for _ in range(n)]

        
for _ in range(2):
    s,e = map(int,input().split())
    del arr[s-1:e]

print(len(arr))
for element in arr:
    print(element)
