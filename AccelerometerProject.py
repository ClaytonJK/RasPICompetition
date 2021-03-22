import time
import board
import busio
import digitalio
import adafruit_lis3dh

print("Starting Program")

i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

if lis3dh.shake()==True:
    print("Shaken")
else:
    print("Stirred")