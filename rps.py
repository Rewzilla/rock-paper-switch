#!/usr/bin/python

def init_state():

	return [
		[' ', ' ', ' ', ' ', ' ', 'r', 'p', 's', 's', 's'],
		[' ', ' ', ' ', ' ', ' ', ' ', 'r', 'p', 'p', 's'],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'p', 's'],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'p'],
		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r'],
		['R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		['P', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		['S', 'P', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		['S', 'P', 'P', 'R', ' ', ' ', ' ', ' ', ' ', ' '],
		['S', 'S', 'S', 'P', 'R', ' ', ' ', ' ', ' ', ' '],
	]

def isswitch(i, j):

	if i == 3 and j == 3:
		return True
	elif i == 6 and j == 3:
		return True
	elif i == 6 and j == 3:
		return True
	elif i == 3 and j == 6:
		return True
	elif i == 6 and j == 6:
		return True
	else:
		return False

def winner(board):

	counts = {
		"r" : 0,
		"p" : 0,
		"s" : 0,
		"R" : 0,
		"P" : 0,
		"S" : 0,
		"@" : 0,
		" " : 0,
	}

	for i in range(0, 9):
		for j in range(0, 9):
			counts[board[i][j]] += 1

	if counts["r"] == 0 or counts["s"] == 0 or counts["p"] == 0:
		return player1
	elif counts["R"] == 0 or counts["S"] == 0 or counts["P"] == 0:
		return player2
	else:
		return None

def parse_move(s):

	return {
		"sy" : ord(s[0]) - 0x61,
		"sx" : int(s[1]),
		"ey" : ord(s[2]) - 0x61,
		"ex" : int(s[3]),
		"xy" : ord(s[4]) - 0x61 if len(s) > 4 else "?",
		"xx" : int(s[5]) if len(s) > 4 else "?",
	}

def try_move(board, turn, move):

		sy = move["sy"]
		sx = move["sx"]
		ey = move["ey"]
		ex = move["ex"]
		xx = move["xx"]
		xy = move["xy"]

		# You must move your own piece
		if turn == 1 and not board[sy][sx].isupper():
			return False
		if turn == 2 and not board[sy][sx].islower():
			return False

		# Rocks must only go orthogonal and diagonal
		if board[sy][sx] in ["R", "r"] and sx - ex != 0 and sy - ey != 0 and abs(sx - ex) != abs(sy - ey):
			return False

		# Rocks can only go three spaces
		if board[sy][sx] in ["R", "r"] and (abs(sx - ex) > 3 or abs(sy - ey) > 3):
			return False

		# Scissors can only move diagonally
		if board[sy][sx] in ["S", "s"] and abs(sx - ex) != abs(sy - ey):
			return False

		# Paper can only move orthogonally
		if board[sy][sx] in ["P", "p"] and abs(sx - ex) != 0 and abs(sy - ey) != 0:
			return False

		# Nothing may be in the way
		tx = sx
		ty = sy
		while abs(ty - ey) > 1 and abs(tx - ex) > 1:

			if ty == ey:
				pass
			elif ty < ey:
				ty += 1
			else:
				ty -= 1

			if tx == ex:
				pass
			elif tx < ex:
				tx += 1
			else:
				tx -= 1

			if board[ty][tx] != " ":
				return False

		# You can't kill your own pieces
		if board[sy][sx].isupper() and board[ey][ex].isupper():
			return False
		if board[sy][sx].islower() and board[ey][ex].islower():
			return False

		# Rock Paper Scissors kill rules
		if board[sy][sx] in ["R", "r"] and board[ey][ex] in ["R", "r", "P", "p"]:
			return False
		if board[sy][sx] in ["P", "p"] and board[ey][ex] in ["S", "s", "P", "p"]:
			return False
		if board[sy][sx] in ["S", "s"] and board[ey][ex] in ["R", "r", "S", "s"]:
			return False

		# Handle switches
		if isswitch(ey, ex):

			# Must supply a third set of coords
			if xy == "?" or xx == "?":
				return False

			# Must switch with your own piece
			if board[sy][sx].isupper() and not board[xy][xx].isupper():
				return False
			if board[sy][sx].islower() and not board[xy][xx].islower():
				return False

			board[ey][ex] = board[sy][sx]
			tmp = board[ey][ex]
			board[ey][ex] = board[xy][xx]
			board[xy][xx] = tmp
			board[sy][sx] = " "

		else:

			board[ey][ex] = board[sy][sx]
			board[sy][sx] = " "

		return board
