import time
import random
def connectmain():
	print('~ WELCOME TO CONNECT 4 ~')
	time.sleep(0.75)
	print('~ PLAYER-1 ~')
	time.sleep(0.5)
	player1 = input('enter your name:\n')
	time.sleep(1)
	print('~ PLAYER-2 ~')
	time.sleep(0.5)
	player2 = input('enter your name:\n')
	row = []
	board = []
	for i in range(7):
		row.append(' ')
	for i in range(6):
		board.append(row)
	print(player1,'vs',player2)
	time.sleep(0.75)
	print("here's you board.")
	time.sleep(0.75)
	q = '| |'
	print('  1    2    3    4    5    6    7')
	
	board =[['| |', '| |', '| |', '| |', '| |', '| |', '| |'],
			['| |', '| |', '| |', '| |', '| |', '| |', '| |'],
			['| |', '| |', '| |', '| |', '| |', '| |', '| |'],
			['| |', '| |', '| |', '| |', '| |', '| |', '| |'],
			['| |', '| |', '| |', '| |', '| |', '| |', '| |'],
			['| |', '| |', '| |', '| |', '| |', '| |', '| |']]
	for i in range(len(board)):
		for j in range(len(board[i])):
			print('',board[i][j],end=' ')
		print()
		time.sleep(0.1)
		

	def start():
		a = '|0|'
		b = '|■|'
		#  ■
		running = True
		while running:
			print('PLAYER-1')
			play1 = int(input('enter the position of your coin:\n'))
			for j in range(1,len(board)+1):

				if board[len(board)-j][play1-1] == '| |':

					board[len(board)-j][play1-1] = '|0|'
					break

				elif board[len(board)-j][play1-1] != '|0|':
					pass
				#
			#
			print('  1    2    3    4    5    6    7')
			for i in range(len(board)):
				for j in range(len(board[i])):
					print('',board[i][j],end=' ')
				print()
				time.sleep(0.1)
			#
			print('PLAYER-2')
			play2 = int(input('enter the position of your coin;\n'))
			
			#
			for j in range(1,len(board)+1):

				if board[len(board)-j][play2-1] == '| |':

					board[len(board)-j][play2-1] = '|■|'
					break

				elif board[len(board)-j][play2-1] != '|■|':
					pass
			#
			print('  1    2    3    4    5    6    7')
			for i in range(len(board)):
				for j in range(len(board[i])):
					print('',board[i][j],end=' ')
				print()
				time.sleep(0.1)

			###############VICTORY-CHECK#############
			def win(tile):
				global victory
				victory = 0
				###horizontal###
				for i in range(7-3):
					for j in range(6):
						if board[j][i] == tile and board[j][i+1] == tile and board[j][i+2] == tile and board[j][i+3] == tile:
							victory = 1
							return  True
							running = False
							break
				###vertical###
				for i in range(7):
					for j in range(6-3):
						if board[j][i] == tile and board[j+1][i] == tile and board[j+2][i] == tile and board[j+3][i] == tile:
							victory = 1
							return  True
							running = False
							break
				###diagonal###
				for i in range(7-3):
					for j in range(6-3):
						if board[j][i] == tile and board[j+1][i+1] == tile and board[j+2][i+2] == tile and board[j+3][i+3] == tile:
							victory = 1
							return  True
							running = False
							break
				###diagonal###
				for i in range(7-3):
					for j in range(3,6):
						if board[j][i] == tile and board[j-1][i+1] == tile and board[j-2][i+2] == tile and board[j-3][i+3] == tile:
							victory = 1
							return  True
							running = False
							break
			###############VICTORY-CHECK#############
			if win(a):
				print('CONGRATULATIONS',player1)
				running = False
			if win(b):
				print('CONGRATULATIONS',player2)
				running = False





	start()                                    