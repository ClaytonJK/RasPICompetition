
import os
import time
'''import board
import busio'''''
import digitalio
#import adafruit_lis3dh


print("Starting Program")
####Variables
setupCounter = 0
x = 1
y = 2
z = 3

####Test Board Connection
'''i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
if lis3dh.shake()==True:
    print("Shaken")
else:
    print("Stirred")'''



setup = input("Ready for Setup? y/n")
if setup[0] == "y":
    print("Perform Gesture Now")
    empty = open("accelSetup.txt", "w")
    empty.write("")
    while setupCounter < 50:
        print("Working!")
        ''' x,y,z = lis3dh.acceleration
        print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))'''
        with open("accelSetup.txt" , "a") as writer:
            writer.write("Acceleration:" + "" + str(x) + "," + str(y) + "," + str(z) + "\n")
        time.sleep(.1)
        setupCounter = setupCounter+1
    if setupCounter == 50:
        os.close("accelSetup.txt")
        print("Setup Complete")
if setup[0] == "n":
    print("OK")
