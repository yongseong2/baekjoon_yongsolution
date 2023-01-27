C=int(input())

for i in range(C):
    N,*scores=map(int,input().split())
    student_average=sum(scores)/N
    over_average=0
    over_average_list=[]
     
    for score in scores:
        
        if score>student_average:
            over_average_list.append(score)
    result=format(round((len(over_average_list)/len(scores))*100, 3),".3f")
      
    print(f'{result}%')