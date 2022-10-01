# OpenVPN Config Grabber
# by Mugi F.
# github.com/mugi789
# 2022-02-06
import requests
import base64
print("""\
    \033[35m    
    █▀█ █▀█ █▀▀ █▄░█ █░█ █▀█ █▄░█
    █▄█ █▀▀ ██▄ █░▀█ ▀▄▀ █▀▀ █░▀█

    █▀▀ █▀█ █▄░█ █▀▀ █ █▀▀   █▀▀ █▀█ ▄▀█ █▄▄ █▄▄ █▀▀ █▀█
    █▄▄ █▄█ █░▀█ █▀░ █ █▄█   █▄█ █▀▄ █▀█ █▄█ █▄█ ██▄ █▀▄\033[0m\n""")
print(" How many configuration files do you want? \033[33m*Max 99*\033[0m")
jumlah = int(input(" Enter Quantity : "))+1
url = "https://www.vpngate.net/api/iphone/"
get = requests.get(url)
print(" "+"\033[36m=\033[0m"*30)
count = 1
try:
    while (count < jumlah):
        ip = get.text.split('\n')[count+1].split(',')[1]
        negara = get.text.split('\n')[count+1].split(',')[6]
        decode = base64.b64decode(get.text.split(',,')[count].split('\n')[0])
        f = open(negara+"_"+ip+'.ovpn', 'wb')
        f.write(decode)
        f.close()
        print(" "+negara+"_"+ip+'.ovpn')
        count = count + 1
    print(" "+"\033[36m=\033[0m"*30)
    print(" Done")
except IndexError:
    print(" "+"\033[36m=\033[0m"*30)