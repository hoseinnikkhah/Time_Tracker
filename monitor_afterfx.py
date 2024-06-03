import time
import psutil
import csv
from datetime import datetime

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def write_to_csv(start_time, end_time, elapsed_time):
    elapsed_hours = elapsed_time / 3600  
    with open('time_sheet.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([start_time, end_time, elapsed_time, elapsed_hours])

if __name__ == "__main__":
    process_name = "AfterFX.exe"
    was_running = False
    start_time = None

    while True:
        if is_process_running(process_name):
            if not was_running:
                print("Running")
                was_running = True
                start_time = datetime.now()
            time.sleep(25)  # Prevents continuous printing
        else:
            if was_running:
                end_time = datetime.now()
                elapsed_time = (end_time - start_time).total_seconds()
                print(f"Stopped. Elapsed time: {elapsed_time} seconds")
                write_to_csv(start_time, end_time, elapsed_time)
                was_running = False
                start_time = None
        time.sleep(1)
