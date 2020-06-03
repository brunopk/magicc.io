from threading import Thread, Semaphore
from rpi_ws281x import PixelStrip

class Effect(Thread):

    def __init__(self):
        super(Effect, self).__init__()
        self.semaphore = None
        self.stop = False
        self.strip = None

    def is_stop_flag_enabled(self):
        self.semaphore.acquire()
        stop = self.stop
        self.semaphore.release()
        return stop

    def range(self, start, stop=None, step=None):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        for i in range(start, stop, step):
            if self.is_stop_flag_enabled():
                break
            yield i

    def set_semaphore(self, semaphore:Semaphore):
        self.semaphore = semaphore

    def set_stop(self, stop:bool):
        self.stop = stop

    def set_strip(self, strip:PixelStrip):
        self.strip = strip