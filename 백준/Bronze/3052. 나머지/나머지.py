nlist=[]

for x in range(10):
    N=int(input())
    nlist.append(N%42)

nset=set(nlist)
print(len(nset))