N = int(input())
lst = input()

cnt = len(lst)

for x in lst:
    if x == 'L':
        cnt -= 0.5

ans = int(cnt + 1)
if ans > len(lst):
    ans = len(lst)

print(ans)