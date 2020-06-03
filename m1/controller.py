import time
from threading import Semaphore
from m1.effects.blink_color import BlinkColor
from m1.effects.static_color import StaticColor
from m1.effects.th_ch import TheaterChase
from m1.effects.rainbow import Rainbow
from m1.effects.rainbow_cycle import RainbowCycle
from m1.effects.th_ch_rb import TheaterChaseRainbow

class Controller:
    """
    Controls the strip in a concurrent thread-safe manner.
    """


    def __init__(self, strip):
        self.semaphore = Semaphore(1)
        self.strip = strip
        self.current_thread = None


    def stop_current_thread(self):
        self.semaphore.acquire()
        self.current_thread.set_stop(True)
        self.semaphore.release()
        self.current_thread.join()


    def turn_off_strip(self):

        if self.current_thread is not None:
            self.stop_current_thread()

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, 0)
            self.strip.show()
            time.sleep(1 / 1000.0)


    def play_effect(self, effect_name, *args):

        if self.current_thread is not None:
            self.stop_current_thread()

        if effect_name.__eq__('blink_color'):
            self.current_thread =  BlinkColor(*args)
        elif effect_name.__eq__('static_color'):
            self.current_thread = StaticColor(*args)
        elif effect_name.__eq__('theater_chase'):
            self.current_thread = TheaterChase()
        elif effect_name.__eq__('rainbow'):
            self.current_thread = Rainbow()
        elif effect_name.__eq__('rainbow_cycle'):
            self.current_thread = RainbowCycle()
        elif  effect_name.__eq__('theater_chase_rainbow'):
            self.current_thread = TheaterChaseRainbow()
        else:
            raise ModuleNotFoundError()

        self.current_thread.set_semaphore(self.semaphore)
        self.current_thread.set_strip(self.strip)
        self.current_thread.start()
