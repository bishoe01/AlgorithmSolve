N , M = map(int,input().split())
arr = []
visited = [False] * (N+1)


def dfs():
    if(len(arr) == M ):
        print(' '.join(map(str,arr)))
        return
    for i in range(1,N+1):
        if(visited[i]):
            continue
        visited[i] = True
        arr.append(i)
        dfs()
        arr.pop()
        visited[i] = False

dfs()