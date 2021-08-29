import psutil
from datetime import datetime
import time
import os


def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


def get_processes_info():
    processes = []
    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            if pid == 0:
                continue

            name = process.name()
            try:
                create_time = datetime.fromtimestamp(process.create_time())
            except OSError:
                create_time = datetime.fromtimestamp(psutil.boot_time())
            try:
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = -1

            cpu_usage = process.cpu_percent()
            status = process.status()

            try:
                nice = int(process.nice())
            except psutil.AccessDenied:
                nice = 0
            try:
                memory_usage = process.memory_full_info().uss
            except psutil.AccessDenied:
                memory_usage = 0

            n_threads = process.num_threads()
            
        processes.append({
            'pid': pid, 'name': name, 'create_time': create_time,
            'cores': cores, 'cpu_usage': cpu_usage, 'status': status, 'priority': nice,
            'memory_usage': memory_usage,'n_threads': n_threads,
        })

    return processes

if __name__ == "__main__":
    live_update = True
    processes = get_processes_info()
    print(processes)
    while live_update:
        processes = get_processes_info()
        os.system("cls") if "nt" in os.name else os.system("clear")
        print(processes)
        time.sleep(0.7)