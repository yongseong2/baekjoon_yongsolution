A,B=map(str,input().split())

lst_A=list(A)
lst_B=list(B)

lst_A.reverse()
lst_B.reverse()

new_A="".join(lst_A)
new_B="".join(lst_B)


if int(new_A)>int(new_B):
    print(int(new_A))
elif int(new_A)<int(new_B):
    print(int(new_B))