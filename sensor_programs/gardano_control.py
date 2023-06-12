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

def read_ai(channel):

    adc = MCP3008(channel=channel, device=0)
    return adc.value

if __name__ == '__main__':
    motor1 = 17
    motor2 = 18
    try:
        time_on = int(input("Enter desired pump run time:\n"))
        motor_on(motor1)
        motor_on(motor2)
        time.sleep(time_on)
        motor_off(motor1)
        motor_off(motor2)
        val = read_ai(0)
        print(val)

    except KeyboardInterrupt:
        print("\nProgram terminated as requested.")

    except Exception as e:
        print("\nAn unkown error occured at {}:{}. Program terminated.".format(datetime.now().hour, datetime.now().minute))
        print(e)

    finally:
        GPIO.cleanup()

