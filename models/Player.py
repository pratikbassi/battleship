from models.Board import Board
from models.Ship import Ship


class Player:
    def __init__(self, name: str, size, shipsToMake: list):

        self.name = name
        self.board = Board(size)
        for ship in shipsToMake:
            ship = Ship(ship[0], ship[1], ship[2])
            self.board.addShip(ship)
