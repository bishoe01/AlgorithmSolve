n = int(input())
for i in range(n):
    num , target = map(int,input().split())
    deck = list(map(int,input().split()))
    answer = [0 for i in range(num)] #0으로 초기화
    answer[target] = 1 #우선순위를 측정할 값
    priority = 0  #최종 출력할 우선순위 변수
    while True:
        if(deck[0] == max(deck)):
            priority += 1
            if(answer[0] == 1):
                print(priority)
                break
            else:
                deck.pop(0)
                answer.pop(0)
        else:
            deck.append(deck.pop(0))
            answer.append(answer.pop(0))
        
