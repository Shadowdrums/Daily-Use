import psutil
import GPUtil
import time
import subprocess
import datetime

def get_meechy_darko_cpu():
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

def get_zombie_juice_memory():
    virtual_memory = psutil.virtual_memory()
    memory_percent = virtual_memory.percent
    return memory_percent

def get_akeem_gpu():
    gpus = GPUtil.getGPUs()
    gpu_percent = gpus[0].load * 100
    return gpu_percent

def get_erick_arc_elliott_disk():
    partitions = psutil.disk_partitions()
    disk_percentages = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_percentages.append(usage.percent)
    return disk_percentages

def print_load_bar(percent, color):
    fill = "█" * int(percent / 10)
    empty = "░" * (10 - int(percent / 10))
    return f"[{fill}{empty}] {percent}% ({color})"

def get_meechy_darko_net():
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    return bytes_sent, bytes_recv

def display_net_usage():
    bytes_sent1, bytes_recv1 = get_meechy_darko_net()
    time.sleep(1)
    bytes_sent2, bytes_recv2 = get_meechy_darko_net()
    sent_speed = (bytes_sent2 - bytes_sent1) / 1024 / 1024
    recv_speed = (bytes_recv2 - bytes_recv1) / 1024 / 1024
    net_usage = f"Network Usage: {sent_speed:.2f} Mbps sent\nNetwork Usage: {recv_speed:.2f} Mbps received"
    return net_usage

def display_system_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))
    system_uptime = f"System Uptime: {uptime_str}"
    return system_uptime

def monitor_pc_health():
    while True:
        cpu_percent = get_meechy_darko_cpu()
        memory_percent = get_zombie_juice_memory()
        gpu_percent = get_akeem_gpu()
        disk_percentages = get_erick_arc_elliott_disk()
        net_usage = display_net_usage()
        system_uptime = display_system_uptime()

        cpu_bar = print_load_bar(cpu_percent, "CPU")
        memory_bar = print_load_bar(memory_percent, "RAM")
        gpu_bar = print_load_bar(gpu_percent, "GPU")
        disk_bars = [print_load_bar(percent, f"DISK-{i}") for i, percent in enumerate(disk_percentages)]

        print(cpu_bar)
        print(memory_bar)
        print(gpu_bar)
        for disk_bar in disk_bars:
            print(disk_bar)
        print(net_usage)
        print(system_uptime)
        time.sleep(1)

if __name__ == '__main__':
    monitor_pc_health()
