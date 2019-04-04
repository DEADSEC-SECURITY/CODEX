import subprocess
import time
import os
import pandas
from tld import get_tld

main = get_tld('https://www.tmg.pt', as_object = True)
subdomain = main.subdomain
domain = main.domain
FLD = main.fld
print(f'This is the subdomain {subdomain}')
print(f'This is the domain {domain}')
print(f'This is fld {FLD}')
print(f'This is the tld {main}')

process = os.popen('whois ' + FLD)
process = str(process.read())
print(process)
