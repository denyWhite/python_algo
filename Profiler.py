"""
Простой профайлер для измерения времени работы куска кода
"""
import time



class Profiler:
    def __init__(self):
        self._startTime = 0

    def start(self):
        """"Старт измерения"""
        self._startTime = time.time()

    def finish(self, rtrn=False):
        """Конец измерения"""
        if rtrn:
            return format(time.time() - self._startTime)
        else:
            print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))
