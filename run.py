## Terkontol kontol
## Aditya Putra Mahesa XD.
try:
    import os
    import sys
    import time
    import bs4
    import rich
    import requests
    import datetime
    import random
    from datetime import datetime
    from rich.panel import Panel
    from rich import print as prints
except ImportError as e:
    os.system("clear")
    exit(f"{e} belum terinstall")

## COLOR FOR RICH
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

## COLOR FOR RICH TABLE
J3 = "#FF8F00" # JINGGA
H3 = "#00FF00" # HIJAU
N3 = "#FF00FF" # PINK
B3 = "#00FFFF" # BIRU MUDA

## RANDOM COLOR
DIT = random.choice([B2,H2,K2,J2,A2,N2])
PK = random.choice([J3,H3,N3,B3])

class Maintenance:

    def __init__(self):
       self.LinkIGEH = "https://instagram.com/xyaa_codename"
       self.LinkEFBI  = "https://www.facebook.com/Aditya.putraXD991"
       self.AdtyaMain()
    
    def WaktuXC(self):
        now = datetime.now()
        hours = now.hour
        if 4 <= hours < 12:timenow = "selamat pagi"
        elif 12 <= hours < 15:timenow = "selamat siang"
        elif 15 <= hours < 18:timenow = "selamat petang"
        else:timenow = "selamat malam"
        return timenow

    def clearLayar(self):
        if 'win' in sys.platform:
           os.system('cls')
        else:
           os.system('clear')

    def Logo(self):
        prints(Panel(f"""
{M2} ⣠⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⣄   {DIT}___           _           _       _ _ {P2}              
{M2} ⣿⣿⣿⡿⠛⢉⡉⠛⢿⣤⣼⣿  {DIT}|_ _|_ __  ___| |_ __ _   / \   __| | |_ _   _  __ _ {P2}
{M2} ⣿⣿⡏⢠⣾⣿⣿⣷⡄⢹⣿⣿   {DIT}| || '_ \/ __| __/ _` | / _ \ / _` | __| | | |/ _` |{P2}
{P2} ⣿⣿⣇⠘⢿⣿⣿⡿⠃⣸⣿⣿   {DIT}| || | | \__ \ || (_| |/ ___ \ (_| | |_| |_| | (_| |{P2}
 {P2}⣿⣿⣿⣷⣤⣈⣁⣤⣾⣿⣿⣿  {DIT}|___|_| |_|___/\__\__,_/_/   \_\__,_|\__|\__, |\__,_|{P2}
 {P2}⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋                                           {DIT}|___/{P2}
\t\t     {K2} InstaAdtya {P2}|{H2} last version 1.6 """,width=80,padding=(0,4),style=f"{PK}"))
    
    def AdtyaMain(self):
        self.clearLayar()
        self.Logo()
        prints(Panel("[white]mohon maaf script ini sedang dalam proses maintenance",title="😊",width=80,padding=(0,11),style=f"{PK}"))
        time.sleep(2.100)
        self.clearLayar()
        self.Logo()
        prints(Panel("[white]harap tunggu sampai proses maintenance selesai",title="🤗",width=80,padding=(0,15),style=f"{PK}"))
        time.sleep(2.100)
        self.clearLayar()
        self.Logo()
        prints(Panel(f"[white][[hot_pink]1[white]]. hubungi admin via WhatsApp\n[[hot_pink]2[white]]. ikuti facebook admin\n[[hot_pink]3[white]]. exit ( [red]keluar[white] )",width=80,padding=(0,22),style=f"{PK}"))
        AdtyaIn = input(" # choose : ")
        if AdtyaIn in   ["1","01"]:self.laporan()
        elif AdtyaIn in ["2","02"]:self.ikuti()
        elif AdtyaIn in ["3","03"]:self.exit()
        else:print(" # input yang bener bro!");time.sleep(2);self.AdtyaMain()
        
    def laporan(self):
        try:
            open("/sdcard/AdtyaMT/adtyaMT.txt","w").write("mohon bersabar ya, script ini sedang dalam proses maintenance\nharap tunggu sampai proses maintenance selesai😘")
            prints(Panel("[white]keren!, anda akan di arahkan ke WhatsApp admin",title="😎",width=80,padding=(0,15),style=f"{PK}"))
            os.system("xdg-open https://wa.me/+16143244921?text=assalamualaikum+bang+kapan+proses+maintenance+selesai+?")
            time.sleep(0.5)
            self.AdtyaMain()
        except:pass
    
    def ikuti(self):
        try:
            open("/sdcard/AdtyaMT/adtyaFoll.txt","w").write("keren lu ngab udah follow facebook admin😎")
            prints(Panel("[white]keren!, anda akan di arahkan ke Facebook admin",title="😎",width=80,padding=(0,15),style=f"{PK}"))
            os.system("xdg-open https://www.facebook.com/Aditya.putraXD991")
            time.sleep(0.5)
            self.AdtyaMain()
        except:pass
    
    def exit(self):
        try:
            open("/sdcard/AdtyaMT/adtyaExit.txt","w").write("kamu berhasil keluar dengan sukses ngab")
            prints(Panel("[white]terima kasih sudah menyempatkan menggunakan script saya :)",title="😝",width=80,padding=(0,9),style=f"{PK}"))
            time.sleep(3)
            sys.exit()
        except:pass
        
if __name__=='__main__':
  os.system("clear")
  try:print(" # please wait...");time.sleep(3)
  except:pass
  os.system("clear")
  try:os.system("git pull")
  except:pass
  try:os.mkdir("/sdcard/AdtyaMT")
  except:pass
  try:Maintenance()
  except:pass
        
