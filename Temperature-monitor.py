import wmi
import subprocess
import time

def get_cpu_temperature():
    try:
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == "Temperature" and "cpu" in sensor.Name.lower():
                return float(sensor.Value)
        return 0  # temperature not found
    except:
        return 0  # error occurred

def get_gpu_temperature():
    try:
        output = subprocess.check_output("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader", universal_newlines=True)
        return float(output.strip())
    except:
        return 0  # temperature not found

def display_load_bar(temp, max_temp, unit, label):
    bar_length = 30
    filled_length = int(round(bar_length * (temp / max_temp)))
    empty_length = bar_length - filled_length
    fill = "█"
    empty = "░"
    load_bar = fill * filled_length + empty * empty_length
    print(f"{label} temperature: {temp:.2f}°{unit}  [{load_bar}]")
    if temp >= (175 if unit == "F" else 80):
        print(f"WARNING: {label} temperature exceeded safe range!")

while True:
    cpu_temp = get_cpu_temperature()
    gpu_temp = get_gpu_temperature()

    display_load_bar(cpu_temp, 100, "C", "CPU")
    display_load_bar(cpu_temp * 1.8 + 32, 212, "F", "CPU")
    display_load_bar(gpu_temp, 100, "C", "GPU")
    display_load_bar(gpu_temp * 1.8 + 32, 212, "F", "GPU")

    time.sleep(1)
