#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_1=GPIO.input(22)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_2=GPIO.input(17)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_3=GPIO.input(18)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
button_4=GPIO.input(27)

pump_1=mh.getMotor(1)
pump_2=mh.getMotor(2)
pump_3=mh.getMotor(3)
pump_4=mh.getMotor(4)

pump_speed = 255

def startPumps():
    pump_1.run(Adafruit_MotorHAT.FORWARD)
    pump_1.setSpeed(pump_speed)
    pump_2.run(Adafruit_MotorHAT.FORWARD)
    pump_2.setSpeed(pump_speed)
    pump_3.run(Adafruit_MotorHAT.FORWARD)
    pump_3.setSpeed(pump_speed)
    pump_4.run(Adafruit_MotorHAT.FORWARD)
    pump_4.setSpeed(pump_speed)
    time.sleep(0.01)

def stopPumps():
   pump_1.run(Adafruit_MotorHAT.RELEASE)
   pump_2.run(Adafruit_MotorHAT.RELEASE)
   pump_3.run(Adafruit_MotorHAT.RELEASE)
   pump_4.run(Adafruit_MotorHAT.RELEASE)
   time.sleep(0.01)
   GPIO.cleanup()

def dispense():
    while True:
        input_state =  GPIO.input(22)
        if input_state == False:
            print("pouring fucking sanitizer")
            startPumps()
            continue
        stopPumps()

dispense()
