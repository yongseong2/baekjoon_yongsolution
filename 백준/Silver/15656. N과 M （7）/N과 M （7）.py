N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []

def dfs(n, com):
    if n == M:
        ans.append(com)
        return
    for i in range(N):
        dfs(n+1, com+[lst[i]])

dfs(0,[])
for x in ans:
    print(*x)