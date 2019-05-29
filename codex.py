#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 2.2.1---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import random
#IMPORT UTILS
from utils.colors import *
from utils.ExtraVariables import *
#Variables
TraceBack = 1         # 0 For OFF | 1 For ON
#TRACEBACK
sys.tracebacklimit = TraceBack
#AIRODUMP VARIABLES
FileName = 'AiroDumpOutPut' #You can edit this variable
Directory = 'Data/Aircrack-ng/' #You can edit this variable
#NMAP
nm = nmap.PortScanner()

#RANDOM
RR = random.randint(0, 100000)

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

        global interface
        global newinterface
        global ip
        global port

        with open('Data/DATA.json') as f:
            data = json.load(f)

        for DefaultInfo in data['DefaultInfo']:
            interface = DefaultInfo['defaultinterface']
            newinterface = DefaultInfo['defaultinterface']
            port = DefaultInfo['defaultportrange']
            ip = DefaultInfo['defaultipaddress']

        return Verify.DefaultInterface()

    #CHECKS IF INTERFACE IS IN MONITOR OR MANAGED
    def CheckInterfaceState():

        global interface
        global mode

        process = subprocess.Popen(['cat', f'/sys/class/net/{interface}/carrier'], stdout = subprocess.PIPE)
        text = str(process.communicate()[0])
        CleanText = text[2:-3]

        if CleanText == '1':
            interface = interface
            mode = 'managed'
            return Menus.StartMenu()

        if CleanText != '1':
            interface = interface + 'mon'
            mode = 'monitor'
            return Menus.StartMenu()

        else:
            OS()
            print(f'Problem loading interface please check line 67')
            input(f'Press {O}ENTER{W} to continue')
            sys.exit()

    #CHECKS FOR EXISTING DEFAULT INETERFACE
    def DefaultInterface():

            global interface

            #Netifaces
            NetworkInterfaces = netifaces.interfaces()

            if newinterface == 'NONE':
                OS()
                print(f'{B}********** Please select your default interface **********{W}')
                print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
                print()
                print(f'{C}----------{W}')
                print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
                print(f'{C}----------{W}')
                print()
                IntefaceNumber = int(input('Please select an interface: '))

                NTCount = len(NetworkInterfaces)

                if IntefaceNumber > NTCount:
                    print(f'Please use only numbers between {O}1{W} and{O} {NTCount}{W}')
                    input(f'Press {O}ENTER{W} to continue')
                    return InterfaceOptions.InterfaceSelect(Menu)

                else:
                    After = IntefaceNumber - 1
                    interface = str(NetworkInterfaces[After:IntefaceNumber])
                    inte = interface[2:-2]
                    #--------------------#

                    with open('Data/DATA.json') as f:
                        data = json.load(f)

                    data['DefaultInfo'][0]['defaultinterface'] = inte
                    with open('Data/DATA.json', 'w') as f:
                        json.dump(data, f, indent = 2)

                    print(f"Interface changed to {O}{inte}{W}")
                    input(f'Press {O}ENTER{W} to continue')
                    interface = inte
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
        print(f'1) WEB Attacks {O}[WORK IN PROGRESS]{W}')
        print('2) Network Attacks')
        print('3) Decrypt Menu')
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
        print(f'{W}Session code: {RR}')

        OptionMenu = str(input())

        if OptionMenu == '0':
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
        if OptionMenu == '1':
            return Menus.WEB()
        if OptionMenu == '2':
            return Menus.NET()
        if OptionMenu == '3':
            return Menus.OFFLINE_DECRYPT()
        if OptionMenu == '4':
            return InterfaceOptions.InterfaceSelect('StartMenu')
        if OptionMenu == '5':
            return Defaults.IP()
        if OptionMenu == '6':
            return Defaults.PortRange()
        if OptionMenu == '7':
            return Defaults.Interface()
        if OptionMenu == '':
            return Menus.StartMenu()
        else:
            print(f'Please use only numbers between {O}0{W} and{O} 6{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.StartMenu()

    #NET MENU
    def NET():

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
        print(f'8) Evil twin attack menu {O}[WORK IN PROGRESS]{W}')
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
        print(f'{W}Session code: {RR}')
        OptionNet = str(input())

        if OptionNet == '0':
            return Menus.StartMenu()
        if OptionNet == '1':
            return InterfaceOptions.InterfaceSelect('NET')
        if OptionNet == '2':
            return InterfaceOptions.monitor('NET')
        if OptionNet == '3':
            return InterfaceOptions.managed('NET')
        if OptionNet == '4':
            if mode == 'monitor':
                return AiroDump.Explorer('NET')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.NET()
        if OptionNet == '5':
            return Menus.DOS()
        if OptionNet == '6':
            return Menus.HANDSHAKE()
        if OptionNet == '7':
            return Menus.OFFLINE_DECRYPT_WPA('NET')
        if OptionNet == '8':
            pass
        if OptionNet == '9':
            return NMAPScan.menu()
        if OptionNet == '':
            return Menus.NET()
        else:
            print(f'Please use only numbers between {O}0{W} and{O} 9{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.NET()

    #WEB MENU
    def WEB():

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Web Attack Menu ************{W}')
        print('0) Return to main menu')
        print('1) Full Website Check')
        print('2) SQL Injection')
        print()
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')
        print(f'{W}Session code: {RR}')

        OptionWeb = str(input())

        if OptionWeb == '0':
            return Menus.StartMenu()
        if OptionWeb == '1':
            return WEBAM.FWC()
        if OptionWeb == '2':
            pass
        if OptionWeb == '':
            return Menus.WEB()
        else:
            print(f'Please use only numbers between {O}0{W} and{O} 2{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.StartMenu()

    #DOS MENU
    def DOS():


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
        print(f'{W}Session code: {RR}')

        DosOption = str(input())

        if DosOption == '0':
            return Menus.NET()
        if DosOption == '1':
            return InterfaceOptions.InterfaceSelect('DOS')
        if DosOption == '2':
            return InterfaceOptions.monitor('DOS')
        if DosOption == '3':
            return InterfaceOptions.managed('DOS')
        if DosOption == '4':
            if mode == 'monitor':
                return AiroDump.Explorer('DOS')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.DOS()
        if DosOption == '5':
            if mode == 'monitor':
                return Attacks.MDK3()
            if mode == 'managed':
                print(f'{Danger} Please put your card in{O} monitor {W}mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.DOS()
        if DosOption == '6':
            if mode == 'monitor':
                return Attacks.Aireplay()
            if mode == 'managed':
                print(f'{Danger} Please put your card in{O} monitor {W}mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.DOS()
        if DosOption == '7':
            if mode == 'monitor':
                return Attacks.Confusion()
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.DOS()
        if DosOption == '':
            return Menus.DOS()
        else:
            print(f'{Danger} Please only use numbers between {O}0{W} and{O} 7{W}')
            input(f'{Danger} Click {O}ENTER{W} to continue')
            return Menus.DOS()

    #HANDSHAKE MENU
    def HANDSHAKE():

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
        print(f'{W}Session code: {RR}')

        HandOption = str(input())

        if HandOption == '0':
            return Menus.NET()
        if HandOption == '1':
            return InterfaceOptions.InterfaceSelect('HANDSHAKE')
        if HandOption == '2':
            return InterfaceOptions.monitor('HANDSHAKE')
        if HandOption == '3':
            return InterfaceOptions.managed('HANDSHAKE')
        if HandOption == '4':
            if mode == 'monitor':
                return AiroDump.Explorer('HANDSHAKE')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()
        if HandOption == '5':
            if mode == 'monitor':
                return Attacks.HandShake('MDK3')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()
        if HandOption == '6':
            if mode == 'monitor':
                return Attacks.HandShake('Aireplay')
            if mode == 'managed':
                print(f'{Danger} Please put your card in {O}monitor{W} mode before using this!')
                input(f'{Danger} Click {O}ENTER{W} to continue')
                return Menus.HANDSHAKE()
        if HandOption == '':
            return Menus.HANDSHAKE()
        else:
            print(f'Please use only numbers between {O}0{W} and{O} 6{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.HANDSHAKE()

    #OFFLINE_DECRYPT MENU
    def OFFLINE_DECRYPT():
        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}************ Decrypt Menu ************{W}')
        print('0) Return to main menu')
        print('1) WPA/WPA2 decrypt menu')
        print(f'{C}----------{W}')
        print(f'2) Dictionary attack against capture file {P}[MD5] {O}[HashCat]{W}')
        print(f'3) Bruteforce attack against capture file {P}[MD5] {O}[HashCat]{W}')
        print(f'{C}----------{W}')
        print(f'4) Dictionary attack against capture file {P}[SHA256] {O}[HashCat]{W}')
        print(f'5) Bruteforce attack against capture file {P}[SHA256] {O}[HashCat]{W}')
        print('')
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')
        print(f'{W}Session code: {RR}')
        offlineOption = str(input())

        if offlineOption == '0':
            return Menus.StartMenu()
        if offlineOption == '1':
            return Menus.OFFLINE_DECRYPT_WPA('OFF')
        if offlineOption == '2':
            return Bruteforce.DicMD5('NONE', 'NONE')
        if offlineOption == '3':
            return Bruteforce.BruteMD5('NONE')
        if offlineOption == '4':
            return Bruteforce.DicSHA256('NONE', 'NONE')
        if offlineOption == '5':
            return Bruteforce.BruteSHA256('NONE')
        if offlineOption == '':
            return Menus.OFFLINE_DECRYPT()
        else:
            print(f'Please use only numbers between {O}1{W} and{O} 1{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT()

    #OFFLINE_DECRYPT_WPA MENU
    def OFFLINE_DECRYPT_WPA(Menu):

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
        print(f'{W}Session code: {RR}')
        offlineOption = str(input())

        if offlineOption == '0':
            if Menu == 'OFF':
                return Menus.OFFLINE_DECRYPT()
            if Menu == 'NET':
                return Menus.NET()
            else:
                return Menus.NET()
        if offlineOption == '1':
            return Bruteforce.DicAircrack('NONE', 'NONE')
        if offlineOption == '2':
            return Bruteforce.BruteAircrack('NONE', 'NONE')
        if offlineOption == '3':
            return Bruteforce.DicHashcat('NONE', 'NONE')
        if offlineOption == '4':
            return Bruteforce.BruteHashcat('NONE', 'NONE')
        if offlineOption == '5':
            return Bruteforce.RuleHashcat('NONE', 'NONE')
        if offlineOption == '':
            return Menus.OFFLINE_DECRYPT_WPA(Menu)
        else:
            print(f'Please use only numbers between {O}1{W} and{O} 5{W}')
            input(f'Press {O}ENTER{W} to continue')
            return Menus.OFFLINE_DECRYPT_WPA()

#Class for Web Attack
class WEBAM():
    def FWC():
        Web = input('Please enter the website you want to scan: ')
        TLD = get_tld(Web, as_object = True)
        WebNoWWWNoHTTP = TLD.fld

        OS()
        print('Starting ...')
        process = os.popen(f'whois {TLD}')
        WhoisOutput = str(process.read())

        print(WhoisOutput)

#Class for interface settings
class InterfaceOptions():

    #Select new interface
    def InterfaceSelect(Menu):

        global interface
        global mode

        #Netifaces
        NetworkInterfaces = netifaces.interfaces()

        OS()
        print()
        print(R + Banner)
        print(G + Dead)
        print(f'{B}********** Please select an interface **********')
        print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
        print()
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')
        print()
        IntefaceNumber = int(input('Please select an interface: '))

        NTCount = len(NetworkInterfaces)

        if IntefaceNumber > NTCount:
            print(f'Please use only numbers between {O}1{W} and{O} {NTCount}{W}')
            input(f'Press {O}ENTER{W} to continue')
            return InterfaceOptions.InterfaceSelect(Menu)

        else:
            After = IntefaceNumber - 1
            interface = str(NetworkInterfaces[After:IntefaceNumber])
            inte = interface[2:-2]
            #--------------------#
            process = subprocess.Popen(['cat', f'/sys/class/net/{inte}/carrier'], stdout = subprocess.PIPE)
            text = str(process.communicate()[0])
            CleanText = text[2:-3]

            if CleanText == '1':
                interface = inte
                mode = 'managed'
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

            if CleanText != '1':
                interface = inte + 'mon'
                mode = 'monitor'
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

            else:
                OS()
                print(f'Problem loading interface please check line 543')
                input(f'Press {O}ENTER{W} to continue')
                sys.exit()

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
        os.system(f'sudo xterm -title MDK3 -fg red -geometry 140x30-0+0 -e sudo mdk3 {interface} d -c {channel}')
        print(f'{R}CTRL-C detected! Ending attack!{W}')
        time.sleep(1)
        return Menus.DOS()

    def Aireplay():
        input(f'Click {O}ENTER{W} to start attack')
        print(f'Changing channel to {O}{channel}{W} ...')
        os.system(f'sudo iwconfig {interface} channel {channel}')
        time.sleep(1)
        print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
        os.system(f'sudo xterm -title AIREPLAY -fg red -geometry 140x30-0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
        print(f'{R}CTRL-C detected! Ending attack!{W}')
        time.sleep(1)
        return Menus.DOS()

    def Confusion():
        input(f'Click {O}ENTER{W} to start attack')
        time.sleep(1)
        print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
        os.system(f'sudo xterm -title CONFUSION -fg red -geometry 140x30-0+0 -e sudo mdk3 {interface} w -e {essid} -c {channel}')
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
                os.system(f'sudo xterm -title AIRODUMP -fg green -geometry 140x30-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -title AIREPLAY -fg red -geometry 140x30+0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
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
                os.system(f'sudo xterm -title AIRODUMP -fg green -geometry 100x20-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -title AIREPLAY -fg red -geometry 140x30+0+0 -e sudo aireplay-ng -0 0 -a {bssid} {interface}')
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
                os.system(f'sudo xterm -title AIRODUMP -fg green -geometry 140x30-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -title MDK3 -fg red -geometry 140x30+0+0 -e sudo mdk3 {interface} d -c {channel}')
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()
            else:
                print(f'Press {O}ENTER{W} to start attack')
                print(f'Starting attack ... {O}[CTRL-C to exit]{W}')
                os.system(f'sudo xterm -title AIRODUMP -fg green -geometry 140x30-0+0 -e sudo airodump-ng -c {channel} --bssid {bssid} -w Data/HandShakes/{FileName} {interface} & sudo xterm -title MDK3 -fg red -geometry 140x30+0+0 -e sudo mdk3 {interface} d -c {channel}')
                print(f'HandShake file saved in {O}Data/HandShakes{W}')
                input(f'Press {O}ENTER{W} to continue!')
                return Menus.HANDSHAKE()

#Class for airodump-ng
class AiroDump():

    def Explorer(Menu):

        FileNameCSV = f'{FileName}-01.csv'
        ExplorePath = os.path.isfile(f'{Directory}{FileNameCSV}')

        if ExplorePath == True:
            os.remove(f'{Directory}{FileNameCSV}')
            os.system(f'xterm -title AIRODUMP -geometry 140x30-0+0 -e sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}')
            return AiroDump.Decoder(Menu)
        else:
            os.system(f'xterm -title AIRODUMP -geometry 140x30-0+0 -e sudo airodump-ng -w {Directory}{FileName} --output-format csv {interface}')
            return AiroDump.Decoder(Menu)

    def Decoder(Menu):

        global id
        global channel
        global essid
        global encrypt
        global bssid

        FileNameCSV = f'{FileName}-01.csv'
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

#Class for bruteforce
class Bruteforce():

    def InputEditor(HPath, WLPath, Attack):
        #Detect if there is an WordListPath
        if WLPath == 'NONE':
            #Detect if 1 Char is '
            CheckAspas = HPath[:1]
            if CheckAspas == "'":
                HPathNO = HPath[1:-2]
                if Attack == 'DA':
                    return Bruteforce.BruteAircrack(HPathNO)
                if Attack == 'BA':
                    return Bruteforce.BruteAircrack(HPathNO)
                if Attack == 'BH':
                    return Bruteforce.BruteHashcat(HPathNO)
                if Attack == 'BM':
                    return Bruteforce.BruteMD5(HPathNO)
                if Attack == 'BS':
                    return Bruteforce.BruteSHA256(HPathNO)
            else:
                if Attack == 'DA':
                    return Bruteforce.BruteAircrack(HPath)
                if Attack == 'BA':
                    return Bruteforce.BruteAircrack(HPath)
                if Attack == 'BH':
                    return Bruteforce.BruteHashcat(HPath)
                if Attack == 'BM':
                    return Brutforce.BruteMD5(HPath)
                if Attack == 'BS':
                    return Bruteforce.BruteSHA256(HPath)
        else:
            #Detect if 1 Char is '
            CheckAspas = HPath[:1]
            WLCheckAspas = WLPath[:1]
            if CheckAspas == "'":
                HPathNO = HPath[1:-2]
                if WLCheckAspas == "'":
                    WLPathNO = WLPath[1:-2]
                    if Attack == 'DA':
                        return Bruteforce.DicAircrack(HPathNo, WLPathNO)
                    if Attack == 'DH':
                        return Bruteforce.DicHashcat(HPathNo, WLPathNO)
                    if Attack == 'RH':
                        return Bruteforce.RuleHashcat(HPathNo, WLPathNO)
                    if Attack == 'DM':
                        return Bruteforce.DicMD5(HPathNo, WLPathNO)
                    if Attack == 'DS':
                        return Bruteforce.DicSHA256(HPathNo, WLPathNO)
            else:
                if WLCheckAspas == "'":
                    WLPathNO = WLPath[1:-2]
                    if Attack == 'DA':
                        return Bruteforce.DicAircrack(HPath, WLPathNO)
                    if Attack == 'DH':
                        return Brutefoce.DicHashcat(HPath, WLPathNO)
                    if Attack == 'RH':
                        return Bruteforce.RuleHashcat(HPath, WLPathNO)
                    if Attack == 'DM':
                        return Bruteforce.DicMD5(HPath, WLPathNO)
                    if Attack == 'DS':
                        return Bruteforce.DicSHA256(HPath, WLPathNO)
                else:
                    if Attack == 'DA':
                        return Bruteforce.DicAircrack(HPath, WLPath)
                    if Attack == 'DH':
                        return Brutefoce.DicHashcat(HPath, WLPath)
                    if Attack == 'RH':
                        return Bruteforce.RuleHashcat(HPath, WLPath)
                    if Attack == 'DM':
                        return Bruteforce.DicMD5(HPath, WLPath)
                    if Attack == 'DS':
                        return Bruteforce.DicSHA256(HPath, WLPath)
    def WrongWordListDirectoryWPA():
        print('WordList path is wrong please try again!')
        input(f'Press {O}ENTER{W} to continue')
        return Menus.OFFLINE_DECRYPT_WPA()
    def WrongHandShakeDirectory():
        print('HandShake path is wrong please try again!')
        input(f'Press {O}ENTER{W} to continue')
        return Menus.OFFLINE_DECRYPT_WPA()
    def WrongWordListDirectoryHash():
        print(f"{R}WordList file path isn't correct!{W}")
        input(f'Press {O}ENTER{W} to continue')
        return Menus.OFFLINE_DECRYPT()
    def WrongHashDirectory():
        print(f"{R}Hash file path isn't correct!{W}")
        input(f'Press {O}ENTER{W} to continue')
        return Menus.OFFLINE_DECRYPT()
    def HashCatFormatError():
        print(f'{R}HashCat only supports .hccapx format!{W}')
        input(f'Press {O}ENTER{W} to continue')
        return Menus.OFFLINE_DECRYPT()

    def DicAircrack(HP, WL):
        if HP == 'NONE' or WL == 'NONE':
            print('Please enter full path for handshake file: ')
            HPath = str(input())
            print('Please enter full path for your wordlist: ')
            WLPath = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'DA')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            WLPVerify = os.path.isfile(f'{WL}')
            if HSPVerify == True:
                if WLPVerify == True:
                    print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                    time.sleep(2)
                    os.system(f'sudo aircrack-ng -w {WL} {HP}')
                    print(f'{R}Dictionary attack finished ...{W}')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
                else:
                    return Bruteforce.WrongWordListDirectoryWPA()
            else:
                return Bruteforce.WrongHandShakeDirectory()
    def BruteAircrack(HP):

        global NetWorkName
        global MinPassLength
        global MaxPassLength

        if HP == 'NONE':
            print('Please enter full path for handshake file: ')
            HP = str(input())
            print('Please enter minium password length: ')
            MinPassLength = str(input())
            print('Please enter max password length: ')
            MaxPassLength = str(input())
            print(f'Please enter the network name {O}[If the network name has spaces write it like this "Example\ Password "]{W}:')
            NetWorkName = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'BA')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            if HSPVerify == True:
                print(f'{R}WARNING: This process will take a lot of time!{W}')
                print(f'Starting bruteforce ... {O}[CTRL-C to exit]{W}')
                time.sleep(2)
                os.system(f'sudo crunch {MinPassLength} {MaxPassLength} abcdefghijklmnopqrstuvwxyz0123456789 | aircrack-ng -e {NetWorkName} -w - {handshakePath}')
                print(f'{R}Brutefoce attack finished ...{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT_WPA()
            else:
                return WrongHandShakeDirectory()
    def DicHashcat(HP, WL):
        if HP == 'NONE' or WL == 'NONE':
            print(f'Please enter full path for handshake file {O}[.hccapx]{W}: ')
            HPath = str(input())
            print('Please enter full path for your wordlist: ')
            WLPath = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'DA')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            WLPVerify = os.path.isfile(f'{WL}')
            if HSPVerify == True:
                if WLPVerify == True:
                    if HSPFormat == '.hccapx':
                        print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                        time.sleep(2)
                        os.system(f'sudo hashcat -a 0 -m 2500 {HP} {WL} --force')
                        print(f'{R}Dictionary attack finished ...{W}')
                        input(f'Press {O}ENTER{W} to continue')
                        return Menus.OFFLINE_DECRYPT()
                    else:
                        return Brutforce.HashCatFormatError()
                else:
                    return Bruteforce.WrongWordListDirectoryWPA()
            else:
                return Bruteforce.WrongHandShakeDirectory()
    def BruteHashcat(HP):

        global NetWorkName
        global MinPassLength
        global MaxPassLength

        if HP == 'NONE':
            print('Please enter full path for handshake file: ')
            handshakePath = str(input())
            print('Please enter minium password length: ')
            MinPassLength = str(input())
            print('Please enter max password length: ')
            MaxPassLength = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'BH')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
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
                    return Brutforce.HashCatFormatError()
            else:
                return Bruteforce.WrongWordListDirectoryWPA()
    def RuleHashcat(HP, WL):
        if HP == 'NONE' or WL == 'NONE':
            print(f'Please enter full path for handshake file {O}[.hccapx]{W}: ')
            HPath = str(input())
            print('Please enter full path for your wordlist: ')
            WLPath = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'DM')
        else:
            print('Please enter full path for your rule file: ')
            rulePath = str(input())
            CheckAspasRP = rulePath[:1]
            if CheckAspasRP == "'":
                rulePathNo = rulePath[1:-2]
                RPVerify = os.path.isfile(f'{rulePathNo}')
            else:
                    RPVerify = os.path.isfile(f'{rulePath}')
            HSPVerify = os.path.isfile(f'{HP}')
            WLPVerify = os.path.isfile(f'{WL}')
            if HSPVerify == True:
                if WLPVerify == True:
                    if HSPFormat == '.hccapx':
                        if RPVerify == True:
                            print(f'Starting rule attack ... {O}[CTRL-C to exit]{W}')
                            time.sleep(2)
                            os.system(f'sudo hashcat  -m 2500 -r {rulePath} {HP} {WL} --force')
                            print(f'{R}Dictionary attack finished ...{W}')
                            input(f'Press {O}ENTER{W} to continue')
                            return Menus.OFFLINE_DECRYPT()
                        else:
                            print('Rule path is wrong please try again!')
                            input(f'Press {O}ENTER{W} to continue')
                            return Menus.OFFLINE_DECRYPT()
                    else:
                        return Bruteforce.HashCatFormatError()
                else:
                    return Bruteforce.WrongWordListDirectoryWPA()
            else:
                return Bruteforce.WrongHandShakeDirectory()
    def DicMD5(HP, WL):
        if HP == 'NONE' or WL == 'NONE':
            print(f'Please enter full path for the MD5 hashes file: ')
            HPath = str(input())
            print('Please enter full path for your wordlist: ')
            WLPath = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'DM')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            WLPVerify = os.path.isfile(f'{WL}')
            if HSPVerify == True:
                if WLPVerify == True:
                    print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                    time.sleep(2)
                    os.system(f'sudo hashcat -m 0 -a 0 -o Data/FoundHashes/MD5-{RR}.txt --remove {HP} {WL} --force')
                    print(f'{R}Dictionary attack finished ...{W}')
                    print(f'{R}Cracked hashes saved to {O}Data/FoundHashes{W} file{W}')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
                else:
                    return Bruteforce.WrongWordListDirectoryHash()
            else:
                return Bruteforce.WrongHashDirectory()
    def BruteMD5(HP):
        if HP == 'NONE':
            print(f'Please enter full path for the MD5 hashes file: ')
            HPath = str(input())
            Bruteforce.InputEditor(HPath, 'NONE', 'BM')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            if HSPVerify == True:
                print(f'{R}WARNING: This process will take a lot of time!{W}')
                print(f'Starting bruteforce attack ... {O}[CTRL-C to exit]{W}')
                time.sleep(2)
                os.system(f'sudo hashcat -m 0 -a 3 -o Data/FoundHashes/MD5-{RR}.txt --remove {HP} --force')
                print(f'{R}Bruteforce attack finished ...{W}')
                print(f'{R}Cracked hashes saved to {O}Data/FoundHashes{W} file{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
            else:
                return Bruteforce.WrongHashDirectory()
    def DicSHA256(HP, WL):
        if HP == 'NONE' or WL == 'NONE':
            print(f'Please enter full path for the SHA256 hashes file: ')
            HPath = str(input())
            print('Please enter full path for your wordlist: ')
            WLPath = str(input())
            Bruteforce.InputEditor(HPath, WLPath, 'DS')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            WLPVerify = os.path.isfile(f'{WL}')
            if HSPVerify == True:
                if WLPVerify == True:
                    print(f'Starting dictionary attack ... {O}[CTRL-C to exit]{W}')
                    time.sleep(2)
                    os.system(f'sudo hashcat -m 1800 -a 0 -o Data/FoundHashes/SHA256-{RR}.txt --remove {HP} {WL} --force')
                    print(f'{R}Dictionary attack finished ...{W}')
                    print(f'{R}Cracked hashes saved to {O}Data/FoundHashes{W} file{W}')
                    input(f'Press {O}ENTER{W} to continue')
                    return Menus.OFFLINE_DECRYPT()
                else:
                    return Bruteforce.WrongWordListDirectoryHash()
            else:
                return Bruteforce.WrongHashDirectory()
    def BruteSHA256(HP):
        if HP == 'NONE':
            print(f'Please enter full path for the SHA256 hashes file: ')
            HPath = str(input())
            Bruteforce.InputEditor(HPath, 'NONE', 'BM')
        else:
            HSPVerify = os.path.isfile(f'{HP}')
            if HSPVerify == True:
                print(f'{R}WARNING: This process will take a lot of time!{W}')
                print(f'Starting bruteforce attack ... {O}[CTRL-C to exit]{W}')
                time.sleep(2)
                os.system(f'sudo hashcat -m 1800 -a 3 -o Data/FoundHashes/SHA256-{RR}.txt --remove {HP} --force')
                print(f'{R}Dictionary attack finished ...{W}')
                print(f'{R}Cracked hashes saved to {O}Data/FoundHashes{W} file{W}')
                input(f'Press {O}ENTER{W} to continue')
                return Menus.OFFLINE_DECRYPT()
            else:
                return WrongHashDirectory()

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
        print()
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')


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

#Class for defaults
class Defaults():

    def IP():

        with open('Data/DATA.json') as f:
            data = json.load(f)
        newip = input("Please enter your new default ip address: ")
        data['DefaultInfo'][0]['defaultipaddress'] = newip
        with open('Data/DATA.json', 'w') as f:
            json.dump(data, f, indent = 2)
        OS()
        print("Default ip address changed to " + newip)
        return Menus.StartMenu()

    def PortRange():
        with open('Data/DATA.json') as f:
            data = json.load(f)

            OS()
            print(R + Banner)
            print(G + Dead + W)
            print(f'{B}********** Please select your default interface **********{W}')
            print()
            print()
            newport = input("Please enter your new default port range: ")
            data['DefaultInfo'][0]['defaultportrange'] = newport

            with open('Data/DATA.json', 'w') as f:
                json.dump(data, f, indent = 2)

            OS()
            print("Default port range changed to " + newport)
            return Menus.StartMenu()

    def Interface():

        global interface

        #Netifaces
        NetworkInterfaces = netifaces.interfaces()

        OS()
        print(f'{B}********** Please select your default interface **********{W}')
        print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
        print()
        print(f'{C}----------{W}')
        print(f'{P}Contribution:{W} If you find any bug please help me fix it or report it to me!')
        print(f'{C}----------{W}')
        print()
        IntefaceNumber = int(input('Please select an interface: '))

        NTCount = len(NetworkInterfaces)

        if IntefaceNumber > NTCount:
            print(f'Please use only numbers between {O}1{W} and{O} {NTCount}{W}')
            input(f'Press {O}ENTER{W} to continue')
            return InterfaceOptions.InterfaceSelect(Menu)

        else:
            After = IntefaceNumber - 1
            interface = str(NetworkInterfaces[After:IntefaceNumber])
            inte = interface[2:-2]
            #--------------------#

            with open('Data/DATA.json') as f:
                data = json.load(f)

            data['DefaultInfo'][0]['defaultinterface'] = inte
            with open('Data/DATA.json', 'w') as f:
                json.dump(data, f, indent = 2)

            print(f"Interface changed to {O}{inte}{W}")
            input(f'Press {O}ENTER{W} to continue')
            interface = inte
            return Verify.CheckInterfaceState()

Verify.CheckAdminPrivs()
