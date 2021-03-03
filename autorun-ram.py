import psutil
import wmi
import os
import smtplib
import socket
from datetime import datetime
from time import sleep

while True:

#Zeit Definieren
  now = datetime.now()
  year = now.strftime("%Y")
  month = now.strftime("%m")
  day = now.strftime("%d")
  time = now.strftime("%H:%M:%S")
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  date_time_log = now.strftime("%m-%d-%Y-%H-%M-%S")

#RAM Auslesen
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
  sleep(5)
