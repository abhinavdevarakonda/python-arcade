import time
import random
guesses=[]
win=0
loss=0
l=[]
hangman=(
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
def hangmanmain():
    guesses=[]
    win=0
    loss=0
    l=[]
    print('___2 PLAYERS___')
    print('~PLAYER-1~')
    time.sleep(0.5)
    p1=input('enter your name: \n')
    time.sleep(1)
    print('~PLAYER-2~')
    time.sleep(0.5)
    p2=input('enter your name \n')
    coin=random.randint(1,2)
    time.sleep(2)
    print('*odds to see who starts*')
    time.sleep(2)
    print(p1,',choose 1 or 2!:')
    c=int(input())
    if c==coin:
        #p1 starts
        time.sleep(1)
        print(p1,', enter the word.',p2,', look away!:')
    elif c!=coin:
        #p2 starts
        time.sleep(1)
        print(p2,', enter the word.',p1,', look away!:')

    word=input()
    print('\n'*50)
    for i in word:
        l.append(i)
    #
    a=[]
    for i in range(len(word)):
        if l[i]!=' ':
            a.append('|__|')
        else:
            a.append('--')
    #
    while loss<10:
        if c==coin:
            time.sleep(1)
            print(p2,'enter a letter:\n')
        else:
            time.sleep(1)
            print(p1,'enter a letter:\n')
        guess=input()
        if guess in guesses:
            print('you have already entered that letter.')
        else:
            guesses.append(guess)
        print('\n'*50)
        for i in range(len(l)):
            if guess==l[i]:
                a[i]=guess
                win+=1
        if guess not in l:
            time.sleep(0.5)
            print('~INCORRECT!~')
            loss+=1
        elif win==len(word.replace(' ','')):
            if c==coin:
                time.sleep(2)
                print('_____',p2,'_WINS!_____')
                break
            elif c!=coin:
                time.sleep(2)
                print('_____',p1,'_WINS!_____')
                break
        print(a)
        time.sleep(0.5)
        print(hangman[loss],'                         ',guesses)              

