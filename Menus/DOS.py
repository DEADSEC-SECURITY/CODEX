#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *
#LOADS TOOLS
from tools.Interfaces import *
from tools.airodump import *

def Dos(interface):

    global DosOption

    #LOADS BSSID CHANNEL ESSID and ENCRYPTION
    from tools.airodump import bssid
    from tools.airodump import essid
    from tools.airodump import encrypt
    from tools.airodump import channel
    #LOADS MDK3 AIREPLAY and CONFUSION ATTACK
    from tools.DosAttacks import MDK3
    from tools.DosAttacks import Aireplay
    from tools.DosAttacks import Confusion

    process = subprocess.Popen(['iw', interface, 'info'], stdout=subprocess.PIPE)
    text = str(process.communicate()[0])
    begin = "ttype"
    end = "twiphy"
    CleanFile = text[text.find(begin):text.find(end)]
    mode = CleanFile[6:-3]

    OS()
    print()
    print(R + Banner)
    print(G + Dead)
    print(B + "************ Dos Attack Menu ************" + W)
    print("0) Exit script")
    print("1) Select another network interface")
    print("2) Put interface in monitor mode")
    print("3) Put interface in managed mode")
    print("4) Explore for targets [Monitor Mode Needed]")
    print(f"{C}----------{W}")
    print("5) Deauth mdk3 attack [Monitor Mode Needed]")
    print("6) Deauth aireplay attack [Monitor Mode Needed]")
    print("7) WIDS | WIPS | WDS Confusion attack [Monitor Mode Needed]")
    print("")
    print(f"{C}----------{W}")
    print(f"{W}Interface {O}{interface} {W}selected. Mode {O}{mode}{W}.")
    print(f"{C}----------{W}")
    print(f"Select ESSID:{O}{essid}{W}")
    print(f"Selected BSSID:{O}{bssid}{W}")
    print(f"Selected Channel:{O}{channel}{W}")
    print(f"Type of Encryption:{O}{encrypt}{W}")
    print(f"{C}----------{W}")
    print(f"{G}NOTE:{W} In case you cant change from monitor to managed restart you pc!")
    print(f"{C}----------{W}")
    DosOption = int(input())

    if DosOption == 0:
        return NET(interface)
    if DosOption == 1:
        return InterfaceSelect('Dos')
    if DosOption == 2:
        return monitor(interface, mode ,'Dos')
    if DosOption == 3:
        return managed(interface, mode, 'Dos')
    if DosOption == 4:
        if mode == "monitor":
            return Explorer(interface, 'Dos')
        if mode == "managed":
            print(f"{Danger} Please put your card in {O}monitor{W} mode before using this!")
            input(f"{Danger} Click {O}ENTER{W} to continue")
            return Dos(interface)
    if DosOption == 5:
        if mode == "monitor":
            logging.info("MDK3 Attack")
            return MDK3(interface)
        if mode == "managed":
            print(f"{Danger} Please put your card in monitor mode before using this!")
            input(f"{Danger} Click ENTER to continue")
            return Dos(interface)
    if DosOption == 6:
        if mode == "monitor":
            logging.info("Aireplay Attack")
            return Aireplay(interface)
        if mode == "managed":
            print(f"{Danger} Please put your card in monitor mode before using this!")
            input(f"{Danger} Click ENTER to continue")
            return Dos(interface)
    if DosOption == 7:
        if mode == "monitor":
            logging.info("Confusion Attack")
            return Confusion(interface)
        if mode == "managed":
            print(f"{Danger} Please put your card in monitor mode before using this!")
            input(f"{Danger} Click ENTER to continue")
            return Dos(interface)
    else:
        print(f"{Danger} Please only use numbers between 0 and 7")
        input(f"{Danger} Click ENTER to continue")
        return Dos()
