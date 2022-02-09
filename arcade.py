#WELCOME TO THE ARCADE!
import random
import time
import threading
import json
from nltk.corpus import words as nltk_words
#importing the games
import RPS
import hangman
import ttt
#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!

choice=int(input(('''
__________MENU__________
1.guess the number
2.rock, paper, scissors game
3.hangman
4.tic-tac-toe
5.connect-4
6.minesweeper
7.sudoku
Enter your choice: \n ''')))                                   
#####################################################                        #COMPLETED
def Minesweeper():
	mines=list()
	reveal=[[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9]]
	numbers=list()
	GG=0
	r=0
	c=0
	count=0
	print("WELCOME TO MINESWEEPER!!")
	print()
	time.sleep(1.5)

	def Numbers():
	    global numbers
	    numbers=list()
	    for i in range (1,9):
	        a=list()
	        for j in range(1,9):
	            if mines[i][j]==1:
	                a.append(9)
	            else:
	                count=0
	                if mines[i+1][j+1]==1:
	                    count+=1
	                if mines[i+1][j]==1:
	                    count+=1
	                if mines[i+1][j-1]==1:
	                    count+=1
	                if mines[i][j+1]==1:
	                    count+=1
	                if mines[i][j-1]==1:
	                    count+=1
	                if mines[i-1][j]==1:
	                    count+=1
	                if mines[i-1][j+1]==1:
	                    count+=1
	                if mines[i-1][j-1]==1:
	                    count+=1
	                a.append(count)
	        numbers.append(a)

	def Home_Screen():
	    while True:
	        print("HOME SCREEN :")
	        print("1.Instructions")
	        print("2.Play the game")
	        ch=input("Select your option :\n")
	        try:
	            ch=int(ch)
	        except:
	            pass
	        if ch==1:
	            print('''
	                             INSTRUCTIONS
	1.A grid of squares is presented to the user where all of them are closed.
	2.a set number of mines are placed at random in the grid.
	3.once a square is opened, numbers will appear. These numbers will tell you how many mines are placed around the number.\n for example: if 1 is shown, that means there is 1 mine adjacent to the square.
	4.the objective is to complete the grid without selecting any mines.
	5.NOTE:empty squares may also appear. This means that there are no mines around that square.
	6.NOW GO HAVE FUN!''')
	            print()
	            print()
	            time.sleep(10)
	        elif ch==2:
	            break
	        else:
	            print("Enter valid option.")

	def Board_Display():
	    global reveal
	    global r
	    global GG
	    for k in range(8):    
	        for i in range(8):
	            for j in range(8):
	                if reveal[i][j]==0:
	                    if (i-1)>=0 and (j-1)>=0:
	                        reveal[i-1][j-1]=numbers[i-1][j-1]
	                    if (i-1)>=0 and (j)>=0:
	                        reveal[i-1][j]=numbers[i-1][j]
	                    if (i-1)>=0 and (j+1)<=7:
	                        reveal[i-1][j+1]=numbers[i-1][j+1]
	                    if (i)>=0 and (j-1)>=0:
	                        reveal[i][j-1]=numbers[i][j-1]
	                    if (i)>=0 and (j+1)<=7:
	                        reveal[i][j+1]=numbers[i][j+1]
	                    if (i+1)<=7 and (j-1)>=0:
	                        reveal[i+1][j-1]=numbers[i+1][j-1]
	                    if (i+1)<=7 and (j)>=0:
	                        reveal[i+1][j]=numbers[i+1][j]
	                    if (i+1)<=7 and (j+1)<=7:
	                        reveal[i+1][j+1]=numbers[i+1][j+1]                
	    print("       ",end="")
	    for i in range(8):
	        print(i+1, end ="    ")
	    print()
	    print()
	    print()
	    for i in range(1,9):
	        print(chr(64+i) , end="      ")
	        for j in range(1,9):
	            if reveal[i-1][j-1]==9:
	                print("\u25A0" , end="    ")
	            elif reveal[i-1][j-1]==0:
	                print(chr(927) , end="    ")
	            else :
	                print(reveal[i-1][j-1],end="    ")
	        print()
	        print()
	        
	def Mines_Randomizer():
	    global mines
	    mines=list()
	    mines.append([9,9,9,9,9,9,9,9,9,9])
	    for i in range(1,9):
	        a=list()
	        a.append(9)
	        for j in range(1,9):
	            if random.randint(0,5)==1:
	                a.append(1)
	            else:
	                a.append(0)
	        a.append(9)
	        mines.append(a)
	    totalm=0
	    for i in range(1,9):
	        for j in range(1,9):
	            if mines[i][j]==1:
	                totalm+=1
	        while totalm>=10:
	            break
	    mines.append([9,9,9,9,9,9,9,9,9,9])
	        
	def Choice():
	    global r
	    global c
	    global d
	    global i1
	    global j1
	    print()
	    if (d==1):
	        r=i1+1
	        c=j1+1
	    else:
	        while(True):
	            cell=input("Select Square:\n")
	            print('\n'*50)
	            if(len(cell)==2 and cell[0].isalpha() and cell[1].isdigit()):
	                r=ord(cell[0].upper())-64
	                c=(cell[1])
	                try:
	                    c=int(c)
	                    if 0<=r<=8 and 0<=c<=8:
	                        break
	                    else:
	                        print("Enter valid coordinates.")
	                        print("For example: A1,a2,h8 etc.\n")
	                except:
	                    print("Enter valid coordinates.")
	                    print("For example: A1,a2,h8 etc.\n")
	                    break
	            else:
	                print("Enter valid coordinates.")
	                print("For example: A1,a2,h8 etc.\n")
	def Result():
	    global mines
	    global count
	    global reveal
	    global r
	    global c
	    global GG
	    if mines[r][c]==1:
	        GG=1
	        print("YOU LOOOOSE!!!!!")
	    else :
	        reveal[r-1][c-1]=numbers[r-1][c-1]

	def Lose():
	    global reveal
	    global mines    
	    print("       ",end="")
	    for i in range(8):
	        print(i+1, end ="    ")
	    print()
	    print()    
	    for i in range(1,9):
	        print(chr(64+i) , end="      ")
	        for j in range(1,9):
	            if mines[i][j]==1:
	                print(chr(1147),end="    ")
	                continue
	            if reveal[i-1][j-1]==9:
	                print("\u25A0" , end="    ")
	            elif reveal[i-1][j-1]==0:
	                print(chr(927) , end="    ")
	            else :
	                print(reveal[i-1][j-1],end="    ")
	        print()
	        print()
	    print()
	    print()
	    time.sleep(2)
	    print('''
	                        ,--.!,
	                     __/   -*-
	                   ,d08b.  '|`
	                   0088MM     
	                   `9MMP'     ''')
	    time.sleep(2)
	    print('''
	                  _ ._  _ , _ ._
	                (_ ' ( `  )_  .__)
	              ( (  (    )   `)  ) _)
	             (__ (_   (_ . _) _) ,__)
	                 `~~`\ ' . /`~~`
	                      |   |
	                      /   \\
	        _____________/_ __ \\_____________ ''')

	def win():
	    print("YOU WINNN!!!")
	    for i in range(1,9):
	        print(chr(64+i) , end="      ")
	        for j in range(1,9):
	            if mines[i][j]==1:
	                print(chr(1147),end="    ")
	                continue
	            if reveal[i-1][j-1]==9:
	                print("\u25A0" , end="    ")
	            elif reveal[i-1][j-1]==0:
	                print(chr(927) , end="    ")
	            else :
	                print(reveal[i-1][j-1],end="    ")
	    print('''
	                         $$$$$$$$$$$$$$$$$$$$
	                       $$$$$$$$$$$$$$$$$$$$$$$$$$$
	                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$   $$$$$
	    $$$$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$$$$$$$
	 $$ $$$$$$      $$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$       $$$$$$$$
	 $$$$$$$$$     $$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$    $$$$$$$$
	   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
	   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  $$$$$$
	    $$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$
	     $$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$
	    $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$
	    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$
	   $$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$
	   $$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$$$$$
	  $$$$       $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$$
	             $$$$$     $$$$$$$$$$$$$$$$$$$$$$$$$         $$$
	               $$$$          $$$$$$$$$$$$$$$           $$$$
	                $$$$$                                $$$$$
	                 $$$$$$      $$$$$$$$$$$$$$        $$$$$
	                   $$$$$$$$     $$$$$$$$$$$$$   $$$$$$$
	                      $$$$$$$$$$$  $$$$$$$$$$$$$$$$$
	                         $$$$$$$$$$$$$$$$$$$$$$
	                                 $$$$$$$$$$$$$$$
	                                     $$$$$$$$$$$$
	                                      $$$$$$$$$$$
	                                       $$$$$$$$
	''')


	#main        
	Home_Screen()
	print()
	d=1
	time.sleep(1)
	print("HERE IS YOUR BOARD")
	time.sleep(1)
	print()
	Mines_Randomizer()
	Numbers()
	Board_Display()
	while(True):
	    str1=input("Select Square \n")
	    if (len(str1)==2 and str1[0].isalpha() and str1[1].isdigit()):
	        i1=(ord(str1[0].upper())-65)
	        j1=(str1[1])
	        try:
	            j1=int(j1)-1
	            if 0<=i1<=7 and 0<=j1<=7:
	                break
	            else:
	                print("Enter valid coordinates.")
	                print("For example: A1,a2,h8 etc.\n")
	        except:
	            print("Enter valid coordinates.")
	            print("For example: A1,a2,h8 etc.\n")
	            break       
	    else:
	        print("Enter valid coordinates.")
	        print("For example: A1,a2,h8 etc.\n")
	while(True):
	    if numbers[i1][j1]!=0:
	        Mines_Randomizer()
	        Numbers()
	    else:
	        break
	Choice()
	Result()
	print('\n'*50)
	Board_Display()
	d=2
	while GG!=1:
	    Choice()
	    Result()
	    Board_Display()
	    count=0
	    i=0
	    j=0
	    ch=0 
	    if (reveal==numbers):
	        GG=0
	        break
	if GG==0:
	    time.sleep(2)
	    print()
	    print()
	    win()
	    
	else:
	    print()
	    print()
	    Lose()
#####################################################                        #INCOMPLETE
def scrabble():
	board=[['Ѡ','■','■','■','■','■','■','Ѡ','■','■','■','■','■','■','Ѡ'],
		   ['■','҈','■','■','■','■','■','■','■','■','■','■','■','҈','■'],
		   ['■','■','҈','■','■','■','■','■','■','■','■','■','҈','■','■'],
		   ['■','■','■','҈','■','■','■','■','■','■','■','҈','■','■','■'],
		   ['■','■','■','■','҈','■','■','■','■','■','҈','■','■','■','■'],
		   ['■','■','■','■','■','Ỽ','■','■','■','Ỽ','■','■','■','■','■'],
		   ['■','■','■','■','■','■','®','■','®','■','■','■','■','■','■'],
		   ['Ѡ','■','■','■','■','■','■','֍','■','■','■','■','■','■','Ѡ'],
		   ['■','■','■','■','■','■','®','■','®','■','■','■','■','■','■'],
		   ['■','■','■','■','■','Ỽ','■','■','■','Ỽ','■','■','■','■','■'],
		   ['■','■','■','■','҈','■','■','■','■','■','҈','■','■','■','■'],
		   ['■','■','■','҈','■','■','■','■','■','■','■','҈','■','■','■'],
		   ['■','■','҈','■','■','■','■','■','■','■','■','■','҈','■','■'],
		   ['■','҈','■','■','■','■','■','■','■','■','■','■','■','҈','■'],
		   ['Ѡ','■','■','■','■','■','■','Ѡ','■','■','■','■','■','■','Ѡ']]
	print('~WELCOME TO SCRABBLE!~')
	time.sleep(0.5)
	print('~PLAYER-1~')
	time.sleep(0.2)
	player1 = input('enter your name:\n')
	time.sleep(0.5)
	print('~PLAYER-2~')
	time.sleep(0.2)
	player2 = input('enter your name:\n')
	time.sleep(1)


	def play_board(display):
		
		print('    A B C D E F G H I J K L M N O')
		print('=================================')
		for i in range(len(display)):
			if i+1 < 10:
				print((i+1),end=' ||')
			elif i+1 >= 10:
				print((i+1),end='||')
			time.sleep(0.05)
			for j in range(len(display)):
				print(display[i][j],end=' ')
			print()
	##############
	def repeat(word,tiles):
		b=0
		c=0
		d_input = {}
		k_input = []
		v_input = []
		d_tile = {}
		k_tile = []
		v_tile = []
		l = []
		for i in word:
			k_input.append(i)
		for i in range(len(word)):
			v_input.append(0)
		for i in range(len(word)):
			for j in range(len(word)):
				if word[i] == word[j]:
					if word[i] not in l:
						v_input[i] += 1
						l.append(word[i])
		for i in range(len(word)):
			d_input[k_input[i]] = v_input[i]

		for i in range(9):
			k_tile.append(tiles[i])
			v_tile.append(0)
		for i in range(9):
			for j in range(9):
				if tiles[i] == tiles[j]:
					v_tile[i] += 1
					tiles.pop(i)
		for i in range(9):
			d_tile[k_tile] = v_tile[i]
		for i in word:
			if i in tiles:
				b+=1
		if b == len(word):
			for i in d_input.keys():
				if d_tile[i] == d_input[i]:
					c+=1
		if c == len(word):
			return True
		else:
			return False
	#####################
	def legit(word,tiles):
		a = 0
		content = dict.fromkeys(nltk_words.words(),None)
		for i in range(len(word)):
			if word[i] in tiles:
				a+=1
			else:
				return False

		if word in content and a == len(word):
			if repeat(word,tiles):			
				return True
			else:
				return False
		else:
			return False
	#####################
	def score_cal(word):
		global score
		total = 0
		score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}
		for i in word:
			total = total + score[i.lower()]
		return total
	#################	
	def play():
		alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		player1_tiles = []
		player2_tiles = []
		player1_score = 0
		player2_score = 0
		count = 1
		print(player1,'starts!')
		time.sleep(0.5)
		print(player2,'look away!')
		time.sleep(3)
		print(player1,'these are you tiles:\n')
		for i in range(9):
			player1_tiles.append(random.choice(alphabets))
			print(player1_tiles[i])
			time.sleep(0.1)
		time.sleep(10)
		print('\n'*50)
		print(player1,'look away!')
		time.sleep(3)
		print(player2,'these are your tiles:\n')
		for i in range(9):
			player2_tiles.append(random.choice(alphabets))
			print(player2_tiles[i])
			time.sleep(0.1)
		time.sleep(10)
		print('\n'*50)
		time.sleep(0.75)

		print('here is the board:')
		time.sleep(0.5)
		play_board(board)
		while True:
			count+=1
			if count==2:
				print(player1,',enter the position of the beginning of your word. (for example: A1,B2,J10 etc.):\n')
				pos = input()
			elif count!=2 and count%2!=0:
				print(player2,',enter the position of the beginning of your word:\n')
				pos = input()
			elif count!=2 and count%2==0:
				print(player1,',enter the position of the beginning of your word:\n')
				pos = input()
			x = pos[0]
			y = ''
			if len(pos) > 2:
				y = pos[1]+pos[2]
			elif len(pos) == 2:
				y = pos[1]

			if x.isalpha():
				x = x.upper()
				if ord(x.upper()) > ord('O'):
					pass
			else:
				print('invalid position.')
			if y.isdigit():
				if int(y) <= 15:
					y = int(y)
					pass 
				else:
					print('invalid position.') 
			else:
				print('invalid position')
			
			print('''enter the direction of you word 
	up = 1
	
	down = 2 
	
	left = 3 
	
	right = 4
	''')

			direc = int(input())
			#####
			print('enter your word:\n')
			user_input = input()
			while True:
				if count%2==0:	
					if legit(user_input,player1_tiles):
						for i in user_input:
							player1_tiles.pop(i)
							player1_tiles.append(random.choice(alphabets))
						break
					elif legit(user_input,player1_tiles) == False:
						user_input = input('please enter a valid word.')
				else:
					if legit(user_input,player2):
						for i in user_input:
							player2_tiles.pop(i)
							player2_tiles.append(random.choice(alphabets))
						break
					elif legit(user_input) == False:
						user_input = input('please enter a valid word.')
			  ##################       UP    #####################
			if direc == 1 and len(user_input) <= y:
				for i in range(len(user_input)):
					board[(y-1)-i][ord(x)-65] = user_input[i].upper()
			##################       DOWN    #####################
			elif direc == 2 and len(user_input) <= 16-y:
				for i in range(len(user_input)):
					board[(y-1)+i][ord(x)-65] = user_input[i].upper()
			##################       LEFT    #####################
			elif direc == 3 and len(user_input) <= (ord(x)-65)+1:
				for i in range(len(user_input)):
					board[y-1][(ord(x)-65)-i] = user_input[i].upper()
			##################       RIGHT    #####################
			elif direc == 4 and len(user_input) <= 16-(ord(x)-65)+1:
				for i in range(len(user_input)):
					board[y-1][(ord(x)-65)+i] = user_input[i].upper()
			###########################################################
			#elif direc == 5 and len(user_input) <= (65-ord(x)) and len(user_input) <= y:
			#	for i in range(len(user_input)):                                                      #APPARANTLY DIAGONAL WORDS ARE NOT ALLOWED
			#		board[(y-1)-i][(ord(x)-65)-i] = user_input[i].upper()
			########################################################                                  #APPARANTLY DIAGONAL WORDS ARE NOT ALLOWED
			#elif direc == 6 and len(user_input) <= (16-(65-ord(x))) and len(user_input) <= y:
			#	for i in range(len(user_input)):
			#		board[(y-1)-i][(ord(x)-65)+i] = user_input[i].upper()                             #APPARANTLY DIAGONAL WORDS ARE NOT ALLOWED
			#########################################################
			#elif direc == 7 and len(user_input) <= ((ord(x)-65)+1) and len(user_input) <= (16-y):   #APPARANTLY DIAGONAL WORDS ARE NOT ALLOWED
			#	for i in range(len(user_input)):
			#		board[(y-1)+i][(ord(x)-65)-i] = user_input[i].upper()
			#########################################################
			#elif direc == 8 and len(user_input) <= (16-(ord(x)-65)-1) and len(user_input) <= (16-y): #APPARANTLY DIAGONAL WORDS ARE NOT ALLOWED
			#	for i in range(len(user_input)):
			#		board[(y-1)+i][(ord(x)-65)+i] = user_input[i].upper()
			########################################################
			if count % 2==0:
				if legit(user_input,player1_tiles):	
					player1_score+=score_cal(user_input)
			else:
				if legit(user_input,player2_tiles):
					player2_score+=score_cal(user_input)

			print('\n'*50)
			print(play_board(board))		
			print(player1,'score:',player1_score)
			print(player2,'score:',player2_score)
			
	play()
#####################################################
#ADD MORE GAMES HERE
#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!#■!
if choice==1:
	import GTN
if choice==2:
	import RPS
	RPS.RPSmain()
if choice==3:
	import hangman
	hangman.hangmanmain()
if choice==4:
	import ttt
	ttt.tttmain()
if choice==5:
	import connect
	connect.connectmain()
if choice==6:
	Minesweeper()
if choice==7:
	scrabble()