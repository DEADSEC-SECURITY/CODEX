#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 2.1.3---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#IMPORT DEPENDENCYS
import os
#IMPORT UTILS
from utils.colors import *
from utils.ExtraVariables import *

if os.geteuid() == 0:
    print(C + Banner)
    print()
    exit(f'{Danger} {R}Error: Need to be run as {O}root\n{Danger} {R}Re-Run it but with {O} sudo {W}')
else:
    print('Starting Setup for CODEX ...')
    print(f'{Plus}{G} Installing TLD ...')
    os.system('sudo pip3 install tld')
    print(f'{Plus}{G} Installing SUBPROCESS')
    os.system('sudo pip3 install subprocess')
    print(f'{Plus}{G} Installing PANDAS ...')
    os.system('sudo pip3 install pandas')
    print(f'{Plus}{G} Installing NMAP ...')
    os.system('sudo pip3 install nmap')
    print(f'{Plus}{G} Installing NETIFACES ...')
    os.system('sudo pip3 install netifaces')
