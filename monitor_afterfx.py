import time
import psutil

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    process_name = "AfterFX.exe"
    while True:
        if is_process_running(process_name):
            print("Running")
            time.sleep(25)  # Prevents continuous printing
        time.sleep(1)
