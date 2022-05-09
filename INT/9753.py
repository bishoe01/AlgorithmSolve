N = int(input())

for i in range(N):
    testcase = int(input())
    dict ={}
    for _ in range(testcase):
        category, cloth = map(str, input().split())
        dict[category] = cloth
        
print(dict)