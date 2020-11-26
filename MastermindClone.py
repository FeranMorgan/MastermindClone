import random


class MasterClone:

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7]
        self.guess = [0, 1, 2, 3, 4, 5, 6]
        self.prevGuesses = []
        self.guesses = 10
        self.matches = 0
        self.gameover = False
        self.palette = ["Red", "Orange", "Yellow", "Green", "Blue", "White", "Black"]
        self.fill()
        self.win = False

    # Randomly generates game board
    def fill(self):
        for i in range(len(self.board)):
            self.board[i] = self.palette[random.randint(0, len(self.board) - 1)]
        print(self.board)

    # Print all the previous guesses and their information
    def printPrevGuesses(self):
        for i in self.prevGuesses:
            print(i)

    # Count the number of matches in the current guess
    def countMatches(self):
        for i in range(len(self.board)):
            if self.board[i] == self.guess[i]:
                self.matches += 1
        return self.matches

    # Check win/loss and gameover conditions as well as accuracy of guesses
    def checkState(self):

        # Check if correct number of dots were added to guess
        if len(self.guess) != len(self.board):
            print("You didn't type the correct number of dots in your guess!")
        else:
            # Check total number of correct places
            matches = self.countMatches()
            self.guesses -= 1
            # Append the current guess, number of matches, and number of remaining guesses to list
            self.prevGuesses.append(str(self.guess) + ", Matches: " + str(matches) +
                                    ", Guesses Left: " + str(self.guesses))

            # Print list of previous guesses and their information
            self.printPrevGuesses()

            # Check if all places are correct and signal win if true
            if matches == len(self.board):
                self.win = True
                self.gameover = True
                print("You win!")
                return

            # Reset matches for the next guess
            self.matches = 0

            # Check if maximum number of guesses has been reached and signal loss if true
            if (self.guesses == 0):
                self.win = False
                self.gameover = True
                print("You lose!")
                print("The correct solution was: " + str(self.board))
                return
            return


game = MasterClone()

# Go game go!
print("Try to match 7 colored dots in the correct order using this color palette: ", game.palette)
print("You will see all of your previous guesses, the number of matches, and your remaining guesses")
print("Type your guess: ")
while (game.gameover == False):
    game.guess = input()
    game.guess = game.guess.split(" ")
    game.checkState()
