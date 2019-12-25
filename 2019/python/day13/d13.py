#! /usr/bin/env python3

from ..day05.intCode import Processor
import curses
from os import path
import time

EMPTY     = 0
WALL      = 1
BLOCK     = 2
H_PADDLE  = 3
BALL      = 4

LEFT      = -1
NEUTRAL   = 0
RIGHT     = 1

SYMBOLS = {
  EMPTY   : ' ',
  WALL    : '|',
  BLOCK   : '#',
  H_PADDLE: '_',
  BALL    : '.'
}

def get_input(file='input13.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return [int(x) for x in f.readline().rstrip('\n').rstrip('\r').split(',')]

def execute(w, program):
  max_x, max_y, blocks, score, move, cells = 0, 0, 0, 0, None, {}
  p = Processor(program, [])
  gen = p.process()
  ball_position, paddle_position = None, None
  while True:
    try:
      x, y, tile_id = next(gen), next(gen), next(gen)
      if w and tile_id == None:
        print_screen(w, cells, max_x, max_y, score)
        time.sleep(0.2)
        move = get_move_hack(w, ball_position, paddle_position)
        p.add_input(move)
        continue
      if x == -1 and y == 0 and (tile_id < 0 or tile_id > 4):
        score = tile_id
      else:
        cells[(x, y)] = tile_id
        if tile_id == BALL:
          ball_position = (x,y)
        elif tile_id == H_PADDLE:
          paddle_position = (x, y)
      max_x, max_y = max(x, max_x), max(y, max_y)
      blocks += BLOCK == tile_id
    except Exception:
      if w:
        w.addstr(f'Score: {score}')
        w.getch()
      return

def get_move_hack(w, ball_position, paddle_position):
  # w.getch()
  return 0 if ball_position[0] == paddle_position[0] else \
    1 if ball_position[0] > paddle_position[0] else -1


def get_move(stdscr):
  while True:
    move = stdscr.getch()
    if move == curses.KEY_LEFT: #'\x1b[D':
      move = LEFT
    elif move == curses.KEY_DOWN: #'\x1b[B':
      move = NEUTRAL
    elif move == curses.KEY_RIGHT: #'\x1b[C':
      move = RIGHT
    elif move == 113: #q:
      quit()
    if move in (LEFT, NEUTRAL, RIGHT):
      return move

def print_screen(stdscr, cells, max_x, max_y, score):
  stdscr.clear()
  stdscr.refresh()
  screen = [[' ' for r in range(max_x+1)] for c in range(max_y+1)]
  blocks = 0
  for (x, y), tile_id in cells.items():
    blocks += tile_id == BLOCK
    screen[y][x] = SYMBOLS[tile_id]
  
  for r in screen:
    # print(''.join(r))
    stdscr.addstr(''.join(r) + '\n')
  stdscr.addstr(' '.join(map(lambda x: str(x%10),range(len(screen[0])//2))) + '\n')

  stdscr.addstr(f'Blocks Left: {blocks}, Blocks Destroyed: {173-blocks}, Score: {score}\n')
  stdscr.refresh()

if __name__ == '__main__':
  execute(None, get_input())
  code = get_input()
  code[0] = 2
  curses.wrapper(execute, code)
  
