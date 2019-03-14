import subprocess
import time
import os
import pandas

interface = 'wlp3s0mon'
ExplorePath = os.path.isfile('Data/AiroDumpOutPut/AiroDumpOutPut-01.csv')

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

if ExplorePath == True:
    os.remove('Data/AiroDumpOutPut/AiroDumpOutPut-01.csv')
    os.system(f"xterm -fg green -e sudo airodump-ng -w Data/AiroDumpOutPut/AiroDumpOutPut --output-format csv {interface}")

else:
    os.system(f"xterm -fg green -e sudo airodump-ng -w Data/AiroDumpOutPut/AiroDumpOutPut --output-format csv {interface}")

OS()
df = pandas.read_csv('Data/AiroDumpOutPut/AiroDumpOutPut-01.csv')
#df = df.drop(df.index[[4, 5]])
stop_row = df[df.BSSID == 'Station MAC'].index[0] -1
df = pandas.read_csv('Data/AiroDumpOutPut/AiroDumpOutPut-01.csv', nrows = stop_row)
df = df.drop(df.columns[[1, 2, 4, 6, 7, 9, 10, 11, 12, 14]], axis=1)
print(df)
print()
ColectedInput = input("Please enter the number of the network: ")
