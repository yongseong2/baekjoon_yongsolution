N, M = map(int,input().split())
visited = [0]*(N+2)
ans = []

def dfs(n, s, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for i in range(s, N + 1):
        dfs(n+1, i, lst + [i])

dfs(0, 1, [])
for x in ans:
    print(*x)