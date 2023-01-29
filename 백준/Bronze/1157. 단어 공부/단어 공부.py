from collections import Counter

word=str(input())
upper_word=word.upper()

count_word=Counter(upper_word)

sort_count_word=sorted(count_word.items(),key=lambda x:x[1],reverse=True)


if len(sort_count_word)==1:
    print(upper_word)
elif sort_count_word[0][1]==sort_count_word[1][1]:
    print('?')
else:
    print(sort_count_word[0][0])
