import time
from m1.effects.effect import Effect
from m1.effects.utils import wheel


class TheaterChaseRainbow(Effect):
    """
    Rainbow movie theater light style chaser animation.
    Extracted from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
    """

    def __init__(self, wait_ms=50):
        super(TheaterChaseRainbow, self).__init__()
        self.wait_ms = wait_ms

    def run(self):
        for j in self.range(256):
            for q in range(3):
                for i in self.range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, wheel((i + j) % 255))
                self.strip.show()
                time.sleep(self.wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)



