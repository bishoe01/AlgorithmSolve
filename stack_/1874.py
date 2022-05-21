n = int(input())
stack , sign, find = [], [] , True
std = 1

for _ in range(n):
    target = int(input())
    while(std <= target):
        stack.append(std)
        sign.append('+')
        std += 1
    
    if(stack[-1]== target):
        stack.pop()
        sign.append('-')
    else:
        find= False
if not find :
    print("NO")
else:
    for i in sign:
        print(i)