N=int(input())

N_list=list(str(N))
int_N_list=map(int,N_list)

sum_N=sum(int_N_list)
sum_N_lst=map(int,list(str(sum_N)))

# newN=int_N_list[0]
print(sum_N)
