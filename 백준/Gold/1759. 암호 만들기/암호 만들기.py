N, M = map(int,input().split())
lst = list(input().split())
lst.sort()

ans = []
visited = [0]*M

def dfs(n, s, com):
    global ans

    if n == N:
        ans.append(com)
        return

    for i in range(s, M):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1,i, sorted(com + [lst[i]]))
            visited[i] = 0

dfs(0, 0,[])

for x in ans:
    a = x.count('a')
    e = x.count('e')
    i = x.count('i')
    o = x.count('o')
    u = x.count('u')
    els = len(x) - (a+e+i+o+u)
    if (a+e+i+o+u) >= 1 and els>=2:
        res = ''.join(x)
        print(res)
