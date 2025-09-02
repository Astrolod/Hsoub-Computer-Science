import random
import tkinter as tk

class Game:

    def chosenumber(self, end):

            self.Rnumber = random.randint(1, end)
            xnumber = None

            while xnumber != self.Rnumber:
             xnumber = int (input("Choose a number between 1 and " + str(end) + ": "))

             if xnumber == self.Rnumber:
                print("You won!")
             elif xnumber > self.Rnumber:
                print("too high!")
             else:
                print("too low!")

    def play(self):

        again = True
        turn = 0

        while again == True:
            turn += 10
            self.chosenumber(end = turn)

            while True:
                ask = input("Do you want to play again? (y/n): ")

                if ask == "n":
                    print("Thank you for playing!")
                    again = False
                    break
                elif ask == "y":
                    again = True
                    break
                else:
                    print("That's not a valid input. Please try again.")

if __name__ == "__main__":
    game = Game()
    game.play()
