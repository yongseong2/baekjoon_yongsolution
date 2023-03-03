N = 10
lst = []
for i in range(N):
    num = int(input())
    lst.append(num%42)

lst = set(lst)
print(len(lst))
