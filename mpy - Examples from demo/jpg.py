'''
jpegtest.py

    Draw a full screen jpg using the slower but less memory intensive method
    of blitting each Minimum Coded Unit (MCU) block. Usually 8×8pixels but can
    be other multiples of 8.

    bigbuckbunny.jpg (c) copyright 2008, Blender Foundation / www.bigbuckbunny.org
'''

import gc
import time
from machine import Pin, SPI
import gc9a01

gc.enable()
gc.collect()


def main():
    '''
    Decode and draw the jpg on the display
    '''
    try:

        # initialize display

        tft = gc9a01.GC9A01(
            SPI(2, baudrate=80000000, polarity=0, sck=Pin(10), mosi=Pin(11)),
            240,
            240,
            reset=Pin(14, Pin.OUT),
            cs=Pin(9, Pin.OUT),
            dc=Pin(8, Pin.OUT),
            backlight=Pin(2, Pin.OUT),
            rotation=0)

        # enable display and clear screen
        tft.init()

        # display jpg
        while True:
            for imagein ["bigbuckbunny.jpg", "bluemarble.jpg"]:
                tft.jpg(image, 0, 0, gc9a01.SLOW)
                time.sleep(5)

    finally:
        # shutdown spi
        if 'spi' in locals():
            spi.deinit()


main()
