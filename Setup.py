#!/usr/bin/python3
#-*- coding: utf-8 -*-

#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 2.2.5---#

#IMPORT DEPENDENCYS
import os
#IMPORT UTILS
from utils.colors import *
from utils.ExtraVariables import *

if os.geteuid() != 0:
    print(C + Banner)
    print()
    exit(f'{Danger} {R}Error: Need to be run as {O}root\n{Danger} {R}Re-Run it but with {O} sudo {W}')
else:
    print(f'{R}Starting Setup for CODEX ...{W}')
    print(f'{Plus}{G} Installing TLD ...{W}')
    os.system('pip3 install tld')
    print(f'{Plus}{G} Installing PANDAS ...{W}')
    os.system('pip3 install pandas')
    print(f'{Plus}{G} Uninstalling NAMP ...{W}')
    os.system('pip3 uninstall nmap')
    os.system('pip uninstall nmap')
    print(f'{Plus}{G} Uninstalling Python-NAMP ...{W}')
    os.system('pip uninstall python-nmap')
    print(f'{Plus}{G} Installing Python-NMAP ...{W}')
    os.system('pip3 install python-nmap')
    print(f'{Plus}{G} Installing NETIFACES ...{W}')
    os.system('pip3 install netifaces')
    print(f'{R}Starting 3º party Setup for CODEX')
    print(f'{Plus}{G} Installing UPDATE ...{W}')
    os.system('sudo apt-get update')
    print(f'{Plus}{G} Installing AIRCRACK-NG ...{W}')
    os.system('sudo apt-get install aircrack-ng')
    print(f'{Plus}{G} Installing MDK3 ...{W}')
    os.system('sudo apt-get install MDK3')
    print(f'{Plus}{G} Installing HASHCAT ...{W}')
    os.system('sudo apt-get install hashcat')
    #print(f'{Plus}{G} Installing WHOIS ...{W}')
    #os.system('sudo apt-get install whois')
    print(f'{Plus}{G} Installing CRUNCH ...{W}')
    os.system('sudo apt-get install crunch -y')
    print(f'{Plus}{G} Installing XTERM ...{W}')
    os.system('sudo apt-get install xterm -y')
    print(f'{Plus}{G} Installing DRIFTNET ...{W}')
    os.system('sudo apt-get install driftnet -y')
    print(f'{Plus}{G} Installing DRIFTNET ...{W}')
    os.system('sudo apt-get install dsniff -y')
    print(f'{Plus}{G} Installing OPENCL ...{W}')
    os.system('sudo apt-get install ocl-icd-opencl-dev -y')
    print(f'{Plus}{G} Installing UNRAR ...{W}')
    os.system('sudo apt-get install unrar -y')
    print(f'{Plus}{G} Installing RUBY ...{W}')
    os.system('sudo apt-get install ruby -y')
    print(f'{Plus}{G} Installing UPDATE ...{W}')
    os.system('sudo apt-get update -y')
    INPUT = str(input(f'{Plus}{G} Would you like to extract all wordlists? [Y/N] {W}'))
    if INPUT == 'Y' or INPUT == 'y':
        os.system('unrar e WordLists/BIG-WPA-LIST-1.rar WordLists/')
        os.system('unrar e WordLists/BIG-WPA-LIST-2.rar WordLists/')
        os.system('unrar e WordLists/BIG-WPA-LIST-3.rar WordLists/')
    print(f'{C}INSTALLATION FINISHED YOU CAN NOW LAUNCH CODEX')
