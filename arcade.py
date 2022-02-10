#WELCOME TO THE ARCADE!
import random
import time
import sys

#importing the games
sys.path.insert(0,'games/')
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
7.scrabble
Enter your choice: \n ''')))                                   
#####################################################                        #COMPLETED


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
	import minesweeper
	minesweeper.Minesweeper()
if choice==7:
	import scrabble
	scrabble.scrabble()