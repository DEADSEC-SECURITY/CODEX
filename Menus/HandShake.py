#-----------Welcome to DeAdSeC Python Codex----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *
#LOADS TOOLS
from tools.Interfaces import *
from tools.airodump import *

def HandShake(interface):

    global mode

    #LOADS BSSID CHANNEL ESSID and ENCRYPTION
    from tools.airodump import bssid
    from tools.airodump import essid
    from tools.airodump import encrypt
    from tools.airodump import channel

    process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
    text = str(process.communicate()[0])
    begin = "ttype"
    end = "twiphy"
    CleanFile = text[text.find(begin):text.find(end)]
    mode = CleanFile[6:-3]

    OS()
    print('OI')
