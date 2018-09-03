import time


# Измерение время работы куска кода
class Profiler():
    def __init__(self):
        self._startTime = 0

    def start(self):
        self._startTime = time.time()

    def finish(self, rtrn = False):
        s = "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)
        if rtrn:
            return format(time.time() - self._startTime)
        else:
            print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))