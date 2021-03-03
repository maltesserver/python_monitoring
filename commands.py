import psutil
import wmi
import os
import smtplib
import socket
from commands import *
from datetime import datetime

#Zeit Definieren

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
date_time_log = now.strftime("%m-%d-%Y-%H-%M-%S")

#RAM Auslesen
def ram():
  print("")
  print("")
  print("")
  print("Ram: " + str(psutil.virtual_memory()[2]) + "%")
  datei = open('logs/log-' + date_time_log + '.txt', 'w')
  datei.write("Datum und Zeit: " + date_time + "\nRAM-Usage: " + str(psutil.virtual_memory()[2]) + "%")
  datei.close()
  if (psutil.virtual_memory()[2] > 95):
    print("RAM Warnung!!!")
    print(str(psutil.virtual_memory()[2]) + "%")
  elif (psutil.virtual_memory()[2] > 100):
    print("RAM Warnung!!!")
    print(str(psutil.virtual_memory()[2]) + "%")
    print("Der RAM ist voll")
  return

#Ping Check

def ping():
  print("")
  print("")
  print("")
  hostname = "googlesaed.com"
  response = os.system("ping -c 1 " + hostname)

  if response == 0:
    print(hostname, "ist verfügbar!")
  else:
    print(hostname, "ist down!")
    return

#Help

def help():
  print("")
  print("")
  print("")
  print("-h   -> Zeigt die Commands an")
  print("-i   -> Zeigt die Infoseite an")
  print("-p  -> Starte einen Pingtest")
  print("-r   -> Starte den RAM Test")
  print("-ra   -> Starte den RAM Test jede 5 Sekunden")
  return

def info():
  print("")
  print("")
  print("")
  print("Code von: Malte und Felix")
  print("GitLab Link: https://gitlab.com/maltesserver/python_monitoring")
  return
