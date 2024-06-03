import tkinter as tk
from tkinter import ttk
import time
import psutil
import csv
from datetime import datetime

def check_process(PID):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if PID.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def save_data(start_time, end_time, elapsed_time_sec):
    hours = elapsed_time_sec / 3600  
    with open('data_sheet.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([start_time, end_time, elapsed_time_sec, hours])

def update_interface():
    if check_process(PID):
        if not process_running[0]:
            status_label.config(text="Running")
            process_running[0] = True
            start_time[0] = datetime.now()
    else:
        if process_running[0]:
            end_time = datetime.now()
            elapsed_time_sec = (end_time - start_time[0]).total_seconds()
            status_label.config(text="Stopped")
            save_data(start_time[0], end_time, elapsed_time_sec)
            process_running[0] = False
            start_time[0] = None
    
    if process_running[0]:
        elapsed_time_seconds = (datetime.now() - start_time[0]).total_seconds()
        elapsed_time_hours = elapsed_time_seconds / 3600
        elapsed_time_seconds_label.config(text=f"Elapsed time (s): {elapsed_time_seconds:.2f}")
        elapsed_time_hours_label.config(text=f"Elapsed time (h): {elapsed_time_hours:.2f}")

    root.after(1000, update_interface)

if __name__ == "__main__":
    PID = "AfterFX.exe"
    process_running = [False]
    start_time = [None]

    root = tk.Tk()
    root.title("Process Monitoring")

    status_label = ttk.Label(root, text="Status: ")
    status_label.pack()

    elapsed_time_seconds_label = ttk.Label(root, text="Elapsed time (s): ")
    elapsed_time_seconds_label.pack()

    elapsed_time_hours_label = ttk.Label(root, text="Elapsed time (h): ")
    elapsed_time_hours_label.pack()

    update_interface()

    root.mainloop()
