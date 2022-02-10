import random
import time
import threading
import json
from nltk.corpus import words as nltk_words
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