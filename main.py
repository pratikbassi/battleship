from models.Game import Game
from tests.Test import TestRunner
from time import sleep

if __name__ == "__main__":
    command = input("Enter 'test' to run tests or anything else to start a game: ").strip().lower()
    if command == 'test':
        # Run tests
        testRunner = TestRunner()
        testRunner.runTests()

    else:
        player1 = input("Enter player one's name: ").strip()
        player2 = input("Enter player two's name: ").strip()
        while not player1 or not player2:
            print("Both players must have names.")
            player1 = input("Enter player one's name: ").strip()
            player2 = input("Enter player two's name: ").strip()
        game = True
        while game:
            curGame = Game([player1, player2])
            sleep(3)
            keepPlaying = input("Do you want to play again? (y/n): ").strip().lower()
            if keepPlaying == 'y':
                continue
            else:
                game = False

    print("Goodbye!")
