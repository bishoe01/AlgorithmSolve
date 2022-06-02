from collections import deque
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    is_error = False
    command = sys.stdin.readline().rstrip()
    num_e = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    array =deque(arr)
    cnt = 0 #R이 몇번나오는지 카운트
    if(num_e ==0 ):
        array = []
    for element in command:
        if(element == "R"): #ROTATE
            cnt+=1
        elif(element == "D"): #첫번쨰 버리기 
            if(len(array) !=0):
                if(cnt %2 == 0):
                    array.popleft()
                else:
                    array.pop()
            else:
                is_error = True
                print("error")
                break
    if(is_error==False):
        if(cnt %2 == 0):
            print("[" + ",".join(array) + "]")
        else:
            array.reverse()
            print("[" + ",".join(array) + "]")