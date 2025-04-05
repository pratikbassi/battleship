class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = [["O" for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.occupiedCoords = set()
        self.shots = {}

    def printBoard(self, showShips: bool = False, showShots: bool = False):
        for i in range(self.size):
            for j in range(self.size):
                if showShips:
                    if (i, j) in self.occupiedCoords:
                        self.board[i][j] = "S"
                    else:
                        self.board[i][j] = "O"
                if showShots:
                    if (i, j) in self.shots:
                        self.board[i][j] = self.shots[(i, j)]
                    else:
                        self.board[i][j] = "O"
        for row in self.board:
            print(" ".join(row))
            print("\n")

    def addShip(self, ship):
        shipCoords = self.__getShipCoords(ship.size, ship.coords, ship.direction)
        # Check if the coordinates are valid

        for coord in shipCoords:
            if not self.__isOccupied(coord) and self.__isValidCoords(coord):
                self.occupiedCoords.add(coord)
                self.ships.append(ship)

    def addShot(self, coord: tuple):
        if self.__isValidCoords(coord):
            if coord in self.occupiedCoords:
                self.shots[coord] = "H"
            else:
                self.shots[coord] = "M"

    def __isValidCoords(self, coord: tuple) -> bool:
        if coord[0] < 0 or coord[0] >= self.size or coord[1] < 0 or coord[1] >= self.size:
            return False
        return True

    def __isOccupied(self, coords) -> bool:
        # Check if the coordinates are already occupied
        if coords in self.occupiedCoords:
            return True
        return False

    def __getShipCoords(self, length, coords, direction) -> list:
        shipCoords = []
        if direction == "V":
            for i in range(length):
                shipCoords.append((coords[0] + i, coords[1]))
        elif direction == "H":
            for i in range(length):
                shipCoords.append((coords[0], coords[1] + i))
        return shipCoords
