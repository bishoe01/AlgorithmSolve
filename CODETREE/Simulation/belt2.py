from codecs import BufferedIncrementalDecoder


n, t  = map(int,input().split())
belt = [
    list(map(int,input().split()))
    for _ in range(2)
] 

belt_new = belt[0] + belt[1]
for _ in range(t):
    tmp=[0]
    tmp[0] = belt_new.pop()
    belt_new = tmp + belt_new


for i in range(len(belt_new)):
    if(i == len(belt_new)//2):
        print()
    print(belt_new[i], end= " ")