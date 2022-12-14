# Accelerometer file to record movement. Run in seperate thread?

import time
import level

# Import the ADXL345 module.
import Adafruit_ADXL345


# Create ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()


# These comments are from an example script
# You can ignore them for now

        # Alternatively you can specify the device address and I2C bus with parameters:
        #accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

        # You can optionally change the range to one of:
        #  - ADXL345_RANGE_2_G   = +/-2G (default)
        #  - ADXL345_RANGE_4_G   = +/-4G
        #  - ADXL345_RANGE_8_G   = +/-8G
        #  - ADXL345_RANGE_16_G  = +/-16G
        # For example to set to +/- 16G:
        #accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_16_G)

        # Or change the data rate to one of:
        #  - ADXL345_DATARATE_0_10_HZ = 0.1 hz
        #  - ADXL345_DATARATE_0_20_HZ = 0.2 hz
        #  - ADXL345_DATARATE_0_39_HZ = 0.39 hz
        #  - ADXL345_DATARATE_0_78_HZ = 0.78 hz
        #  - ADXL345_DATARATE_1_56_HZ = 1.56 hz
        #  - ADXL345_DATARATE_3_13_HZ = 3.13 hz
        #  - ADXL345_DATARATE_6_25HZ  = 6.25 hz
        #  - ADXL345_DATARATE_12_5_HZ = 12.5 hz
        #  - ADXL345_DATARATE_25_HZ   = 25 hz
        #  - ADXL345_DATARATE_50_HZ   = 50 hz
        #  - ADXL345_DATARATE_100_HZ  = 100 hz (default)
        #  - ADXL345_DATARATE_200_HZ  = 200 hz
        #  - ADXL345_DATARATE_400_HZ  = 400 hz
        #  - ADXL345_DATARATE_800_HZ  = 800 hz
        #  - ADXL345_DATARATE_1600_HZ = 1600 hz
        #  - ADXL345_DATARATE_3200_HZ = 3200 hz
        # For example to set to 6.25 hz:
        #accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_6_25HZ)

print('Operating')
# Find base ref values
base_x, base_y, base_z = accel.read()

base_x = abs(base_x)
base_y = abs(base_y)
base_z = abs(base_z)

# max amount to specify true change in movement
max_dif = 5

# incremented in loop to check trigger for gainExp()
brink = 0

while True:

    # Read x, y, z values
    x, y, z = accel.read()
    x = abs(x)
    y = abs(y)
    z = abs(z)

    # If x, y, or z are greater than 0 call leveling

    print('X={0}, Y={1}, Z={2}'.format(x, y, z))

    if (base_x - x) > max_dif:
        print("x moving")
        brink += 1

    if (base_y - y) > max_dif:
        print("y moving")
        brink += 1

    if (base_z - z) > max_dif:
        print("z moving")
        brink += 1

    if brink > 1:
        level.gainExp()

    # Set these values as new base for next iteration

    base_x = x
    base_y = y
    base_z = z

    # Set brink back to zero

    brink = 0

    # Wait 0.5 seconds and repeat.
    time.sleep(0.5)