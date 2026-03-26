import playgame
import ascii
import functions

while True:
    playgame.start_game()   # play one full run

    while True:
        print("")
        playagain = input("Do you want to play again to discover another ending? Y/N ").lower().strip()
        print("")

        if playagain in ("n", "no"):
            exit()

        elif playagain in ("y", "yes"):
            print("")
            break   # break inner loop → outer loop starts a new game

        else:
            print("Enter the choice again: Y/N")

