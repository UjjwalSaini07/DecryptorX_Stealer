import subprocess, os , time 
from colorama import Fore as f
from colorama import init
init()
print(f.LIGHTCYAN_EX + "")
print(" __          ___ ______ _ _____           __      ___                 ")
print(" \ \        / (_)  ____(_)  __ \          \ \    / (_)                ")
print("  \ \  /\  / / _| |__   _| |__) |_ _ ___ __\ \  / / _  _____      __  ")
print("   \ \/  \/ / | |  __| | |  ___/ _` / __/ __\ \/ / | |/ _ \ \ /\ / /  ")
print("    \  /\  /  | | |    | | |  | (_| \__ \__ \\   /  | |  __/\ V  V /   ")
print("     \/  \/   |_|_|    |_|_|   \__,_|___/___/ \/   |_|\___| \_/\_/    \n")
print(f.LIGHTWHITE_EX + "\n  [+] Made by GH0STH4CK3R  [+] \n")

#print(f.LIGHTGREEN_EX + "") #LightGreen Console colour
#Current User Profile
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n') #Getiing Wifi Profiles
profiles = [i.split(":")[1][1:-1] for i in data if "Current User Profile" in i]   # Splitting Output

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]  # Getting Key Content

    auth = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    auth = [c.split(":")[1][1:-1] for c in auth if "Authentication" in c]    # Getting Authentication
    
    cipher = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    cipher = [d.split(":")[1][1:-1] for d in cipher if "Cipher" in d] # Getting Encryption
    
    ssid = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    ssid = [e.split(":")[1][1:-1] for e in ssid if "SSID name" in e] # Getting Ssid

    try: #Printing Details
        print(f.GREEN + "+----------------+-------------------+------------------+---------------+----------------+")
        print(f.LIGHTGREEN_EX + "|  Name          |  SSID             |  Authentication  |  Encryption   |  Password      |")
        print(f.GREEN + "+----------------+-------------------+------------------+---------------+----------------+")
        print(f.LIGHTYELLOW_EX + "")
        print ("{:>0}|  {:<}".format("",i),end="")
        print ("{:>4}| {:<}".format("",ssid[0]),end="")
        print ("{:>6}| {:<}".format("",auth[0]),end="")
        print ("{:>4}| {:<}".format("",cipher[0]),end="")
        print ("{:>10}| {:<}".format("",results[0]))
        #print(f.LIGHTGREEN_EX + "")
    except IndexError:
        print ("{:<15}:    {:<}".format(i, "Error"))
time.sleep(1)

#All User Profile
data2 = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles2 = [i.split(":")[1][1:-1] for i in data2 if "All User Profile" in i]

for i in profiles2:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [x.split(":")[1][1:-1] for x in results if "Key Content" in x]

    auth = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    auth = [y.split(":")[1][1:-1] for y in auth if "Authentication" in y]
    
    cipher = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    cipher = [z.split(":")[1][1:-1] for z in cipher if "Cipher" in z]

    ssid2 = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    ssid2 = [w.split(":")[1][1:-1] for w in ssid2 if "SSID name" in w] 


    try:
        print("")
        print(f.GREEN + "\n+----------------+-------------------+------------------+---------------+----------------+")
        print(f.LIGHTGREEN_EX + "|  Name          |  SSID             |  Authentication  |  Encryption   |  Password      |")
        print(f.GREEN + "+----------------+-------------------+------------------+---------------+----------------+")
        print(f.LIGHTYELLOW_EX + "")
        print ("{:>0}|  {:<}".format("",i),end="")
        print ("{:>4}| {:<}".format("",ssid2[0]),end="")
        print ("{:>6}| {:<}".format("",auth[0]),end="")
        print ("{:>4}| {:<}".format("",cipher[0]),end="")
        print ("{:>10}| {:<}".format("",results[0]))
        print(f.LIGHTGREEN_EX + "")
    except IndexError:
        print ("{:<15}:    {:<}".format(i, "Error"))
       
input("\nExit >")
