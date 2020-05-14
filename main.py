import psutil
import wmi

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
