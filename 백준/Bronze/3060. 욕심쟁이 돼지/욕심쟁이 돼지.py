T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = sum(list(map(int, input().split())))

    day = 1
    while N >= lst:
        day += 1
        lst *= 4
    print(day)
