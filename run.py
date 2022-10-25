import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("run").cek_lisensi_aktif()
   except Exception as e:
       exit(str(e))
