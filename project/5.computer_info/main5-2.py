# 필요한 정보만 출력
import psutil

cpu = psutil.cpu_freq() # cpu 속도 출력
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f' cpu speed : {cpu_current_ghz}GHz')

cpu_core = psutil.cpu_count(logical=False) # cpu의 물리코어 수 출력
print(f' core : {cpu_core}')

memory = psutil.virtual_memory() # memory 정보 출력
memory_total = round(memory.total / 1024**3)
print(f' memory : {memory_total}GB')

disk = psutil.disk_partitions() # disk 정보 출력
for p in disk:
    print(p.mountpoint, p.fstype, end='  ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f' disk mount : {disk_total}GB')

net = psutil.net_io_counters() # 네트워크를 통해 보내고 받은 데이터량 출력
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f' send : {sent}MB   recv : {recv}MB')