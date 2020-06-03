import time
from rpi_ws281x import Color
from m1.effects.effect import Effect


class BlinkColor(Effect):
    """
    All led with same color
    """

    def __init__(self, color: Color, times=3, wait_ms=500):
        super(BlinkColor, self).__init__()
        self.color = color
        self.wait_ms = wait_ms
        self.times = times

    def run(self):
        for _ in self.range(self.times):
            for j in self.range(self.strip.numPixels()):
                self.strip.setPixelColor(j, self.color)
            self.strip.show()
            time.sleep(self.wait_ms / 1000.0)
            for j in self.range(self.strip.numPixels()):
                self.strip.setPixelColor(j, 0)
            self.strip.show()
            time.sleep(self.wait_ms / 1000.0)



