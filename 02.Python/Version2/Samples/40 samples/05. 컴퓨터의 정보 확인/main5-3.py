import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'CPU사용량: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1)
    print( f'사용가능한 메모리: {memory_avail}GB' )

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2
    
    sent = round(curr_sent-prev_sent,1)
    recv = round(curr_recv-prev_recv,1)
    
    print(f'보내기: {sent}MB   받기: {recv}MB')
    
    prev_sent = curr_sent 
    prev_recv = curr_recv
