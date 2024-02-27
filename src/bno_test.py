import pyb
import utime
import struct

i2c1 = pyb.I2C (1, pyb.I2C.CONTROLLER, baudrate = 100000) # Initialize the I2C comms
utime.sleep(1)

i2c1.mem_write ('\x1C', 0x28, 0x3D) # Writes byte to set the OPR_MODE to NDOF
utime.sleep(1)
i2c1.mem_write ('\x80', 0x28, 0x3B) # Writes byte to set the UNIT_SEL to deg

while True:
    
    buffy = bytearray(6)                 # create byte array of size 6
    i2c1.mem_read (buffy, 0x28, 0x1A)    # read the Euler angles starting at register 1A
    
    a,b,c = struct.unpack('<hhh',buffy)  # unpack the byte array data into 3 decimal values
    
    a = a/1435*90 # convert the values to degrees (conversion factor determined experimentally)
    b = b/1435*90 # convert
    c = c/1435*90 # convert
    
    print(f'{a},{b},{c}') # print Euler angles (x,y,z)
    utime.sleep(1)
