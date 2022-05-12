n, m = map(int, input().split())
arr= []

def dfs():
    if( len(arr) == m):
        print(" ".join(map(str, arr)))
        return
    for i in range(1,n+1):
        # if( i not in arr ): # 이 부분을 지워주면은 수열간 중복이 허용된다.
        arr.append(i)
        dfs()
        arr.pop()

dfs()