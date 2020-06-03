import time
from rpi_ws281x import Color
from m1.effects.effect import Effect


class StaticColor(Effect):
    """
    All leds with same color
    """

    def __init__(self, color:Color, wait_ms=1):
        super(StaticColor, self).__init__()
        self.color = color
        self.wait_ms = wait_ms

    def run(self):
        for i in self.range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(self.wait_ms / 1000.0)