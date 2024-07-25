"""
rotation.py

    Shows the effect of each of the 8 rotation values on the display.

"""
import utime
from machine import Pin, SPI
import gc9a01
from bitmap import vga1_bold_16x32 as font


def main():
    tft = gc9a01.GC9A01(
        SPI(2, baudrate=60000000,polarity=0, sck=Pin(10), mosi=Pin(11)),
        240,
        240,
        reset=Pin(14, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(2, Pin.OUT),
        rotation=0,
        buffer_size=16*32*2)

    tft.init()
    tft.fill(gc9a01.BLACK)
    utime.sleep(1)

    while True:
        for rot in range(8):
            tft.fill(gc9a01.BLACK)
            tft.rotation(rot)
            s = "Rotation {}".format(rot)
            tft.text(font, s, 40, 104, gc9a01.WHITE)
            utime.sleep(3)


main()
