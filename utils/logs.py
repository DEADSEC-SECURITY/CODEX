import logging

def Logs():

    logging.basicConfig(filename = f'Data/LOGS/LOG-{date}', level = logging.INFO,
                    format = '%(asctime)s:%(message)s')
