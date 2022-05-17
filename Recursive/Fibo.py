fibonum = int(input())

def fibo(x):
    if(x == 1 or x == 2): 
        return 1
    elif(x >2):
        return fibo(x-1)+fibo(x-2)
    elif(x ==0):
        return 0
    
print(fibo(fibonum))
