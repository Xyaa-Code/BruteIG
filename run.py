# coding:utf-8
#/usr/bin/python
import os,requests,time

P = '\x1b[1;97m'
M = '\x1b[1;91m'

try:
    xyaa_reg = requests.get("http://ip-api.com/json/").json()
    xyaa_xcc = xyaa_reg["country"]
    
except:
        xyaa_xcc = "Indonesia"
        
if __name__ == "__main__":
	if "Indonesia" == xyaa_xcc:
		os.system('git pull')
		__import__("run").makedirectory()
	else:
	     os.system("clear")
	     print(f"{P}[{M}!{P}] sorry, this script can only be used in Indonesia")
