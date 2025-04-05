from models.Board import Board
from models.Ship import Ship
class Player:
    def __init__(self, name: str, size, shipNames: list):
        self.shipData = {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
        }
        self.name = name
        self.board = Board(size)
        for name, coord in shipNames:
            ship = Ship(name, self.shipData[name])
            self.board.addShip(ship, coord)