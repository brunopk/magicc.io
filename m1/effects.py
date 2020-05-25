import time

from rpi_ws281x import Color

# Following effects were extracted from
# https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py

# TODO Implement to stop effects abruptly

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def color_wipe(strip, color, wait_ms=50):
    """
    Wipe color across display a pixel at a time.
    """
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theater_chase(strip, color=Color(255, 0, 0), wait_ms=50, iterations=10):
    """
    Movie theater light style chaser animation.
    """
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def rainbow(strip, wait_ms=20, iterations=1):
    """
    Draw rainbow that fades across all pixels at once.
    """
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbow_cycle(strip, wait_ms=20, iterations=1):
    """
    Draw rainbow that uniformly distributes itself across all pixels.
    """
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theater_chase_rainbow(strip, wait_ms=50):
    """
    Rainbow movie theater light style chaser animation.
    """
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


# -------------------------------------------------------------------------------------------------------------------- #

def turn_off(strip, wait_ms=1):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
        strip.show()
        time.sleep(wait_ms/1000.0)


def static_color(strip, color, wait_ms=1):
    """
    All leds with same color
    """
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def blink_color(strip, color, times=3, wait_ms=500):
    for i in range(times):
        for j in range(strip.numPixels()):
            strip.setPixelColor(j, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        for j in range(strip.numPixels()):
            strip.setPixelColor(j, 0)
        strip.show()
        time.sleep(wait_ms/1000.0)
