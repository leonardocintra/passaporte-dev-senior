from os import system
from time import sleep

from gameoflife.core import GameOfLife


def show(board):
    system('clear')
    print(board)


def cli():
    gol = GameOfLife(50, 25)

    while True:
        try:
            next(gol)
            show(str(gol))
            sleep(0.05)
        except (KeyboardInterrupt, SystemExit):
            break

