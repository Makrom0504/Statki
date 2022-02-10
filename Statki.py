# create an empty board
def init_board():
	board = []
	for i in range(10):
		board_row = ['_'] * 10
		board.append(board_row)
	return board


def run_game():
	board = init_board()
	board2 = init_board()
	#print_2boards(board, board2)


run_game()
