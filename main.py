import psutil
import wmi
import os
import smtplib
import socket
from commands import *

#Willkommensnachricht
while True:
    print ("")
    print ("")
    print ("")
    print ("Python Monitoring")
    print ("")
    print ("Commands:")
    print ("")
    print("-h   -> Zeigt die Commands an")
    print("-i   -> Zeigt die Infoseite an")
    print("-p  -> Starte einen Pingtest")
    print("-r   -> Starte den RAM Test")
    print("-ra   -> Starte den RAM Test jede 5 Sekunden")

# Commandsabfrage

    commands = input("Command: ")
    print
    if commands == "-h":
        help()
    elif commands == "-i":
        info()
    elif commands == "-p":
        ping()
    elif commands == "-r":
        ram()
    elif commands == "-ra":
        os.system("py autorun-ram.py")
sleep(1)