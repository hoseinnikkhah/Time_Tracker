import tkinter as tk
from tkinter import ttk
import time
import psutil
import csv
from datetime import datetime

def is_process_running(PID):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if PID.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def write_to_csv(start, end, elapsed_time_s):
    hours = elapsed_time_s / 3600  
    with open('time_sheet.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([start, end, elapsed_time_s, hours])

def update_gui():
    if is_process_running(PID):
        if not running_p[0]:
            status_label.config(text="Running")
            running_p[0] = True
            start[0] = datetime.now()
    else:
        if running_p[0]:
            end = datetime.now()
            elapsed_time_s = (end - start[0]).total_seconds()
            status_label.config(text="Stopped")
            write_to_csv(start[0], end, elapsed_time_s)
            running_p[0] = False
            start[0] = None
    
    # Update GUI with elapsed time
    if running_p[0]:
        elapsed_time_seconds = (datetime.now() - start[0]).total_seconds()
        elapsed_time_hours = elapsed_time_seconds / 3600
        elapsed_time_seconds_label.config(text=f"Elapsed time (s): {elapsed_time_seconds:.2f}")
        elapsed_time_hours_label.config(text=f"Elapsed time (h): {elapsed_time_hours:.2f}")

    root.after(1000, update_gui)

if __name__ == "__main__":
    PID = "AfterFX.exe"
    running_p = [False]  # Using a list to make it mutable
    start = [None]  # Using a list to make it mutable

    # GUI Setup
    root = tk.Tk()
    root.title("Process Monitor")

    status_label = ttk.Label(root, text="Status: ")
    status_label.pack()

    elapsed_time_seconds_label = ttk.Label(root, text="Elapsed time (s): ")
    elapsed_time_seconds_label.pack()

    elapsed_time_hours_label = ttk.Label(root, text="Elapsed time (h): ")
    elapsed_time_hours_label.pack()

    update_gui()

    root.mainloop()
