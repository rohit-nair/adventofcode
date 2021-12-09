#! /usr/bin/env python3

from os import path

def process():
  called_numbers, boards = get_input()

  bingo_boards = []
  for called_number in called_numbers:
    for board_idx, board in enumerate(boards):
      bingo, score = run_round_for_board(board, called_number)

      if bingo:
        # print(f'Bingo! Board {board_idx}. Score is {score}.')
        # return
        if board_idx not in [b[0] for b in bingo_boards]:
          if len(bingo_boards) + 1 == len(boards):
            print(f'Slowest bingo board has idx: {board_idx} has score: {score}.')
            return
          bingo_boards.append((board_idx, score))

def print_boards(boards):
  for board in boards:
    print_board(board)

def print_board(board):
  for row in board:
    print(row)
  print('-----------------------')

def run_round_for_board(board, called_number):
  for y, row in enumerate(board):
    if called_number in row:
      x = row.index(called_number)
      board[y][x] = None
      if check_board(board, x, y):
        return True, compute_result(board, called_number)

  return False, None

def check_board(board, x, y):
  for row in board:
    if all([r is None for r in row]):
      return True

  for col in zip(*board):
    if all([c is None for c in col]):
      return True
  
  return False

def compute_result(board, called_number):
  score = sum([sum([r for r in row if r is not None]) for row in board])
  # print(board, score, called_number)
  return score*called_number


def get_input():
    called_numbers, boards, board = [], [], []
    with open(path.join(path.dirname(__file__), 'input04.txt'), 'r+') as f:
      for l in f.readlines():
        if not called_numbers:
          called_numbers = list(map(int, l.strip().split(',')))
          continue

        if l.strip() == '':
          if len(board) > 0:
            boards.append(board)
            board = []
          continue
        
        board.append(list(map(int, l.split())))

    if len(board) > 0:
      boards.append(board)

    return called_numbers, boards


process()