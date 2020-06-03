from rpi_ws281x import Color


def wheel(pos):
    """
    Generate rainbow colors across 0-255 positions.
    Extracted from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
    """
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)