N, M = map(int,input().split())

lst = [x for x in range(1, N+1)]

ans = []
def dfs(n, com):
    if len(com) > M:
        return
    if n == N:
        if len(com) == M:
            ans.append(com)
        return
    dfs(n+1, com+[lst[n]])
    dfs(n+1, com)

dfs(0,[])

for x in ans:
    print(*x)