import random
import time
#ROCK PAPER SCISSORS CODE
def RPSmain():
    print('_____USER VS. BOT___')
    print('_____BEST OF FIVE___')
    print('''
    1=rock
    2=paper
    3=scissors ''')
    ties=0
    u_wins=0
    b_wins=0
    for i in range(5):
        bot=random.randrange(1,4)
        user=int(input('enter your play: '))
        print ('bot-->',bot)
        print ('user-->',user)
        if user+1==bot or user-2==bot:
            print('___BOT WINS!___')
            #print('you played',user)
            #print('bot played',bot)
            b_wins+=1
        elif user==bot:
            print ('__Its a tie!__')
            ties+=1	
        else:
            print('___USER WINS!___')
            u_wins+=1
        print('user_wins:',u_wins)
        print('bot_wins:',b_wins)
        print (ties,'ties')

    if u_wins>b_wins:
        print('___YOU WIN!___')
    elif b_wins>u_wins:
        print('___YOU LOSE!___')

    elif b_wins==u_wins:
        def tie():
            ties=0
            print('~TIE BREAKER!~')
            
            bot=random.randrange(1,4)
            user=int(input('enter your play: '))
            if user!=1 or user!=2 or user!=3:
                print('invalid input.')
            else:
                if user+1==bot or user-2==bot:
                    print('___YOU LOSE!___')
                    print('you played',user)
                    print('bot played',bot)
                
                elif user==bot:
                    ties=1	
                else:
                    print('___YOU WINS!___')
                    print('you played',user)
                    print('bot played',bot)
            if ties>0:
                return tie()
        return tie()

