from itertools import permutations
N, M = map(int,input().split())
lst = [x for x in range(1, N+1)]

for x in permutations(lst, M):
    print(*x)