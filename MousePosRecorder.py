import os
os.system("pip install -r requirements.txt")
import pyautogui

# AUTHOR: Maria Babcock
# DATE: 3/26/2023
# REQUIREMENTS: 
#   1. None
# DIRECTIONS:
#   1. Open command prompt
#   2. Type in python FilePath\MousePosRecorder.py

os.system("pip install -r requirements.txt")

while True:
    x, y = pyautogui.position()
    
    print("x: " + str(x) + ", y: " + str(y))