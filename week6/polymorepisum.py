"""
Description: This script is used to on device
Author: Dhruval patel
"""

class Device:
    def turn_on(self):
        pass

class TV(Device):
    def turn_on(self):
        return "TV is now on"
    
class Fan(Device):
    def turn_on(self):
        return "Fan is now spinning"
    
class Light(Device):
    def turn_on(self):
        return "Light is now on"
    
def acctivate_device(device):
    print(device.turn_on())


tv = TV()
fan = Fan()
light = Light()

acctivate_device(tv)
acctivate_device(fan)
acctivate_device(light)