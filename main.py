import psutil
cpu = psutil.cpu_percent()
vram = psutil.virtual_memory()
dvram = dict(psutil.virtual_memory()._asdict())

print(cpu)
print(vram)
print(dvram)