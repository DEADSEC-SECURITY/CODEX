#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *
#LOADS TOOLS
from tools.Interfaces import *
from tools.airodump import *

def NET(interface):

    global mode

    #LOADS Menus
    from codex import StartMenu
    from Menus.DOS import Dos
    from Menus.HandShake import HandShake
    #LOADS BSSID CHANNEL ESSID and ENCRYPTION
    from tools.airodump import bssid
    from tools.airodump import essid
    from tools.airodump import encrypt
    from tools.airodump import channel

    process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
    text = str(process.communicate()[0])
    begin = "ttype"
    end = "twiphy"
    CleanFile = text[text.find(begin):text.find(end)]
    mode = CleanFile[6:-3]

    OS()
    print()
    print(R + Banner)
    print(G + Dead)
    print(f"{B}************ Network Attack Menu ************{W}")
    print("0) Return to main menu")
    print("1) Select another network interface")
    print("2) Put interface in monitor mode")
    print("3) Put interface in managed mode")
    print("4) Explore for targets [Monitor Mode Needed]")
    print(f"{C}----------{W}")
    print("5) DoS Attack menu")
    print("6) HandShake Tools menu")
    print("7) WPA/WPA2 decrypt menu")
    print("8) Evil twin attack menu")
    print("9) NMAP menu")
    print("")
    print(f"{C}----------{W}")
    print(f"{W}Interface {O}{interface} {W}selected. Mode {O}{mode}{W}.")
    print(f"{C}----------{W}")
    print(f"Select ESSID:{O}{essid}{W}")
    print(f"Selected BSSID:{O}{bssid}{W}")
    print(f"Selected Channel:{O}{channel}{W}")
    print(f"Type of Encryption:{O}{encrypt}{W}")
    print(f"{C}----------{W}")
    print(f"{G}NOTE:{W} In case you cant change from monitor to managed restart you pc!")
    print(f"{C}----------{W}")
    OptionNet = int(input())

    if OptionNet == 0:
        return StartMenu()
    if OptionNet == 1:
        return InterfaceSelect('NET')
    if OptionNet == 2:
        return monitor(interface, mode, 'NET')
    if OptionNet == 3:
        return managed(interface, mode, 'NET')
    if OptionNet == 4:
        if mode == "monitor":
            return Explorer(interface, 'NET')
        if mode == "managed":
            print(f"Please put your card in {O}monitor{W} mode before using this!")
            input(f"Click {O}ENTER{W} to continue")
            return NET(interface)
    if OptionNet == 5:
        return Dos(interface)
    if OptionNet == 6:
        return HandShake(interface)
    if OptionNet == 7:
        pass
    if OptionNet == 8:
        pass
    if OptionNet == 9:
        return NMAPScan.menu()
