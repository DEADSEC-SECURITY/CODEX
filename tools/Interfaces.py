#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *
#LOADS TOOLS
from tools.Interfaces import *

def InterfaceSelect(Menu):

    global NetworkInterfaces
    global interface

    #LOADS MENUS
    from Menus.DOS import Dos
    from Menus.NET import NET
    from Menus.WEB import WEB
    from codex import StartMenu

    OS()
    print()
    print(R + Banner)
    print(G + Dead)
    print(f"{B}********** Please select an interface **********")
    print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
    print()
    print(f"{C}----------")
    print(f"{G}Note: {W}Please write the interface the way it shows in the menu!")
    print(f"{C}----------")
    print(f"{P}Contribution: {W}We are looking for a way to make it so you dont need to write the hole interface name and only a number!")
    print(f"{C}----------{W}")
    print()
    interface = input("Please write the interface you want to use: ")
    logging.info("Selected new interface " + interface)
    if Menu == 'StartMenu':
        return StartMenu()
    if Menu == 'NET':
        return NET()
    if Menu == 'Dos':
        return Dos()
    else:
        return StartMenu()

def monitor(interface, mode, Menu):

    from Menus.NET import NET
    from Menus.DOS import Dos

    if mode == "managed":
        OS()
        os.system(f"sudo airmon-ng start {interface}")
        interface = interface + "mon"
        process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
        text = str(process.communicate()[0])
        begin = "ttype"
        end = "twiphy"
        CleanFile = text[text.find(begin):text.find(end)]
        mode = CleanFile[6:-3]
        logging.info("MONITOR MODE ENEBLED")

        print()
        print(f"{W}Interface now in {O}monitor{W} mode!")
        input(f"Press {O}ENTER{W} to continue!")
        if Menu == 'NET':
            return NET(interface)
        if Menu == 'Dos':
            return Dos(interface)
        else:
            return NET(interface)
    else:
        print(f"You wifi card is already in {O}monitor{W} mode!")
        input(f"Press {O}ENTER{W} to continue!")
        if Menu == 'NET':
            return NET(interface)
        if Menu == 'Dos':
            return Dos(interface)
        if Menu == 'HandShake':
            return HandShake(interface)
        else:
            return NET(interface)

def managed(interface, mode, Menu):

    from Menus.NET import NET
    from Menus.DOS import Dos

    if mode == "monitor":
        OS()
        os.system(f"sudo airmon-ng stop {interface}")
        interface = interface[:-3]
        process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
        text = str(process.communicate()[0])
        begin = "ttype"
        end = "twiphy"
        CleanFile = text[text.find(begin):text.find(end)]
        mode = CleanFile[6:-3]
        logging.info("MANAGED MODE ENEBLED")

        print()
        print(f"{W}Interface now in {O}managed{W} mode!")
        input(f"Press {O}ENTER{W} to continue")
        if Menu == 'NET':
            return NET(interface)
        if Menu == 'Dos':
            return Dos(interface)
        if Menus == 'HandShake':
            return HandShake(interface)
        else:
            return NET(interface)
    else:
        print(f"You wifi card is already in {O}manged{W} mode!")
        input(f"Press {O}ENTER{W} to continue!")
        if Menu == 'NET':
            return NET(interface)
        if Menu == 'Dos':
            return Dos(interface)
        if Menu == 'HandShake':
            return HandShake(interface)
        else:
            return NET(interface)
