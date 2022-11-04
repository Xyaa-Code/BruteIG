# My name ( Xyaa Code )
# my facebook ( https://www.facebook.com/Aditya.putraXD991 )
# whatsapp ( +1 (614) 324-4921 )

import os
try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import bs4
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Rich belum terinstall!...\n')
    os.system('pip install rich')

if __name__ == '__main__':
    try:
        os.system("git pull")
        __import__("run").buy_lisenn()
    except Exception as e:
        exit(str(e)) 
    
