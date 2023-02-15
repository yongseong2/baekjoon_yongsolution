arr = [[0]*100 for _ in range(100)]

N=int(input())
for _ in range(N):
    r, c = map(int,input().split())

    for i in range(r,r+10):
        for j in range(c,c+10):
            arr[i][j] = 1

cnt=0
for i in arr:
    for j in i:
        if j==1:
            cnt+=1

print(cnt)