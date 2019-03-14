import datetime
import netifaces

Banner = """     __       ______   ______    _______   __________   ___     __
    |  |     /      | /  __  \  |       \ |   ____\  \ /  /    |  |
    |  |    |  ,----'|  |  |  | |  .--.  ||  |__   \  V  /     |  |
    |  |    |  |     |  |  |  | |  |  |  ||   __|   >   <      |  |
    |__|    |  `----.|  `--'  | |  '--'  ||  |____ /  .  \     |__|
    (__)     \______| \______/  |_______/ |_______/__/ \__\    (__) """


Dead = f"""
              		By         : DeAdSeC
              		Version    : 1.0.0
              		GitHub     : REP
              		Discord    : DISC
              		"""
                    
#Please dont change any of these variables!
NetworkInterfaces = netifaces.interfaces()
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M")

#DEFAULT SETTINGS [DONT CHANGE]
bssid = 'NONE'
channel = 'NONE'
essid = 'NONE'
encrypt = 'NONE'
