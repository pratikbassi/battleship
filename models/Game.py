from models.Player import Player


class Game:
    def __init__(self, playerNames):
        self.player2 = None
        self.player1 = None
        print("Initializing game...")
        self.startGame(playerNames)

    def startGame(self, playerNames):
        self.player1 = Player(
            playerNames[0],
            10,
            [("Carrier", (0, 0), "H")])
        self.player2 = Player(
            playerNames[1],
            10, [("Carrier", (0, 0), "H")])
        print(f"Welcome to Battleship, {self.player1.name} and {self.player2.name}!")
