

n , m = map(int,input().split())
answer = []

def print_answer():
    for element in answer:
        print(element,end = ' ')
    print()
def choose(curr_num, cnt):
    if curr_num == n +1: 
        if( cnt == m ):
            print_answer()
        return

    answer.append(curr_num)
    choose(curr_num+1, cnt + 1)
    answer.pop()    

    choose(curr_num +1 , cnt)

choose(1,0)