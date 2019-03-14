#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import subprocess
import netifaces

#OS to clean the screen
def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

#Load all json
def LoadJson():

    global newinterface

    with open('Data/DATA.json') as f:
        data = json.load(f)

    for DefaultInfo in data['DefaultInfo']:
        newinterface = DefaultInfo['defaultinterface']

#Checks if interface is in monitor or managed mode
def CheckInterfaceState():

    global interface

    process = subprocess.Popen(['cat', f'/sys/class/net/{newinterface}/carrier'], stdout=subprocess.PIPE)
    text = str(process.communicate()[0])
    CleanText = text[2:-3]

    if CleanText == "1":
        interface = newinterface

    if CleanText != "1":
        interface = newinterface + 'mon'

#Checks for existign default interface
def CheckDefaultInterface():

    global newinterface

    if newinterface == "NONE":
        OS()
        print("********** Please select your default interface **********")
        print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
        print()
        print(W + "----------")
        print(R + "Note: Please write the interface the way it shows in the menu!")
        print(R + "Note: You can change the interface later if you need!")
        print(W + "----------")
        print(Y + "Contribution: We are looking for a way to make it so you dont need to write the hole interface name and only a number!")
        print(W + "----------")
        print()
        newinterface = input("Please write your new default interface: ")

        data['DefaultInfo'][0]['defaultinterface'] = defaultinterface = newinterface
        with open('Data/DATA.json', 'w') as f:
            json.dump(data, f, indent = 2)

        logging.info("New default interface added " + newinterface)

        return CheckInterfaceState()
    else:
        return CheckInterfaceState()
