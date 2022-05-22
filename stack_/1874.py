n = int(input())

stack , sign , std =[] , [] , 1
result = True
for _ in range(n):
    target = int(input()) #목표로 하는 숫자
    while(std <= target):
        stack.append(std)
        sign.append('+')
        std+=1
    
    if(stack[-1] == target): #목표 값까지 스택에 채워줬을때는 이제 마지막 요소를 삭제해준다 (pop한 것은 상상 속에 스택에 저장한다고 생각)
        stack.pop()
        sign.append('-')
    else:
        result = False
if(result == False):
    print("NO")
else:
    for element in sign:
        print(element)
