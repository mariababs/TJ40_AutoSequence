 AUTHOR: Maria Babcock
 DATE: 4/13/2023
 PURPOSE:
    1. To run custom automated test sequences for Emrby-Riddle's TJ40 engine
 REQUIREMENTS: 
   1. TJ40 Monitor program must be full screen on Monitor 2 
      (middle) of Prop Lab PIXe computer and button must not be covered
   2. Make sure nothing is covering TJ40 engine control buttons
   3. Make sure engine is at idle before running because
      starting up is not included in this program 
   4. AutoSequence.xlsx needs to be in the the same folder as this script
   5. AutoSequence.xlsx should have three columns titled "Command", "Throttle (%)", 
      and "Duration (Seconds)"
   6. Check that mouse position coordinates of each button are correct using MousePosRecorder.py
 DIRECTIONS:
   1. Open command prompt
   2. Type in python FilePath\FlightOperation_monitor2.py
   3. Monitor engine stats on TJ40 Monitor program and LabVIEW while running