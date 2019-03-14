#LOADS UTILS
from utils.ExtraVariables import *
from utils.colors import *
from utils.logs import *
from utils.Verify import *

def WEB():

    global OptionWeb

    from codex import StartMenu

    OS()
    print()
    print(R + Banner)
    print(G + Dead)
    print(f"{B}************ Web Attack Menu ************{W}")
    print("0) Exit script")
    print("1) Full Website Check")
    print("2) SQL Injection")
    OptionWeb = int(input())

    if OptionWeb == 0:
        return StartMenu()
    if OptionWeb == 1:
        logging.info("FULL Website Attack")
        pass
    if OptionWeb == 2:
        logging.info("SQL Attack")
        pass
