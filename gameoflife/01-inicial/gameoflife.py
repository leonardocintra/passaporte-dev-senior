from copy import deepcopy
from os import system
from time import sleep


BLANK = "O"

def x(c):
    return c[0]


def y(c):
    return c[1]


def string(board):
    """Print the Board."""
    return "\n".join(("".join(row) for row in board))


def width(board):
    return len(board[0])


def height(board):
    return len(board)


def get_item(board, coord):
    return board[y(coord) - 1][x(coord) - 1]


def set_item(board, coord, value):
    board[y(coord) - 1][x(coord) - 1] = value


def set_many(board, coords, value):
    for c in coords:
        set_item(board, c, value)


def items(board):
    for coord in coord_of(board):
        yield coord, get_item(board, coord)


def get_many(board, coords):
    for coord in coords:
        yield get_item(board, coord)


def coord_of(board):
    yield from region(1, 1, width(board), height(board))


def region(colStart, rowStart, colStop, rowStop):
    for row in range(rowStart, rowStop + 1):
        for col in range(colStart, colStop + 1):
            yield col, row


def contains(board, coord):
    """Check if a cmd is out of list range."""
    return 1 <= x(coord) <= width(board) and 1 <= y(coord) <= height(board)


def offset(coord, rel):
    return x(coord) + x(rel), y(coord) + y(rel)


def create(board, w, h):
    """Create a array - 'I' Command."""
    board[:] = [[BLANK] * w for _ in range(h)]


def clear(board, value=BLANK):
    """Clean a array - 'C' Command."""
    set_many(board, coord_of(board), value)


DEAD = chr(0x00B7)
LIVE = chr(0x2588)

SURROUNDING = tuple((a, b)
                    for a in range(-1, 2)
                    for b in range(-1, 2)
                    if not (a == b == 0))

GLIDER = ((2, 1), (3, 2), (1, 3), (2, 3), (3, 3))


def main():

    def neighbors(c):
        yield from ((x(c) + a, y(c) + b) for a, b in SURROUNDING)

    def wrap(c, w, h):
        yield from ((a % w, b % h) for a, b in c)

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

    board = []
    create(board, 50, 25)
    clear(board, DEAD)
    set_many(board, GLIDER, LIVE)

    while True:
        try:
            system('clear')
            print(string(board))

            new_board = deepcopy(board)
            for coord, status in items(board):
                n = neighbors(coord)
                n = wrap(n, width(board), height(board))
                ns = get_many(board, n)
                total = how_many_alive(ns)

                set_item(new_board, coord, rule(coord, status, total))

            board = new_board
            sleep(0.05)
        except (KeyboardInterrupt, SystemExit):
            break


if __name__ == '__main__':
    main()
