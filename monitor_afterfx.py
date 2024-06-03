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
    was_running = False
    while True:
        if is_process_running(process_name):
            if not was_running:
                print("Running")
                was_running = True
            time.sleep(25)  # Prevents continuous printing
        else:
            if was_running:
                print("Stopped")
                was_running = False
        time.sleep(1)
