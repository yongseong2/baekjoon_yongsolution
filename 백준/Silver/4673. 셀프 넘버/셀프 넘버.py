def self_number():
    all_list=list(range(1,9999))
    dn_list=[]
    
    i=0
    while True:
        i+=1
        sumn=0
        for n in list(str(i)):
            sumn+=int(n)
        dn_list.append(sumn+i)
        if i>=10000:
            break
    
    result=[x for x in all_list if x not in dn_list]
    
    for re in result:
        print(re)

self_number()