N=int(input())
scores=map(int,input().split())

scores_list=list(scores)
max_score=max(scores_list)

newscore_list=[]
for x in scores_list:
    newscore=x/max_score*100
    newscore_list.append(newscore)
print(sum(newscore_list)/N)