import sys;
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline()))
m = int(sys.stdin.readline())
for _ in range(m):
    target1, target2 = map(int(sys.stdin.readline().split()))
    B = A[target1-1:target2-1]
    C = [] 
    for i in range(len(B)-1, -1,-1):
        C.append(B[i])

    if(B == C):
        print(0)
    else:
        print(1)
