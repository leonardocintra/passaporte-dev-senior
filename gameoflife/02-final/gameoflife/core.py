from copy import deepcopy

from gameoflife.bitmap import BoardTorus

DEAD = chr(0x00B7)
LIVE = chr(0x2588)

SURROUNDING = tuple((a, b)
                    for a in range(-1, 2)
                    for b in range(-1, 2)
                    if not (a == b == 0))

GLIDER = ((2, 1), (3, 2), (1, 3), (2, 3), (3, 3))


def neighbors(c):
    yield from (c + rel for rel in SURROUNDING)


def how_many_alive(l):
    return sum(1 for s in l if s == LIVE)


def should_die(total):
    return total < 2 or total > 3


def should_ressurect(total):
    return total == 3


def rule(c, status, total):
    s = status

    if status == LIVE:
        if should_die(total):
            s = DEAD
    else:
        if should_ressurect(total):
            s = LIVE

    return s


def setup(w, h):
    board = BoardTorus(w, h, DEAD)
    board.set_many(GLIDER, LIVE)
    return board


def update(board):
    new_board = deepcopy(board)
    for coord, status in board.items():
        n = neighbors(coord)
        ns = board.get_many(n)
        total = how_many_alive(ns)

        new_board[coord] = rule(coord, status, total)

    return new_board


def alive(board):
    for coord, status in board.items():
        if status == LIVE:
            yield coord


class GameOfLife:
    def __init__(self, w, h):
        self.board = setup(w, h)

    def __next__(self):
        self.board = update(self.board)
        return list(alive(self.board))

    def __str__(self):
        return str(self.board)
