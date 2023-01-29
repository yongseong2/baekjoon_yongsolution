word=input()

coroatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in coroatia:
    word=word.replace(i,'*') #replace 함수 크로아티아 리스트에 있는 요소들을 워드에서 *로 대체하라.
    
print(len(word))