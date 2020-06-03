import time
from rpi_ws281x import Color
from m1.effects.effect import Effect


class TheaterChase(Effect):
    """
    Movie theater light style chaser animation.
    Extracted from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
    """

    def __init__(self, color=Color(255, 0, 0), wait_ms=50):
        super(TheaterChase, self).__init__()
        self.color = color
        self.wait_ms = wait_ms

    def run(self):
        while not self.is_stop_flag_enabled():
            for q in self.range(3):
                for i in self.range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, self.color)
                self.strip.show()
                time.sleep(self.wait_ms / 1000.0)
                for i in self.range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)