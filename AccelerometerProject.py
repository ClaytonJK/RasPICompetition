

import os
import time
'''import board
import busio'''''
import digitalio
import usb.core
#import adafruit_lis3dh
import sys

#### Internal Variables
setupCounter = 0
gestureCounter = 0
checkList = []
check = 0
indexIncrement = 0
tolerance = 0

#### Acceleration Variables
x = 1
y = 2
z = 3
x1 = 4
y1 = 5
z1 = 6


print("Starting Program")
#####Searches for connected USB Devices. Used for determining if setup is possible (if there is a keyboard, mouse, etc connected to the pi)
devices = list(usb.core.find(find_all=True))
print(devices)

#### Test Board Connection
'''i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
if lis3dh.shake()==True:
    print("Shaken")
else:
    print("Stirred")'''

#### Set Up Passgesture and Tolerances
#### If there is a connected usb device (ie. pi is connected to a desktop)
if devices[0] != "":
    #### Requesting Setup
    setup = input("Ready for Setup? y/n")
    if setup[0] == "y":
        toleranceInput = input("What would you like the tolerance to be on your passgesture? Default is 2 ")
        tolerance = int(toleranceInput)
        print("Perform Gesture Now")
        #### Creates a new file containing the information about the passgesture key and writes the gesture to it
        empty = open("accelSetup.txt", "w")
        empty.write("")
        for setupCounter in range(50):
            print("Working!")
            ''' x,y,z = lis3dh.acceleration
            print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))'''
            with open("accelSetup.txt" , "a") as writer:
                writer.write(str(x)+ "\n")
                writer.write(str(y)+ "\n")
                writer.write(str(z)+ "\n")
            #### 50 checks with .1 sec in between gives a total of five seconds per passgesture and allows for actual changes in the acceleration
            time.sleep(.1)
        empty.close()
        print("Setup Complete")
    if setup[0] != "y":
        print("OK")

#### Checking the Passgesture
for gestureCounter in range(50):
    constants=open("accelSetup.txt","r")
    constantsList=constants.readlines()
    '''x1,y1,z1 = lis3dh.acceleration'''
    #### Checks each accelerometer value to see if it is within range of the constant value. Adds the boolean to a list of passes and fails
    if (abs(int(constantsList[indexIncrement]))+tolerance)>=x1 and (abs(int(constantsList[indexIncrement]))-tolerance)<=x1:
       checkList.append(True)
    else:
        checkList.append(False)
    indexIncrement = indexIncrement+1
    if (abs(int(constantsList[indexIncrement]))+tolerance)>=y1 and (abs(int(constantsList[indexIncrement]))-tolerance)<=y1:
       checkList.append(True)
    else:
        checkList.append(False)
    indexIncrement = indexIncrement+1
    if (abs(int(constantsList[indexIncrement]))+tolerance)>=z1 and (abs(int(constantsList[indexIncrement]))-tolerance)<=z1:
       checkList.append(True)
    else:
        checkList.append(False)
    indexIncrement = indexIncrement+1
#### 50  checks with .1 sec in between gives a total of five seconds per passgesture and allows for actual changes in the acceleration
    time.sleep(.1)
#### Adds up all of the boolean values. True = 1, False = 0
for test in checkList:
    check = check + int(test)
#### If at least half of the accelerations are within range, the unlocking occurs
if check>=75:
    print("Unlocking")
else:
    print("Try Again!")