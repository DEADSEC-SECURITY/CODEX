import nmap
import os
import sys
import json
import logging

from utils.ExtraVariables import *

W = "\033[0m" # white (normal)
R = "\033[31m" # red
G = "\033[32m" # green
O = "\033[33m" # orange
B = "\033[34m" # blue
P = "\033[35m" # purple
C = "\033[36m" # cyan
GR = "\033[37m" # gray
D = "\033[2m" # dims current color. {W} resets.
Plus = f'{W}{D}[{W}{G}+{W}{D}]{W}'
Danger = f'{O}[{R}!{O}]{W}'
WTF = f'{W}[{C}?{W}]'
nm = nmap.PortScanner()

def Logs():

        logging.basicConfig(filename = 'Data/LOGS/LOG', level = logging.INFO,
                        format = '%(asctime)s:%(message)s')

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

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

        OS()

        #Will print the data colected

        print(f"{B}Colected data:")
        print(f"{C}--------------")
        print(f"{Plus} {G}Ip Status: {W}" + state)
        print(f"{Plus} {G}Port Range: {W}" + portrange)
        print(f"{Plus} {G}HostName: {W}" + host)
        print(f"{Plus} {G}Scanned Hosts: {W}" + scanned_hosts)
        print(f"{Plus} {G}Open TCP Ports: {W}" + All_TCP)
        print(f"{Plus} {G}Open UDP Ports: {W}" + All_UDP)
        print(f"{Plus} {G}Open SCTP Ports: {W}" + All_SCTP)
        print(f"{Plus} {G}Open IP Ports: {W}" + All_IP)

        #Will create logs of all commands ran

        logging.info("")
        logging.info("")
        logging.info("ALL DATA COLECTED FROM A FULL SCAN")
        logging.info("Colected data:")
        logging.info("--------------")
        logging.info("Ip Status: " + state)
        logging.info("Port Range: " + portrange)
        logging.info("HostName: " + host)
        logging.info("Scanned Hosts " + scanned_hosts)
        logging.info("Open TCP Ports: " + All_TCP)
        logging.info("Open UDP Ports: " + All_UDP)
        logging.info("Open SCTP Ports: " + All_SCTP)
        logging.info("Open IP Ports: " + All_IP)

        print()
        input("Press any key to continue! ")
        NMAPScan.menu()

    def TCPScan():

        NMAPScan.Scan()

        OS()

        #Will print the data colected!

        print(f"{B}Colected data:")
        print(f"{C}--------------")
        print(f"{Plus} {G}Ip Status: {W}" + state)
        print(f"{Plus} {G}Port Range: {W}" + portrange)
        print(f"{Plus} {G}HostName: {W}" + host)
        print(f"{Plus} {G}Scanned Hosts: {W}" + scanned_hosts)
        print(f"{Plus} {G}Open TCP Ports: {W}" + All_TCP)

        #Will log the data colected!

        logging.info("")
        logging.info("")
        logging.info("ALL DATA COLECTED FROM A TCP SCAN")
        logging.info("Colected data:")
        logging.info("--------------")
        logging.info("Ip Status: " + state)
        logging.info("Port Range: " + portrange)
        logging.info("HostName: " + host)
        logging.info("Scanned Hosts " + scanned_hosts)
        logging.info("Open TCP Ports: " + All_TCP)

        print()
        input("Press any key to continue! ")
        NMAPScan.menu()

    def UDPScan():

        NMAPScan.Scan()

        OS()

        #Will print all the info colected

        print(f"{B}Colected data:")
        print(f"{C}--------------")
        print(f"{Plus} {G}Ip Status: ", nm[defaultipaddr].state())
        print(f"{Plus} {G}Port Range: ", portrange)
        print(f"{Plus} {G}HostName: ", nm[defaultipaddr].hostname())
        print(f"{Plus} {G}Scanned Hosts: ", nm.all_hosts())
        print(f"{Plus} {G}Open UDP Ports: ", nm[defaultipaddr].all_udp())

        #Will create logs of all commands ran

        logging.info("")
        logging.info("")
        logging.info("ALL DATA COLECTED FROM A UDP SCAN")
        logging.info(f"{B}Colected data:")
        logging.info(f"{C}--------------")
        logging.info(f"{Plus} {G}Ip Status: " + state)
        logging.info(f"{Plus} {G}Port Range: " + portrange)
        logging.info(f"{Plus} {G}HostName: " + host)
        logging.info(f"{Plus} {G}Scanned Hosts " + scanned_hosts)
        logging.info(f"{Plus} {G}Open UDP Ports: " + All_UDP)

        print()
        input("Press any key to continue! ")
        NMAPScan.menu()

    def SpecificPort():

        NMAPScan.Scan()

        Has_TCP = str(nm[defaultipaddr].has_tcp(int(port)))
        Has_UPD = str(nm[defaultipaddr].has_udp(int(port)))
        Has_SCTP = str(nm[defaultipaddr].has_sctp(int(port)))

        OS()

        #Will print the info colected!

        print(f"{B}Colected data:")
        print(f"{C}--------------")
        print(f"{Plus} {G}Ip Status: {w}{state}")
        print(f"{Plus} {G}Selected Port: {W}{port}")
        print(f"{Plus} {G}HostName: {W}{host}")
        print(f"{Plus} {G}Scanned Hosts: {W}{scanned_hosts}")
        print(f"{Plus} {G}UDP OPEN: {W}{has_udp}")
        print(f"{Plus} {G}UDP OPEN: {W}{has_udp}")
        print(f"{Plus} {G}TCP OPEN: {W}{has_tcp}")
        print(f"{Plus} {G}SCTP OPEN: {W}{has_sctp}")

        #Will create logs of all commands ran!

        logging.info("")
        logging.info("")
        logging.info("ALL DATA COLECTED FROM A Specific Port SCAN")
        logging.info("Colected data:")
        logging.info("--------------")
        logging.info("Ip Status: " + state)
        logging.info("Port Range: " + portrange)
        logging.info("HostName: " + host)
        logging.info("Scanned Hosts " + scanned_hosts)
        logging.info("UDP OPEN: " + Has_UPD)
        logging.info("TCP OPEN: " + Has_TCP)
        logging.info("SCTP OPEN: " + Has_SCTP)

        print()
        input("Press any key to continue! ")
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

        Logs()

        with open('Data/DATA.json') as f:
            data = json.load(f)

        for DefaultInfo in data['DefaultInfo']:
            portrange = DefaultInfo['defaultportrange']
            defaultipaddr = DefaultInfo['defaultipaddress']

        OS()
        print()
        print(R + Banner)
        print(G + Dead + W)
        print(f"{B}************ NMAP Menu ************{W}")
        print("0) Exit Script")
        print("1) Full Network Scan")
        print("2) TCP Scan")
        print("3) UDP Scan")
        print("4) Scan for a specified port")
        print(f"{C}------------{W}")

        menuoption = int(input())

        if menuoption == 0:

            OS()
            return Menus.NET()

        if menuoption == 1:
            OS()
            print("Would you like to use the default ip? [" + defaultipaddr + "]")
            optionip = input()

            if optionip == "Y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                if optionport == "y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "N":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                if optionport == "y":

                    return  NMAPScan.FullNetworkScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.FullNetworkScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                if optionport == "y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "n":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                if optionport == "y":

                    return NMAPScan.FullNetworkScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.FullNetworkScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            else:
                print("Use only Y/N or y/n")
                return NMAPScan.menu()

        if menuoption == 2:

            OS()
            print("Would you like to use the default ip? [" + defaultipaddr + "]")
            optionip = input()

            if optionip == "Y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.TCPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                if optionport == "y":

                    return NMAPScan.TCPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.enu()

            if optionip == "N":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.TCPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                if optionport == "y":

                    return  NMAPScan.TCPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.TCPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                if optionport == "y":

                    return NMAPScan.TCPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "n":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.TCPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                if optionport == "y":

                    return NMAPScan.TCPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.TCPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            else:
                print("Use only Y/N or y/n")
                return NMAPScan.menu()

        if menuoption == 3:

            OS()
            print("Would you like to use the default ip? [" + defaultipaddr + "]")
            optionip = input()

            if optionip == "Y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.UDPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                if optionport == "y":

                    return NMAPScan.UDPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "N":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.UDPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                if optionport == "y":

                    return  NMAPScan.UDPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "y":

                OS()
                print("Would you like to use the default port range? [" + portrange + "]")
                optionport = input()

                if optionport == "Y":

                    nm.scan(ipaddr, portrange, '-v')

                    return NMAPScan.UDPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                if optionport == "y":

                    return NMAPScan.UDPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            if optionip == "n":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                OS()
                print("Would you like to use the default port range? [", portrange, "]")
                optionport = input()

                if optionport == "Y":

                    return NMAPScan.UDPScan()

                if optionport == "N":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                if optionport == "y":

                    return NMAPScan.UDPScan()

                if optionport == "n":

                    OS()
                    print("Please use this format for the port range: MinPort-MaxPort")
                    portrange = input("What port range would you want me to use: ")

                    return NMAPScan.UDPScan()

                else:
                    print("Please use only Y/N or y/n")
                    return NMAPScan.menu()

            else:
                print("Use only Y/N or y/n")
                return NMAPScan.menu()

        if menuoption == 4:
            OS()
            print("Would you like to use the default ip? [" + defaultipaddr + "]")
            optionip = input()

            OS()
            port = input("Please enter the port you wanna scan: ")

            if optionip == "Y":

                return  NMAPScan.SpecificPort()

            if optionip == "N":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                return NMAPScan.SpecificPort()

            if optionip == "y":

                return NMAPScan.SpecificPort()

            if optionip == "n":

                OS()
                defaultipaddr = input("Please enter your ip address: ")

                return NMAPScan.SpecificPort()