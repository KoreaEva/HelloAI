import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu속도: {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어: {cpu_core} 개"  )

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print( f'메모리: {memory_total}GB' )

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f'디스크크기: {disk_total}GB' )

net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f'보내기: {sent}MB   받기: {recv}MB')