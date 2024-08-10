# Cobbled together from a reference source
# https://github.com/micropython/micropython/blob/master/docs/library/machine.ADC.rst

from machine import Pin,ADC
from math import ceil

class BATTERY():
    def __init__(self):
        self.pin = Pin(1, Pin.IN)
        self.battery = ADC(self.pin)
        #self.battery.atten(ADC.ATTN_0DB)
        #self.battery.width(ADC.WIDTH_12BIT)
        self.battery.atten(ADC.ATTN_11DB)

    def rawAnalog(self):
        # read a raw analog value in the range 0-65535
        #return self.battery.read_u16()
        return self.battery.read_uv()
        #return self.battery.read() * (3.3/4095)
        #return self.battery.read_uv() * (3.3 / 4096 * 3)
        
    def getLevel(self):
        # Return a percentage (0-100) as an int
        currentLevel = round(self.rawAnalog()/100000,0)
        #maxLevel = 65535
        #maxLevel = 152
        maxLevel = 12
        #maxLevel = 31000
        #maxLevel = 1521000
        return ceil(round(currentLevel / maxLevel, 3) * 100)