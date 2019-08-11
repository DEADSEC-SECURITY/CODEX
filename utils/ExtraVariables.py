#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 2.2.4---#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import os
    import sys
except ImportError as error:
    print(C + Banner)
    print()
    print(f'{Danger} {R}ImportError: Missing modules or incorrect path! Please run{O} setup.py {R}first.')
    exit(f'{Danger} {R}Error: {O}{error}')

Banner = '''     __       ______   ______    _______   __________   ___     __
    |  |     /      | /  __  \  |       \ |   ____\  \ /  /    |  |
    |  |    |  ,----'|  |  |  | |  .--.  ||  |__   \  V  /     |  |
    |  |    |  |     |  |  |  | |  |  |  ||   __|   >   <      |  |
    |__|    |  `----.|  `--'  | |  '--'  ||  |____ /  .  \     |__|
    (__)     \______| \______/  |_______/ |_______/__/ \__\    (__) '''


Dead = f'''
              		By         : DeAdSeC
              		Version    : 2.2.4
              		GitHub     : CODEX
              		Discord    : dFD5HHa
              		'''
#DEFAULT SETTINGS [DONT CHANGE]
bssid = 'NONE'
channel = 'NONE'
essid = 'NONE'
encrypt = 'NONE'

#Tranceback
sys.tracebacklimit = 1     # 0 For OFF | 1 For ON

#OS to clean the screen
def OS():
    os.system('cls' if os.name == 'nt' else 'clear')
