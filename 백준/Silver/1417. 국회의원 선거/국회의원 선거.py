N = int(input())
lst = []
for _ in range(N):
    p = int(input())
    lst.append(p)

ans = 0
while True:
    if len(lst) == 1:
        ans = 0
        break
    elif lst[0] > max(lst[1:]):
        break
    else:
        for i in range(1,N):
            if lst[i] == max(lst):
                lst[i] -= 1
                lst[0] += 1
                ans += 1

print(ans)