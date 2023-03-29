
from requests import get
from colorama import init, Fore

init()

user = input('the Enetr url > ')

with open('word.txt', 'r')as open:
    mylist = open.read().strip().split('\n')

for x in mylist:
    link = 'https://' + user + '/' + x
    rec = get(link)
    if rec.status_code == 200:
        print(Fore.CYAN+f'is fonud url {Fore.LIGHTRED_EX}', link)
    elif rec.status_code == 401:
        print(Fore.LIGHTCYAN_EX +
              f'is fonud url maskok bod [ 401 ] {Fore.RED}', link)
    elif rec.status_code == 403:
        print(Fore.LIGHTCYAN_EX +
              f'is fonud url maskok bod  [ 402 ] {Fore.RED}', link)
    else:
        print(Fore.RED+'[-]'+Fore.WHITE+' NotFound url', flush=True)
