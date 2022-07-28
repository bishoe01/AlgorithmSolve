

k , n = map(int,input().split())
answer = []

def print_answer():
    for element in answer:
        print(element,end = ' ')
    print()
def choose(cnt):
    if cnt == n: 
        print_answer()
        return
    
    for i in range(1, k+1):
        if(cnt >=2 and i == answer[-1] and i== answer[-2]):
            continue
        answer.append(i)
        choose(cnt +1) 
        answer.pop()


choose(0)