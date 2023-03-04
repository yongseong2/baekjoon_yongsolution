N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for k in range(N):
    x, y, w, h = map(int,input().split())

    for i in range(x,x+w): # 색종이를 k 순대로 덮기
        for j in range(y,y+h):
            arr[i][j] = k+1


for k in range(N): # 색종이에서 k+1 찾아내기
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == k+1:
                cnt += 1

    print(cnt)