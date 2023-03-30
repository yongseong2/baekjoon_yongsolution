N, S = map(int,input().split())
lst = list(map(int,input().split()))

visited = [0]*N
cnt = 0

def dfs(n, com):
    global cnt

    if n == N:
        if sum(com) == S and len(com) >= 1:
            cnt += 1
        return

    dfs(n+1, com+[lst[n]])
    dfs(n+1, com)

dfs(0, [])
print(cnt)