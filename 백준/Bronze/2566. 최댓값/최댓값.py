arr = [list(map(int,input().split())) for _ in range(9)]

maxy=0
a=b=0
for i in range(9):
    for j in range(9):
        if maxy <= arr[i][j]:
            maxy = arr[i][j]
            a=i+1
            b=j+1

print(maxy)
print(a,b)