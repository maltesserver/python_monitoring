import psutil
import wmi
import os

cpu = psutil.cpu_percent()
vram = psutil.virtual_memory()

c = wmi.WMI()
print ("INFO")
systeminfo = c.Win32_ComputerSystem()[0]

Manufacturer = systeminfo.Manufacturer
Model = systeminfo.Model

print(systeminfo)
print(Manufacturer)
print(Model)


print ("CPU")
print(cpu)
print ("RAM")
print(vram)

print ("")
print ("[------Ping Test------]")
print ("")

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, "is up!")
else:
  print (hostname, "is down!")
