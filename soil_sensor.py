import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw

# Setup the I2C bus and the Seesaw sensor
i2c = busio.I2C(board.SCL, board.SDA)
ss = Seesaw(i2c, addr=0x36)

# Repeat
while True:
    # Read the moisture level
    moisture = ss.moisture_read()
    temperature = ss.get_temp() * 1.8 + 32

    # Print the moisture level
    print("Moisture level:", moisture)
    
    # Print the moisture level
    print("Temperature level:", temperature)


