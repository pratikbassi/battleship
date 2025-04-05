from models.Board import Board
from models.Ship import Ship


class Player:
    def __init__(self, name: str, size, shipsToMake: list):

        self.name = name
        self.board = Board(size)
        for (name, coord, direction) in shipsToMake:
            ship = Ship(name, coord, direction)

