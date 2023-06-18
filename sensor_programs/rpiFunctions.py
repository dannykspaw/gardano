"""
Author(s): 
    Russell Hedrick; hedrickrussell@gmail.com
Date of Last Revision:  
    06/17/2023
Description:
    This program provides various IO functions to be able to easily
    interface with the raspberry pi. 
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                              Imports
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import RPi.GPIO as GPIO
from gpiozero import MCP3008
from datetime import datetime
import time
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ai_read(chan):

    adc = MCP3008(channel=chan)
    output = adc.value
    voltage = round(3.3 * output, 1)
    return voltage

def vegetronix_temp(channel):

    try:
        v = ai_read(channel)
        temp = (v * 75) - 40
        return temp
    except Exception as e:
        print("Failed to read from vegetronix temp. sensor.")
        return None

def vegetronix_moist(channel):
    
    try:
        v = ai_read(channel)
        if v <= 1.1:
            vwc = 10*v - 1
        elif v > 1.1 and v <= 1.3:
            vwc = 25*v - 17.5
        elif v > 1.3 and v <= 1.82:
            vwc = 48.08*v - 47.5
        elif v > 1.82 and v <= 2.2:
            vwc = 26.32*v - 7.89
        else:
            vwc = 62.5*v - 87.5
        return round(vwc, 1)

    except Exception as e:
        print("Failed to read from vegetronix moisture sensor.")
        return None

def pump_control(pin, time_on):

    try:
        # Turn pump on by closing 5V relay. 3.3V signal sent to specified pin
        pump_on = True
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(time_on)
        # Turn pump off and cleanup channels
        GPIO.output(pin, GPIO.HIGH)
        GPIO.cleanup()
        pump_on = False
    except Exception as e: 
        print(f"Failure activating pump on pin: {pin}")
    finally:
        if pump_on: GPIO.cleanup()



if __name__ == "__main__":
    
    print(f"""
    Temperature: {vegetronix_temp(0)}
    Moisture:   {vegetronix_moist(3)}
    """)
