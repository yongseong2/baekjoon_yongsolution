N = int(input())

lst = [N,0]
ans1 = 0
ans2 = 0
for i in range(0, 30001):
    lst[1] = i
    while lst[-1] >= 0:
        lst.append(lst[-2]-lst[-1])
        if ans1 < len(lst):
            ans1 = len(lst)
            ans2 = lst
    lst = [N, 0]

print(ans1-1)
print(*ans2[:-1])