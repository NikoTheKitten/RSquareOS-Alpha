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
import psutil

os.system('cls')

biosscreen=("""
╔═══╦═══╦══╗╔══╦═══╦═══╗
║╔═╗║╔═╗║╔╗║╚╣╠╣╔═╗║╔═╗║
║╚═╝║╚══╣╚╝╚╗║║║║─║║╚══╗
║╔╗╔╩══╗║╔═╗║║║║║─║╠══╗║
║║║╚╣╚═╝║╚═╝╠╣╠╣╚═╝║╚═╝║
╚╝╚═╩═══╩═══╩══╩═══╩═══╝""")
 
print(biosscreen)

print("")
print("")
print("")

print("""
▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▒█▀▀▀█  ░█▀▀█ ▒█░░░ ▒█▀▀█ ▒█░▒█ ░█▀▀█  ▒█░░▒█ ▄█░ 
▒█▀▀▄ ▒█░ ▒█░░▒█ ░▀▀▀▄▄  ▒█▄▄█ ▒█░░░ ▒█▄▄█ ▒█▀▀█ ▒█▄▄█  ░▒█▒█░ ░█░ 
▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▒█▄▄▄█  ▒█░▒█ ▒█▄▄█ ▒█░░░ ▒█░▒█ ▒█░▒█  ░░▀▄▀░ ▄█▄""")

print("")
print("")
print("")

print("BIOS Mode")

print("")
print("")
print("")

def display_usage(cpu_usage, mem_usage, bars=50):
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' *int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rMem Usage:  |{mem_bar}| {mem_usage:.2f}%  ", end="\r")

while True:
    display_usage(psutil.virtual_memory().percent,30)
    time.sleep(0.5)