'''
hershey.py
    Draw greetings on display cycling thru hershey fonts and colors
'''

import utime
from machine import SPI, Pin
import gc9a01

# Load several frozen fonts from flash

from vector import greeks
from vector import italicc
from vector import italiccs
from vector import meteo
from vector import music
from vector import romanc
from vector import romancs
from vector import romand
from vector import romanp
from vector import romans

from vector import scriptc
from vector import scripts


def cycle(p):
    '''
    return the next item in a list
    '''
    try:
        len(p)
    except TypeError:
        cache = []
        for i in p:
            yield i
            cache.append(i)
        p = cache
    while p:
        yield from p


COLORS = cycle([0xe000, 0xece0, 0xe7e0, 0x5e0, 0x00d3, 0x7030])

FONTS = cycle([
    greeks, italicc, italiccs, meteo, music, romanc,
    romancs, romand, romanp, romans, scriptc, scripts])

GREETINGS = cycle([
    "bonjour", "buenas noches", "buenos dias",
    "good day", "good morning", "hey",
    "hi-ya", "hi", "how are you", "how goes it",
    "howdy-do", "howdy", "shalom", "welcome",
    "what's happening", "what's up"])


def main():
    '''
    Draw greetings on display cycling thru hershey fonts and colors
    '''
    try:
        spi = SPI(2, baudrate=80000000, polarity=0, sck=Pin(10), mosi=Pin(11))

        tft = gc9a01.GC9A01(
            spi,
            240,
            240,
            reset=Pin(14, Pin.OUT),
            cs=Pin(9, Pin.OUT),
            dc=Pin(8, Pin.OUT),
            backlight=Pin(2, Pin.OUT),
            rotation=0,)

        tft.init()
        tft.fill(gc9a01.BLACK)
        height = tft.height()
        width = tft.width()
        row = 0

        while True:
            row += 32
            color = next(COLORS)
            tft.fill_rect(0, row-16, width, 32, gc9a01.BLACK)
            tft.draw(next(FONTS), next(GREETINGS), 0, row, color)

            if row > 192:
                row = 0

            utime.sleep(0.25)

    finally:
        # shutdown spi
        if 'spi' in locals():
            spi.deinit()


main()
