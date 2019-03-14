#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import os

#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *

FileName = 'AiroDumpOutPut'
FileNameCSV = f'{FileName}-01.csv'
Directory = 'tools/Data/Aircrack-ng/'
ExplorePath = os.path.isfile(f'{Directory}{FileNameCSV}')

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

def Explorer(interface, Menu):
    if ExplorePath == True:
        OS()
        os.remove(f'{Directory}{FileNameCSV}')
        os.system(f"sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}")
        return Decoder(interface, Menu)
    else:
        OS()
        os.system(f"sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}")
        return Decoder(interface, Menu)

def Decoder(interface, Menu):

    global bssid
    global channel
    global essid
    global encrypt

    from Menus.NET import NET
    from Menus.DOS import Dos

    CS = pandas.read_csv(f'{Directory}{FileNameCSV}')
    stop_row = CS[CS.BSSID == 'Station MAC'].index[0] -1

    OS()
    df = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
    df = df.drop(df.columns[[1, 2, 4, 6, 7, 9, 10, 11, 12, 14]], axis=1)
    print(df)
    print()
    ColectedInput = int(input("Please enter the number of the network: "))

    number = 0
    while number < 100:
        if ColectedInput == number:
            #GET THE SELECTED ROW
            out = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
            out = out.drop(out.columns[[1, 2, 4, 6, 7, 9, 10, 11, 12, 14]], axis=1)
            out = out.iloc[[number]]
            #GET BSSID
            bssid = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
            bssid = bssid.drop(bssid.columns[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
            bssid = bssid.iloc[[number]]
            bssid = bssid.to_string(index=False, header=False, skipinitialspace=True)
            #GET CHANNEL
            channel = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
            channel = channel.drop(channel.columns[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
            channel = channel.iloc[[number]]
            channel = channel.to_string(index=False, header=False, skipinitialspace=True)
            #GET ESSID
            essid = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
            essid = essid.drop(essid.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]], axis=1)
            essid = essid.iloc[[number]]
            essid = essid.to_string(index=False, header=False, skipinitialspace=True)
            #GET ENCRYPTION
            encrypt = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
            encrypt = encrypt.drop(encrypt.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
            encrypt = encrypt.iloc[[number]]
            encrypt = encrypt.to_string(index=False, header=False, skipinitialspace=True)

            if Menu == 'Dos':
                return Dos(interface)
            if Menu == 'NET':
                return NET(interface)
            else:
                return NET(interface)
        number = number + 1
