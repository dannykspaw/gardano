import RPi.GPIO as GPIO
from gpiozero import MCP3008
from datetime import datetime
import time
import csv


def motor_on(pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)

def motor_off(pin):

    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

def read_ai(chan):

    adc = MCP3008(channel=chan)
    output = adc.value
    voltage = round(3.3 * output, 1)
    return voltage

def vegetronix_moist(v):

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


if __name__ == '__main__':
    motor1 = 17
    motor2 = 18
    try:
        temp = (read_ai(0) * 75) - 40
        moisture = vegetronix_moist(read_ai(3))
        print(temp)
        print(moisture)

        time_on = int(input("Enter desired pump run time:\n"))
        motor_on(motor1)
        motor_on(motor2)
        time.sleep(time_on)
        motor_off(motor1)
        motor_off(motor2)
        
    except KeyboardInterrupt:
        print("\nProgram terminated as requested.")

    except Exception as e:
        print("\nAn unkown error occured at {}:{}. Program terminated.".format(datetime.now().hour, datetime.now().minute))
        print(e)

    finally:
        GPIO.cleanup()

