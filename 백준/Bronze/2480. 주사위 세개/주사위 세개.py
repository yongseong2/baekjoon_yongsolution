dice1, dice2, dice3=map(int,input().split())

if dice1==dice2==dice3:
    print(10000+1000*dice1)
elif dice1==dice2:
    print(1000+100*dice1)
elif dice2==dice3:
    print(1000+100*dice2)
elif dice1==dice3:
    print(1000+100*dice1)
elif dice1!=dice2!=dice3:
    print(max(dice1,dice2,dice3)*100)