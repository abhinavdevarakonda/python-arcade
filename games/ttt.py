import random
import time
#tic tac toe code
def tttmain():
    running = True
    def board_display():
        global board
        board=[
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]	
        for i in range(len(board)):
            print('   ',chr(65+i),end='')
        print()
        for i in range(len(board[0])):
            print(i+1,board[i],end='   ')
            print()
            print()
    player1='X'
    player2='O'

    print('''___SELECT_GAME_MODE___
    1.SINGLE_PLAYER
    2.TWO_PLAYER
    ENTER YOUR CHOICE: \n ''')
    c=int(input())
    print('\n'*50)

    def play(x):
        running = True
        if u==coin:
            P=0
        else:
            P=1
        global play 
        global user_play
        wins=0
        print('___START!___')
        print(board_display())
        while running:
            if P%2==0:
                print(a1,'select a position:\n')
            else:
                print(a2,'select a position:\n')
            user_play=input()
            user_play=user_play.upper()
            print('\n'*50)
            if (ord(user_play[0]))>67 or (ord(user_play[0]))<65 or int(user_play[1])>3 or int(user_play[1])<1:
                print('~Invalid_Position~')
            else:
            #actual_play
                if P%2==0:
                    board[int(user_play[1])-1][ord(user_play[0])-65]=player1
                    P+=1
                else:
                    board[int(user_play[1])-1][ord(user_play[0])-65]=player2
                    P+=1
            #VICTORY-CHECK:
            def win(box):
                #horizontal##########################################################
                if board[0][0] == box and board[0][1] == box and board[0][2] == box:
                    return True
                if board[1][0] == box and board[1][1] == box and board[1][2] == box:
                    return True
                if board[2][0] == box and board[2][1] == box and board[2][2] == box:
                    return True
                #####################################################################
                #vertical##########################################################
                if board[0][0] == box and board[1][0] == box and board[2][0] == box:
                    return True
                if board[0][1] == box and board[1][1] == box and board[2][1] == box:
                    return True
                if board[0][2] == box and board[1][2] == box and board[2][2] == box:
                    return True
                ######################################################################
                #diagonal#############################################################
                if board[0][0] == box and board[1][1] == box and board[2][2] == box:
                    return True
                if board[2][0] == box and board[1][1] == box and board[0][2] == box:
                    return True
                ######################################################################

            #display-in-loop
            for i in range(len(board)):
                print('   ',chr(65+i),end='')
            print()
            for i in range(len(board[0])):
                print(i+1,board[i],end='   ')
                print()
                print()
            
            if win(player1):
                print('CONGRATULATIONS PLAYER-1')
                running = False
            if win(player2):
                print('CONGRATULATIONS PLAYER-2')
                running = False
    if c==2:
        print('~PLAYER_1~')
        a1=input('enter your name:\n')
        print('~PLAYER_2~')
        a2=input('enter your name:\n')
        coin=random.randint(1,2)
        time.sleep(0.5)
        print('*odds to see who starts*')
        time.sleep(1)
        print(a1,'choose 1 or 2!:\n')
        u=int(input())
        if u==coin:
            return play(player1)
        elif u!=coin:
            return play(player2)			            

