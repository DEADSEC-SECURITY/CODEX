#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys

#LOADS TOOLS
from tools.nmap import *
from tools.airodump import *
#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *

#Variables
TraceBack = 1         # 0 For OFF | 1 For ON
sys.tracebacklimit = TraceBack

#CHECK ADIMIN PRIVIVILEDGES [ROOT]
def CheckAdminPrivs():

    if os.geteuid() != 0:
        print(C + Banner)
        print()
        exit(f"{Danger} {R}Error: Need to be run as {O}root\n{Danger} {R}Re-Run it but with {O} sudo {W}")
    else:
        return StartMenu()

#START MENU
def StartMenu():

    global OptionMenu
    global mode

    LoadJson()
    CheckDefaultInterface()
    CheckInterfaceState()

    #LOADS UTILS
    from utils.Verify import interface
    #LOADS TOOLS
    from tools.Interfaces import interface
    #LOADS MENU
    from Menus.NET import NET
    from Menus.WEB import WEB
    from Menus.DOS import Dos
    from tools.Interfaces import InterfaceSelect

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
    print(f"{B}************ Welcome to Codex ************{W}")
    print("1) WEB Attacks")
    print("2) Network Attacks")
    print(f"{B}**************** Options *****************{W}")
    print("3) Change interface")
    print(f"{B}************ Default Files ***************{W}")
    print("4) Change default ip address [NMAP]")
    print("5) Change default port range [NMAP]")
    print("6) Change default interface")
    print("")
    print(f"{C}----------{W}")
    print(f"{W}Interface {O}{interface}{W} selected. Mode {O}{mode}{W}.")
    print(f"{C}----------{W}")
    print(f"{G}Note: {W}In case you cant change from monitor to managed restart you pc!")
    print(f"{C}----------{W}")

    OptionMenu = int(input())

    if OptionMenu == 1:
        return WEB()
    if OptionMenu == 2:
        return NET(interface)
    if OptionMenu == 3:
        return InterfaceSelect('StartMenu')
    if OptionMenu == 4:
        return IP()
    if OptionMenu == 5:
        return PortRange()
    if OptionMenu == 6:
        return Interface()
    else:
        print(f"Please use only numbers between {O}1{W} and{O} 6{W}")
        input(f'Press {O}ENTER{W} to continue')
        return StartMenu()

CheckAdminPrivs()
