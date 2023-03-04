T = 4
arr = [[0]*101 for _ in range(101)]

for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            ans += 1

print(ans)