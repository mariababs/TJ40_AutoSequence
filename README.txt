 AUTHOR: Maria Babcock
 DATE: 4/13/2023
 PURPOSE:
    1. To run custom automated test sequences for Emrby-Riddle's TJ40 engine
 REQUIREMENTS: 
   1. TJ40 Monitor program must be full screen on Monitor 2 
      (middle) of Prop Lab PIXe computer and buttons must not be covered
   2. Make sure nothing is covering TJ40 engine control buttons
   3. Make sure engine is at idle before running because
      starting up is not included in this program 
   4. AutoSequence.xlsx needs to be in the the same folder as this script
   5. AutoSequence.xlsx should have three columns titled "Command", "Throttle (%)", 
      and "Duration (Seconds)"
   6. Check that mouse position coordinates of each button are correct using MousePosRecorder.py
   7. Make sure that TJ40 CAN-to-USB converter had been set up correctly and is receiving data
   8. Make sure engine is in CAN mode, not RC mode (Jeti box will still display data in this mode)
 DIRECTIONS:
   0. Make sure the requirement 6 was done
   1. Open command prompt
   2. Type in python FilePath\AutoSequence_monitor2.py
   3. Monitor engine stats on TJ40 Monitor program and LabVIEW while running

TO SET UP TJ40 CAN-to-USB CONVERTER:
   0. FOllow instructions in the pdf that is on the flash drive that in the converter box/came with the converter.
   1. Will have to run the BAFCAN program that should already be on desktop of proplab computer, but is also on the flash drive in case it is lost
   2. Select converter and choose TJ40 configutation
   3. On TJ40 monitor app select the right COM in the top right corner of the screen (probaby gonna be COM 9 but it is whatever matches the device in BafCan app. 
   4. Should see data start transmitting after that (top left corner), you will know if numbers appear on the bottom of the guages of the TJ40 monitor app too
   5. If data is not being received, check that CANH and CANL were wired to the correct pins (check pdf from flash drive for pin diagram)

