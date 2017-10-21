import subprocess
import time 
block = subprocess.Popen('python3 keyboard_block.py')
time.sleep(2.5)
block.kill()
