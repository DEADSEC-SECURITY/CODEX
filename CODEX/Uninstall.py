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
    print(f'{Plus}{G} Uninstalling TLD ...{W}')
    os.system('pip3 uninstall tld')
    print(f'{Plus}{G} Uninstalling PANDAS ...{W}')
    os.system('pip3 uninstall pandas')
    print(f'{Plus}{G} Uninstalling Python-NMAP ...{W}')
    os.system('pip3 uninstall python-nmap')
    print(f'{Plus}{G} Uninstalling NETIFACES ...{W}')
    os.system('pip3 uninstall netifaces')
    print(f'{Plus}{G} Uninstalling AIRCRACK-NG ...{W}')
    os.system('sudo apt purge install aircrack-ng')
    print(f'{Plus}{G} Uninstalling MDK3 ...{W}')
    os.system('sudo apt purge install MDK3')
    print(f'{Plus}{G} Uninstalling HASHCAT ...{W}')
    os.system('sudo apt purge install hashcat')
    #print(f'{Plus}{G} Installing WHOIS ...{W}')
    #os.system('sudo apt-get install whois')
    print(f'{Plus}{G} Uninstalling CRUNCH ...{W}')
    os.system('sudo apt purge install crunch')
    INPUT = input(f'{Danger} Would you like to uninstall XTERM? [Y/N] ')
    if INPUT == 'Y' or INPUT == 'y':
        print(f'{Plus}{G} Uninstalling XTERM ...{W}')
        os.system('sudo apt purge install xterm')
    print(f'{Plus}{G} Uninstalling DRIFTNET ...{W}')
    os.system('sudo apt purge install driftnet')
    print(f'{Plus}{G} Uninstalling DRIFTNET ...{W}')
    os.system('sudo apt purge install dsniff')
    print(f'{Plus}{G} Uninstalling OPENCL ...{W}')
    os.system('sudo apt purge install ocl-icd-opencl-dev')
    print(f'{Plus}{G} Uninstalling UNRAR ...{W}')
    os.system('sudo apt purge install unrar')
    INPUT = input(f'{Danger} Would you like to uninstall RUBY? [Y/N] ')
    if INPUT == 'Y' or INPUT == 'y':
        print(f'{Plus}{G} Uninstalling RUBY ...{W}')
        os.system('sudo apt-get purge ruby')
    print(f'{Plus}{G} Installing UPDATE ...{W}')
    os.system('sudo apt-get update')
    print(f'{C}UNINSTALL FINISHED YOU CAN NOW DELEAT CODEX')
