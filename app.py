import threading
import time
import subprocess

def run_script(script):
    subprocess.run(["python3", script])
    
if __name__ == "__main__":
    collarService = threading.Thread(target=run_script, args=("main.py",))
    # eventListener = threading.Thread(target=run_script, args=("eventListener.py",))
    collarService.start()
    
    
    collarService.join()