#!/usr/bin/python

import time
import os
from rps import *

def output(s, color="default"):

	if (color == "default"):
		print(s, end="")
	elif (color == "red"):
		print("\033[31;1m{}\033[0m".format(s), end="")
	elif (color == "green"):
		print("\033[32;1m{}\033[0m".format(s), end="")
	elif (color == "yellow"):
		print("\033[33;1m{}\033[0m".format(s), end="")
	elif (color == "blue"):
		print("\033[34;1m{}\033[0m".format(s), end="")

def fancy(c):

	if c == "r" or c == "R":
		return "&"
	if c == "p" or c == "P":
		return "#"
	if c == "s" or c == "S":
		return "X"

def render(board):

	os.system("clear")

	output("\n")

	output("              [ ")
	output("ROCK ", color="red")
	output("PAPER ")
	output("SWITCH ", color="yellow")
	output("]\n")

	output("\n")

	output("    |")
	for i in range(0, 10):
		output(" {} ".format(i), color="green")
		output("|")

	output("\n")

	for i in range(0, 10):

		output(" ")
		for j in range(0, 11):
			output("---+")
		output("\n")

		output("  {} ".format(chr(0x61 + i)), color="green")
		output("|")

		for j in range(0, 10):
			if (board[i][j].isupper()):
				output(" {} ".format(fancy(board[i][j])), color="red")
			elif (board[i][j].islower()):
				output(" {} ".format(fancy(board[i][j])), color="blue")
			elif isswitch(i, j):
				output(" @ ", color="yellow")
			else:
				output("   ")
			output("|")

		output("\n")

	output("    +")
	for i in range(0, 10):
		output("---+")

	output("\n")

def welcome():

	os.system("clear")

	output("\n")
	output("Welcome to ")
	output("ROCK ", color="red")
	output("PAPER ")
	output("SWITCH \n", color="yellow")

	output("\n")

	output("Enter player 1 name: ")
	player1 = input()
	output("Enter player 2 name: ")
	player2 = input()

	return player1, player2

def gui_main():

	player1, player2 = welcome()

	turn = player1
	board = init_state()

	while not winner(board):

		render(board)

		output("\n")

		output("Turn: ")
		if turn == player1:
			output("{}\n".format(player1), color="red")
		elif turn == player2:
			output("{}\n".format(player2), color="blue")

		while True:

			output("Enter a move: ".format(turn))

			move = parse_move(input())

			t = 1 if turn == player1 else 2
			test = try_move(board, t, move)

			if test:

				board = test

				if turn == player1:
					turn = player2
				else:
					turn = player1

				break

			else:

				output("Illegal move\n", color="red")

	output("{} is the winner!\n".format(winner(board)))

if __name__ == "__main__":

	gui_main()
