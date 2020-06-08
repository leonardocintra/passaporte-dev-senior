from collections import namedtuple

BLANK = "O"


class Board:
    def __init__(self, w, h, value=BLANK):
        """Create a array - 'I' Command."""
        self.board = [[value] * w for _ in range(h)]

    def __str__(self):
        """Print the Board."""
        return "\n".join(("".join(row) for row in self.board))

    @property
    def width(self):
        return len(self.board[0])

    @property
    def height(self):
        return len(self.board)

    @staticmethod
    def index(coord):
        if not isinstance(coord, Coord):
            coord = Coord(*coord)
        return coord + (-1, -1)

    def __getitem__(self, coord):
        c = self.index(coord)
        return self.board[c.y][c.x]

    def __setitem__(self, coord, value):
        c = self.index(coord)
        self.board[c.y][c.x] = value

    def set_many(self, coords, value):
        for c in coords:
            self[c] = value

    def items(self):
        for coord in self.coord_of():
            yield coord, self[coord]

    def get_many(self, coords):
        for coord in coords:
            yield self[coord]

    def __contains__(self, coord):
        """Check if a cmd is out of list range."""
        return 1 <= coord.x <= self.width and 1 <= coord.y <= self.height

    def coord_of(self):
        yield from region(1, 1, self.width, self.height)


class BoardTorus(Board):
    def index(self, coord):
        return super().index(coord) % (self.width, self.height)


class Coord(namedtuple('Coord', 'x y')):
    def __add__(self, other):
        return Coord(self.x + other[0], self.y + other[1])

    def __mod__(self, other):
        return Coord(self.x % other[0], self.y % other[1])

    def __mul__(self, scalar):
        return Coord(self.x * scalar, self.y * scalar)


def region(colStart, rowStart, colStop, rowStop):
    for row in range(rowStart, rowStop + 1):
        for col in range(colStart, colStop + 1):
            yield Coord(col, row)

