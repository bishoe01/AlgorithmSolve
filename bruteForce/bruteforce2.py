N = int(input())
Target = 0

for i in range(1,N+1):
    A = list(map(int,str(i)))
    s = i + sum(A)  
    if(N == s):
        Target = i
        break
    
print(Target)   
