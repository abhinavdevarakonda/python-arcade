#GUESS THE NUMBER CODE
import random
#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!
def GTNmain():
    r=random.randrange(1,10)
    tries=0
    for i in range(3):
        a=int(input('enter a number from 1 to 10: '))
        if a<1 or a>10:
            print('invalid input.')
        else:
            if a!=r:
                print('~TRY AGAIN~')
                tries+=1
                if tries==3:
                    print('~YOU LOST!~')
                    break
            elif a==r:
                print('~YOU WIN!~')
                break

GTNmain()
