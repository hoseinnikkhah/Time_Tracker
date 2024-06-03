import tkinter as tk
from tkinter import ttk
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

def update_gui():
    if is_process_running(process_name):
        if not was_running[0]:
            status_label.config(text="Running")
            was_running[0] = True
            start_time[0] = datetime.now()
    else:
        if was_running[0]:
            end_time = datetime.now()
            elapsed_time = (end_time - start_time[0]).total_seconds()
            status_label.config(text="Stopped")
            write_to_csv(start_time[0], end_time, elapsed_time)
            was_running[0] = False
            start_time[0] = None
    
    # Update GUI with elapsed time
    if was_running[0]:
        elapsed_time_seconds = (datetime.now() - start_time[0]).total_seconds()
        elapsed_time_hours = elapsed_time_seconds / 3600
        elapsed_time_seconds_label.config(text=f"Elapsed time (s): {elapsed_time_seconds:.2f}")
        elapsed_time_hours_label.config(text=f"Elapsed time (h): {elapsed_time_hours:.2f}")

    root.after(1000, update_gui)

if __name__ == "__main__":
    process_name = "AfterFX.exe"
    was_running = [False]  # Using a list to make it mutable
    start_time = [None]  # Using a list to make it mutable

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
