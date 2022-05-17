num = int(input()) #판 n개 입력받기

def hanoiFunction(x,first,second,third):
    if(x == 1):
        print(first, third)
    else:
        hanoiFunction(x-1,first,third,second)
        print(first,third)
        hanoiFunction(x-1,second,first,third)

sum = 1;
for i in range(num-1):
    sum = sum*2 +1

print(sum);
hanoiFunction(num,1,2,3);
