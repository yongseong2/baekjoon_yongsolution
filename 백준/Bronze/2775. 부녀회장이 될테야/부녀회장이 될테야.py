T=int(input())
for tc in range(T):
    k=int(input())
    n=int(input())
    
#k층의 n호에 살려면 자신의 아래(k-1)층의 1호부터 n까지 사람들의 수의 합
    #0층 1호에는 1명
    #0층 2호에는 2명
    #0층 3호에는 3명 ...
    
    #1층 1호에는 1명
    #1층 2호에는 3명
    #1층 3호에는 6명
    #1층 4호에는 10명
    #1층 5호에는 15명
    #1층 6호에는 21명
    
    #2층 1호에는 1명
    #2층 2호에는 4명
    #2층 3호에는 10명
    #2층 4호에는 20명
    #2층 5호에는 35명
    
    #3층 1호에는 1명
    #3층 2호에는 5명
    #3층 3호에는 15명
    #3층 4호에는 35명
    
    zero_list=[x for x in range(1,n+1)]

    for i in range(k):
        for j in range(1,n):
            zero_list[j]+=zero_list[j-1]
        
    print(zero_list[-1])