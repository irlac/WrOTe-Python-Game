#Wrath of Tenepres - Adventure Game by Camden Richter

#imports
import datetime
import time
import currency
from prettytable import PrettyTable


#class definitions
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


#variable definitions
realDate = datetime.datetime.date(datetime.datetime.now())
realTime = datetime.datetime.time(datetime.datetime.now())
playerName = "You"
charName = "Guy"
location = "Some Place"
beastName = "Beast"
message = str()
pause = time.sleep
txtForm = int()
formatChosen = 'null'


#function definitions
def player(message):
    (print("{0}: {1}".format(playerName, message)))


def char(message):
    (print("{0}: {1}".format(charName, message)))


def beast(message):
    (print(Color.BOLD + "{0}: {1}".format(beastName, message) + Color.END))



def form(txtForm):
    if txtForm == 1:
        formatChosen == playerName
    elif txtForm == 2:
        formatChosen == location
    elif txtForm == 3:
        formatChosen == charName
    elif txtForm == 4:
        formatChosen == beastName
    elif txtForm == 5:
        formatChosen == realTime
    elif txtForm == 6:
        formatChosen == realDate
    elif txtForm == 7:
        formatChosen == fakeBeast
    '.format(formatChosen)'


#game
print(Color.BOLD + Color.UNDERLINE + 'Wrath of Tenepres' + Color.END)
pause(2)
print(Color.BOLD + 'Chapter 1: Awake' + Color.END)
pause(2)
print()
playerName = input("...Hello? You! What is your name? ")
player("I think it's {0}.".format(playerName))
pause(1.5)
char("You think? Ok, anyway {0},".format(playerName))
pause(1.5)
location = input("Would you mind telling me where we are? ")
player("Uh... {0}... maybe?".format(location))
pause(1.5)
char("Great. Thanks... {0}... I'm sorry, I just seem to have forgotten everything... It's weird...".format(location))
pause(3)
player("Yeah, I seem to have as well...")
pause(1.5)
charName = input("Do you know what my name is? ")
player("I mean, your nametag says {0}.".format(charName))
pause(1.5)
char("Oh, right. {0}... sounds nice.".format(charName))
pause(1.5)
print(Color.BOLD + 'BEINGS. WELCOME TO MY LAND. YOU ARE NOW MY SLAVES.' + Color.END)
pause(1.5)
player("What the!?")
pause(1)
char("{1}, let's get out of here!".format(charName, playerName))
pause(1.5)
beast('YOU WILL NOT RUN, FOR THERE IS NOWHERE TO GO.')
pause(1.5)
beastName = input("{0}: What is that thing!? ".format(charName))
player("It looks like {0}!".format(beastName))
fakeBeast = beastName
pause(1.5)
beast('FOOLS, I AM NOT {0}, I AM TENEPRES, GOD OF ALL'.format(beastName))
beastName = "Tenepres"
pause(0.5)
beast('AS PROOF THAT I AM ALL MIGHTY, I KNOW THAT THE TIME IS {0} ON THE DAY OF {1}'.format(realTime,realDate))
pause(1.5)
player("Jeez")
pause(1.5)
char("I know! Let's go to that shop! I'm sure it has something we can use to fight this... {0}!".format(fakeBeast))
pause(1.5)
shop.main()
