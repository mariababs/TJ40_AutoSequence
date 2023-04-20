import os
# os.system("pip install -r requirements.txt")
import pyautogui
from time import sleep
import xlrd
import sys

# AUTHOR: Maria Babcock
# DATE: 4/13/2023
# REQUIREMENTS: 
#   1. TJ40 Monitor program must be full screen on Monitor 2 
#      (middle) of Prop Lab PIXe computer and button must not be covered.
#   2. Make sure nothing is covering TJ40 engine control buttons
#   3. Make sure engine is at idle before running because
#      starting up is not included in this program 
#   4. AutoSequence.xlsx needs to be in the the same folder as this script
#   5. AutoSequence.xlsx should have three columns titled "Command", "Throttle (%)", 
#      and "Duration (Seconds)"
#   6. Check that mouse position coordinates of each button are correct using MousePosRecorder.py
# DIRECTIONS:
#   1. Open command prompt
#   2. Type in python FilePath\AutoSequence_monitor2.py
#   3. Monitor engine stats on TJ40 Monitor program and LabVIEW while running

# INPUTS:
# Monitor 1 Coordinates
start_x = 47
start_y = 976
stop_x = 132
stop_y = 976
cool_x = 213
cool_y = 976
idle_x = 300
idle_y = 976
throttle_50_x = 386 
throttle_50_y = 976
throttle_60_x = 470
throttle_60_y = 976
throttle_70_x = 555
throttle_70_y = 976
throttle_80_x = 636
throttle_80_y = 976
throttle_90_x = 725
throttle_90_y = 976
throttle_100_x = 810
throttle_100_y = 976

# Get input string from command line argument
input_string = sys.argv[1]

# Give the location of the file 
loc = (input_string) 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# Skip the first row 
row = 1

# Get the number of columns
cols = sheet.ncols

# Create arrays for each column
arrays = []
for i in range(cols):
    arrays.append([])

# Iterate through each row and store values in each array
while(row < sheet.nrows):
    for i in range(cols):
        arrays[i].append(sheet.cell_value(row, i))
    row += 1

# print(arrays)

# Designate corresponding arrays
commandStr = arrays[0]
throttle = arrays[1]
delta_t = arrays[2]

# Get the length of each array
lengths = []
for array in arrays:
    lengths.append(len(array))

# Get the shortest array's length
min_length = min(lengths)

print("STARTING AUTO SEQUENCE")
print("Total Test Duration: "+str(sum(delta_t))+" seconds")

# Execute loop for each row
for i in range(min_length):
    # Print what command row will be executing
    print(commandStr[i]+":")

    # Error handeling for duration: Needs to be a positive number
    if delta_t[i] < 0 or type(delta_t[i]) != float:
        print("ERROR: Not a valid time duration. Must be a positive number.")
        continue
    
    # Error handeling for throttle command. Must be one of the TJ40 Monitor program buttons.
    throttleStr = str(throttle[i])
    if throttle[i] != 100 and throttle[i] != 90 and throttle[i] != 80 and throttle[i] != 70 and throttle[i] != 60 and throttle[i] != 50:
        if throttleStr.lower() != 'idle' and throttleStr.lower() != 'start' and throttleStr.lower() != 'stop' and throttleStr.lower() != 'cool':
            print("ERROR: Not a valid throttle command. See TJ40 Monitor screen for valid commands.")
            continue
    
    # Print command details
    print("\tThrottle: "+str(throttle[i])+" for "+str(delta_t[i])+" seconds...")

    # Click the appropriate throttle button
    if throttle[i] == 50:
        pyautogui.click(throttle_50_x,throttle_50_y)
    elif throttle[i] == 60:
        pyautogui.click(throttle_60_x,throttle_60_y)
    elif throttle[i] == 70:
        pyautogui.click(throttle_70_x,throttle_70_y)
    elif throttle[i] == 80:
        pyautogui.click(throttle_80_x,throttle_80_y)
    elif throttle[i] == 90:
        pyautogui.click(throttle_90_x,throttle_90_y)
    elif throttle[i] == 100:
        pyautogui.click(throttle_100_x,throttle_100_y)
    elif throttleStr.lower() == 'idle':
        pyautogui.click(idle_x,idle_y)
    elif throttleStr.lower() == 'stop':
        pyautogui.click(stop_x,stop_y)
    elif throttleStr.lower() == 'start':
        pyautogui.click(stop_x,stop_y)
    elif throttleStr.lower() == 'cool':
        pyautogui.click(cool_x,cool_y)
 
    # Wait/hold throttle setting for specified duration
    sleep(delta_t[i])

print("FINISHED AUTO SEQUENCE")

