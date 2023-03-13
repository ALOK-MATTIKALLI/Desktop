import RPi.GPIO as GPIO
import time

freq = 1000
GPIO.setmode(GPIO.BCM)

    
class MotorControl:
    def __init__(self,pins):
        for i in pins:
            GPIO.setup(i, GPIO.OUT)

        self.m1a = GPIO.PWM(pins[0], freq)
        self.m1b = GPIO.PWM(pins[1], freq)
        self.m2a = GPIO.PWM(pins[2], freq)
        self.m2b = GPIO.PWM(pins[3], freq)
        self.m1a.start(0)
        self.m1b.start(0)
        self.m2a.start(0)
        self.m2b.start(0)

    def drive(self,l_speed, r_speed):
        if l_speed > 0 and r_speed > 0:
            self.motor_excite(l_speed, 0, r_speed,0)

        elif l_speed < 0 and r_speed > 0:
            self.motor_excite(0,abs(l_speed), r_speed,0 )
        
        elif l_speed > 0 and r_speed < 0:
            self.motor_excite(l_speed, 0, 0, abs(r_speed))

        elif l_speed < 0 and r_speed < 0:
            self.motor_excite(0, abs(l_speed), 0, abs(r_speed))

        else:
            self.motor_excite(0,0,0,0)
            

    def motor_excite(self,m1a,m1b,m2a,m2b):
        self.m1a.ChangeDutyCycle(m1a)
        self.m1b.ChangeDutyCycle(m1b)
        self.m2a.ChangeDutyCycle(m2a)
        self.m2b.ChangeDutyCycle(m2b)

