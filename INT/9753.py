from collections import Counter ##key의 개수를 알기위한 Counter라이브러리 임포트
N = int(input())


for i in range(N):
    testcase = int(input())
    arr =[]
    for _ in range(testcase):
        cloth,category = map(str, input().split())
        arr.append(category) ##옷이 무엇인지는 계산할 떄 필요하지 않으므로 category만 리스트에 추가를해준다. 
    
    sum = 1 
    result = Counter(arr)  #Counter로 옷 종류(Key)가 몇 종류 있는지 딕셔너리로 만들어준다.
    for key in result :  #이때 key의 값은 
        sum *=result[key] + 1
    print(sum-1)
    
    