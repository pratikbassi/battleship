class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = [["O" for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.occupiedCoords = set()

    def printBoard(self):
        print("  " + " ".join([str(i) for i in range(self.size)]))

    def addShip(self, ship, coords: tuple):
        if self.__checkShip(ship.size, coords, ship.direction):
            shipCoords = self.__getShipCoords(ship.size, coords, ship.direction)
            for coord in shipCoords:
                if not self.__isOverlap(coord):
                    self.occupiedCoords.add(coord)

        pass

    def __checkShip(self, length: int, coords: tuple, direction: str) -> bool:
        if direction == "V":
            # checks the vertically oriented ship
            if coords[0] + length > self.size or coords[0] < 0 or coords[1] < 0 or coords[1] >= self.size:
                return False
        elif direction == "H":
            # checks the horizontally oriented ship
            if coords[1] + length > self.size or coords[1] < 0 or coords[0] < 0 or coords[0] >= self.size:
                return False

        return True

    def __isOverlap(self, coords) -> bool:
        # Check if the coordinates are already occupied
        if coords in self.occupiedCoords:
            return True
        return False

    def __getShipCoords(self, length, coords, direction):
        shipCoords = []
        if direction == "V":
            for i in range(length):
                shipCoords.append((coords[0] + i, coords[1]))
        elif direction == "H":
            for i in range(length):
                shipCoords.append((coords[0], coords[1] + i))
        return shipCoords
