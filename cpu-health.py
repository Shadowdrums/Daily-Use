import psutil
import time
import subprocess
import datetime

def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(percpu=True)
    return cpu_percent

def print_load_bar(percent, core_num):
    fill = "█" * int(percent / 10)
    empty = "░" * (10 - int(percent / 10))
    return f"Core {core_num}: [{fill}{empty}] {percent}%"

def monitor_cpu_health():
    while True:
        cpu_percent = get_cpu_percent()
        for i, percent in enumerate(cpu_percent):
            cpu_bar = print_load_bar(percent, i)
            print(cpu_bar)
        time.sleep(1)

if __name__ == '__main__':
    monitor_cpu_health()
