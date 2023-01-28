def self_number(): #셀프넘버 함수
    all_list=list(range(1,10001)) #10000까지의 리스트
    dn_list=[]
    
    i=0
    while True:
        i+=1
        sumn=0
        for n in list(str(i)):
            sumn+=int(n) #각자리수의 합
        dn_list.append(sumn+i) #dn_list의 각자리수의 합+i를 더함
        if i>=10000: #i가 10000이 되었을 때 반복문 빠져나가기
            break
    
    result=[x for x in all_list if x not in dn_list] #두개에 리스트에서 중복요소를 제거한 새로운 리스트 생성
    
    for re in result:
        print(re)

self_number()

