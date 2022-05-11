n,m = map(int, input().split())
arr =[]

def dfs():
    if(len(arr)==m):
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if i not in arr: ##visited 배열이 굳이 필요가 없다. 그냥 not in 해버리면 없으면 넘어가고 할 수 있다. 
            arr.append(i)
            dfs()
            arr.pop()

dfs()