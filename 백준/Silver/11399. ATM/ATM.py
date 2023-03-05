N = int(input())
lst = list(map(int,input().split()))

lst.sort()

cnt = 0
ans = []
for i in range(N):
    cnt += lst[i]
    ans.append(cnt)

print(sum(ans))