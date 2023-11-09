import os
import time
import requests
import re  
import getpass
import subprocess
import platform
import sys
import csv
import shutil
from datetime import datetime
#import pynexos as python os

def napos():
    exit=1
    oldscreen=""" 
    ██████╗░░██████╗░██████╗░██╗░░░██╗░█████╗░██████╗░███████╗  ░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝
    ██████╔╝╚█████╗░██║██╗██║██║░░░██║███████║██████╔╝█████╗░░  ██║░░██║╚█████╗░
    ██╔══██╗░╚═══██╗╚██████╔╝██║░░░██║██╔══██║██╔══██╗██╔══╝░░  ██║░░██║░╚═══██╗
    ██║░░██║██████╔╝░╚═██╔═╝░╚██████╔╝██║░░██║██║░░██║███████╗  ╚█████╔╝██████╔╝
    ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═════╝░"""
    os.system('cls')
    print(oldscreen)
    print("")
    while exit!=0:
        y=input("$")
        if y=='shutdown':
            os.system('cls')
            print("[+] Instances Safely Shutting Down")
            time.sleep(2.69)
            print("[+] Shutting Down")
            time.sleep(1.7)
            os.system('cls')
            exit=0
        elif y=="restart":
            os.system('cls')
            print("[+]Restarting")
            time.sleep(0.8)
            print("[+]Saving Files")
            time.sleep(0.5)
            print("[+]Instances Safely Restarting")
            time.sleep(0.3)
            print("[+]Loading Files")
            time.sleep(0.9)
            print("[+]Loading Instances")
            os.system('cls')
            print(oldscreen)
        elif y=="cls":
            os.system('cls')
            print(oldscreen)
        elif y=="version --list":
            print("RSquare OS Alpha")
        elif y=="adminterminal --start":
            wipasswd=input("Password: ")
            while wipasswd!=passwd:
                print("Wrong Password")
                wipasswd=input("Password: ")
            os.system('cls')
            adminterminalnoactivate()
        elif y=="help":
            print("shutdown - Shutdowns The System")
            print("restart - Restarts The System")
            print("version --list - Lists The Current version Of The Os")
            print("cls - Clears the screen")
            print("adminterminal --start - Start Admin Terminal Which Has No Password Prompts")
        elif y=="":
            continue    
        else:
            print("Command Not Found")

def adminterminalnoactivate():

    exit=1
    noadminscreen=""" 
    ░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
    ██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
    ███████║██║░░██║██╔████╔██║██║██╔██╗██║  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
    ██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
    ██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
    ╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝"""

    print(noadminscreen)
    print("")
    while exit!=0:
        y=input("$")
        if y=='shutdown':
            os.system('cls')
            print("[+] Instances Safely Shutting Down")
            time.sleep(2.69)
            print("[+] Shutting Down")
            time.sleep(1.7)
            os.system('cls')
            exit=0
        elif y=="restart":
            os.system('cls')
            print("[+]Restarting")
            time.sleep(0.8)
            print("[+]Saving Files")
            time.sleep(0.5)
            print("[+]Instances Safely Restarting")
            time.sleep(0.3)
            print("[+]Loading Files")
            time.sleep(0.9)
            print("[+]Loading Instances")
            os.system('cls')
            print(noadminscreen)
        elif y=="cls":
            os.system('cls')
            print(noadminscreen)
        elif y=="version --list":
            print("RSquare OS ALPHA V1")
        elif y=="adminterminal --exit":
            os.system('cls')
            napos()
        elif y=="help":
            print("shutdown - Shutdowns The System")
            print("restart - Restarts The System")
            print("version --list - Lists The Current version Of The Os")
            print("cls - Clears the screen")
            print("adminterminal --start - Start Admin Terminal Which Has No Password Prompts") 
        elif y=="":
            continue    
        else:
            print("Command Not Found")

def download():
        os.system('cls')
        downloading=("""
        █████████████████████████████████████████████████████████████████████▀█
        █▄─▄▄▀█─▄▄─█▄─█▀▀▀█─▄█▄─▀█▄─▄█▄─▄███─▄▄─██▀▄─██▄─▄▄▀█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
        ██─██─█─██─██─█─█─█─███─█▄▀─███─██▀█─██─██─▀─███─██─██─███─█▄▀─██─██▄─█
        ▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀""")
        print(downloading)
        print("")
        print("")
        print("Status")
        print("")
        print("")
        print("")
        print("[-] Fetching/Downloading Files")
        print("[-] Installing features")
        print("[-] Compiling and Finishing")
        time.sleep(12.00)
        os.system('cls')
        print(downloading)
        print("")
        print("")
        print("Status")
        print("")
        print("")
        print("")
        print("[+] Fetching/Downloading Files")
        print("[-] Installing features")
        print("[-] Compiling and Finishing")
        time.sleep(8.00)
        os.system('cls')
        print(downloading)
        print("")
        print("")
        print("Status")
        print("")
        print("")
        print("")
        print("[+] Fetching/Downloading Files")
        print("[+] Installing features")
        print("[-] Compiling and Finishing")
        time.sleep(9.00)
        os.system('cls')
        print(downloading)
        print("")
        print("")
        print("Status")
        print("")
        print("")
        print("")
        print("[+] Fetching/Downloading Files")
        print("[+] Installing features")
        print("[+] Compiling and Finishing")

def new_install():

    os.system('cls')
    print("""
    ████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███▄─▄▄─█▄─█─▄█▄─▀█▄─▄█▄─▄▄─█▄─▀─▄███─▄▄─█─▄▄▄▄█
    ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─████─▄▄▄██▄─▄███─█▄▀─███─▄█▀██▀─▀████─██─█▄▄▄▄─█
    ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄█▄▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀""")
    print("")
    print("")
    print("")
    print("NOTE : PLEASE READ THE README FILE BEFORE STARTING THE INSTALLATION")
    print("AGAIN I REPEAT")
    print("PLEASE READ THE README FILE BEFORE STARTING THE INSTALLATION")
    print("")
    print("")
    print("")
    continueupgrade=input("Do you want to install PyNex OS Y/N : ")
    if continueupgrade == "Yes" or continueupgrade=="y" or continueupgrade=='Y':
        print("[+] Starting Setup")
        time.sleep(0.4)
        os.system('cls')
        print("""
        █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▀█ █▀█ █▀█ █░█ █▀▀ ▀█▀   █▄▀ █▀▀ █▄█   ▀█▀ █▀█   ▄▀█ █▀▀ ▀█▀ █ █░█ ▄▀█ ▀█▀ █▀▀
        ██▄ █░▀█ ░█░ ██▄ █▀▄   █▀▀ █▀▄ █▄█ █▄█ █▄▄ ░█░   █░█ ██▄ ░█░   ░█░ █▄█   █▀█ █▄▄ ░█░ █ ▀▄▀ █▀█ ░█░ ██▄""")
        print("")
        print("")
        print("The product key looks like : 00000 : ")
        print("")
        print("")
        activationkey=input("Do you have a key :")
        if activationkey=='no' or activationkey=="N" or activationkey=="NO" or activationkey=="No" or activationkey=="nO":
            download()    
            fp=open("avc.txt","w")
            fp.writelines("11615")
            fp.close()
            os.system('cls')
            napos()
        else:
            os.system('cls')
            k=input("Please Enter Product Key Or Activation Key..:")
            os.system('cls')
            avc=open("avc.txt","w")
            avc.writelines(k)
            avc.close()
            download()

                




passdecryptor=open("password.txt","r")
passwd=passdecryptor.readline()
passdecryptor.close()

avc=open("avc.txt","r")
key=avc.readline()
avc.close()

if key == "0000":
    new_install()

elif key == "11615":
    os.system('cls')
    print("[+] Starting")
    time.sleep(1.3)
    print("[+]Loading Files")
    time.sleep(0.9)
    print("[+]Loading Instances")
    os.system('cls')
    wipasswd=input("Password: ")
    while wipasswd!=passwd:
        print("Wrong Password")
        wipasswd=input("Password: ")
    napos()
else:
    os.system('cls')
    print("INVALID KEY \n\n")
    print("BOOT FAILED")
