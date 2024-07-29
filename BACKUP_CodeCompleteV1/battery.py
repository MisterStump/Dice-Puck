# Cobbled together from a reference source
# https://github.com/micropython/micropython/blob/master/docs/library/machine.ADC.rst

from machine import ADC


class BATTERY():
    def __init__(self):
        self.pin = 1
        self.battery = ADC(self.pin)

    def rawAnalog(self):
        # read a raw analog value in the range 0-65535
        return self.battery.read_u16()
        
    def getLevel(self):
        # Return a percentage (0-100) as an int
        currentLevel = self.rawAnalog()
        maxLevel = 65535
        return int(round(currentLevel / maxLevel, 2) * 100)