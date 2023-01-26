N=int(input())
number=map(int,input().split())
v=int(input())

v_list=[]
for n in list(number):
    if n==v:
        v_list.append(n)
    

print(len(v_list))