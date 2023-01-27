N=int(input())

for i in range(N):
    case=str(input())
    score=0
    score_count=0
    for j in list(case):
        if j=='O':
            score_count+=1 #스코어 카운트
            score+=score_count #누적합
        elif j=='X':
            score_count=0 #X를 만났을 때 score_count를 초기화 시켜서 다시 1부터 시작함
    print(score)