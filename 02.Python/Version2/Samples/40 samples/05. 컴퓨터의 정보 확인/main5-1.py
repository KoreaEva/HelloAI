import psutil

cpu = psutil.cpu_freq()
print(cpu)

cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

memory = psutil.virtual_memory()
print(memory)

disk = psutil.disk_partitions()
print(disk)

net = psutil.net_io_counters()
print(net)
