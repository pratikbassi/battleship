from models.Player import Player
SHIPS = [
    ("Carrier", (0, 0), "H"),
    ("Battleship", (1, 0), "H"),
    ("Cruiser", (2, 0), "H"),
    ("Submarine", (3, 0), "H"),
    ("Destroyer", (4, 0), "H")
]

class Game:
    def __init__(self, playerNames):
        self.player2 = None
        self.player1 = None
        print("Initializing game...")
        self.startGame(playerNames)
        print("Game initialized.")
        self.play()

    def startGame(self, playerNames):
        self.player1 = Player(
            playerNames[0],
            10,
            SHIPS)
        self.player2 = Player(
            playerNames[1],
            10, SHIPS)
        print(f"Welcome to Battleship, {self.player1.name} and {self.player2.name}!")

    def __runTurn(self, currentPlayer, targetPlayer):
        print(f"{currentPlayer.name}'s turn.")
        print(f"{targetPlayer.name}'s board:")
        targetPlayer.board.printBoard(showShots=True)
        row = int(input("Enter row to shoot at: "))
        column = int(input("Enter column to shoot at: "))
        valid = targetPlayer.board.addShot((row, column))
        while not valid:
            print("Invalid coordinates. Try again.")
            row = int(input("Enter row to shoot at: "))
            column = int(input("Enter column to shoot at: "))
            valid = targetPlayer.board.addShot((row, column))

        if gameOver := self.__gameOver():
            print(f"{currentPlayer.name} wins!")
            return True
        else:
            print(f"{currentPlayer.name} shot at ({row}, {column}) and hit {targetPlayer.board.shots[(row, column)]}.")
            targetPlayer.board.printBoard(showShots=True)
            return False

    def play(self):
        while True:
            if self.__runTurn(self.player1, self.player2):
                break
            if self.__runTurn(self.player2, self.player1):
                break

    def __gameOver(self):
        return self.player1.board.checkAllShipsDestroyed() or self.player2.board.checkAllShipsDestroyed()

