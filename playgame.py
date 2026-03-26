import ascii
import time
import functions
from colorama import Style, Back, Fore, init
init(autoreset = True)

def start_game():
    print("Hi. Welcome to the Temple of -")
    print(ascii.doom_ascii())

    name1 = functions.getplayer_name()
    choice1 = functions.player_choice()