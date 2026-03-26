from colorama import Style, Fore, Back, init
init(autoreset = True)

def doom_ascii(): 
    doom = Fore.GREEN + Style.BRIGHT + r''' 
 ____   ___   ___  __  __
|  _ \ / _ \ / _ \|  \/  |
| | | | | | | | | | |\/| |
| |_| | |_| | |_| | |  | |
|____/ \___/ \___/|_|  |_| 
    '''
    return doom

def gameover_ascii(): 
    gameover = Fore.RED + Style.NORMAL + r'''  
  ____    _    __  __ _____    _____     _______ ____  
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ 
 '''
    return gameover