N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []

def dfs(n,s, com):
    global ans
    if n == M:
        ans.append(com)
        return
    for i in range(s, N):
        dfs(n+1, i+1, com + [lst[i]])

dfs(0,0,[])
for x in ans:
    print(*x)