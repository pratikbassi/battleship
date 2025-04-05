from models.Game import Game
from tests.Test import TestRunner

if __name__ == "__main__":
    command = input("Enter 'test' to run tests or 'play' to start a game: ").strip().lower()
    if command == 'test':
        # Run tests
        testRunner = TestRunner()
        testRunner.runTests()

    elif command == 'play':
        player1 = input("Enter player one's name").strip().split(",")
        player2 = input("Enter player two's name").strip().split(",")
        game = True
        while game:
            curGame = Game([player1, player2])
            game = False

    print("Goodbye!")
