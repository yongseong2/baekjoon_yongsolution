N, M = map(int,input().split())
lst = [x for x in range(1, N+1)]
ans = []

def dfs(n, com):
    global ans
    if n == M:
        ans.append(com)
        return
    for i in range(N):
        dfs(n+1, com + [lst[i]])


dfs(0, [])

for x in ans:
    print(*x)