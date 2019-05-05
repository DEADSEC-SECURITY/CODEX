#IMPORT DEPENDENCYS
from tld import get_tld
import sys
import os
import json
import subprocess
import time
import pandas
import nmap
import netifaces

W = '\033[0m' # white (normal)
R = '\033[31m' # red
G = '\033[32m' # green
O = '\033[33m' # orange
B = '\033[34m' # blue
P = '\033[35m' # purple
C = '\033[36m' # cyan
GR = '\033[37m' # gray
D = '\033[2m' # dims current color. {W} resets.
Plus = f'{W}{D}[{W}{G}+{W}{D}]{W}' #[+]
Danger = f'{O}[{R}!{O}]{W}' #[!]
WTF = f'{W}[{C}?{W}]' #[?]

#OS to clean the screen
def OS():
    os.system('cls' if os.name == 'nt' else 'clear')


def InterfaceSelect():

    global interface
    global mode

    #Netifaces
    NetworkInterfaces = netifaces.interfaces()

    OS()
    print()
    print(f'{B}********** Please select an interface **********')
    print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
    print()
    print(f'{C}----------')
    print(f'{G}Note: {W}Please write the interface the way it shows in the menu!')
    print(f'{C}----------')
    print(f'{P}Contribution: {W}We are looking for a way to make it so you dont need to write the hole interface name and only a number!')
    print(f'{C}----------{W}')
    print()
    NumberInterface = int(input('Please write the interface you want to use: '))

    After = NumberInterface - 1
    interface = str(NetworkInterfaces[After:NumberInterface])
    inte = interface[2:-2]

    print(NetworkInterfaces)
    print(NumberInterface)
    print(interface)
    print(inte)


InterfaceSelect()
