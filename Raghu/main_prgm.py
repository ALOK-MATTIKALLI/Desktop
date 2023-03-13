from motor_control import MotorControl
import time

pins = [17,27,10,9]
drive = MotorControl(pins)
drive.drive(25,25)
time.sleep(1)