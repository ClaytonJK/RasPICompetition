import time
import board
import busio
import digitalio
import adafruit_lis3dh
import pyudev

print("Starting Program")

context = pyudev.Context()
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

for device in context.list_devices():
    device
if lis3dh.shake()==True:
    print("Shaken")
else:
    print("Stirred")