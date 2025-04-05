from models.Game import Game
from tests.Test import TestRunner

if __name__ == "__main__":
    command = input("Enter 'test' to run tests or anything else to start a game: ").strip().lower()
    if command == 'test':
        # Run tests
        testRunner = TestRunner()
        testRunner.runTests()

    else:
        player1 = input("Enter player one's name: ").strip()
        player2 = input("Enter player two's name: ").strip()
        game = True
        while game:
            curGame = Game([player1, player2])
            keepPlaying = input("Do you want to play again? (y/n): ").strip().lower()
            if keepPlaying == 'y':
                continue
            else:
                game = False

    print("Goodbye!")
