import json

from Menus.StartMenu import *
from codex import OS

def IP():
    OS()

    with open('Data/DATA.json') as f:
        data = json.load(f)

    newip = input("Please enter your new default ip address: ")
    data['DefaultInfo'][0]['defaultipaddress'] = defaultipaddr = newip
    with open('Data/DATA.json', 'w') as f:
        json.dump(data, f, indent = 2)

    OS()
    print("Default ip address changed to " + newip)

    logging.info("Port range changed to " + newip)
    return StartMenu()

def PortRange():
    OS()

    with open('Data/DATA.json') as f:
        data = json.load(f)

    newport = input("Please enter your new default port range: ")
    data['DefaultInfo'][0]['defaultportrange'] = portrange = newport
    with open('Data/DATA.json', 'w') as f:
        json.dump(data, f, indent = 2)

    OS()
    print("Default port range changed to " + newport)

    logging.info("Port range changed to " + newport)
    return Menus.StartMenu()

def Interface():

    with open('Data/DATA.json') as f:
        data = json.load(f)

    for DefaultInfo in data['DefaultInfo']:
        interface = DefaultInfo['defaultinterface']

    OS()
    print("********** Please select your default interface **********")
    print(*(W + '{}) {}'.format(x, y) for (x, y) in enumerate(NetworkInterfaces, 1)), sep='\n')
    print()
    print(W + "----------")
    print(R + "Note: Please write the interface the way it shows in the menu!")
    print(R + "Note: You can change the interface later if you need!")
    print(W + "----------")
    print(Y + "Contribution: We are looking for a way to make it so you dont need to write the hole interface name and only a number!")
    print(W + "----------")
    print()
    interface = input("Please write your new default interface: ")

    data['DefaultInfo'][0]['defaultinterface'] = defaultinterface = interface
    with open('Data/DATA.json', 'w') as f:
        json.dump(data, f, indent = 2)

    print("Interface changed to " + interface)

    return Menus.StartMenu()
