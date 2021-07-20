
import wave
import contextlib
import os
import math

class LrcCalc:
    total_duration = 0
    total_min = 0
    total_sec = 0
    total_msec = 0

    def add_total_time(self, duration):
        self.total_min = math.floor(float(self.total_duration / 60))
        self.total_sec = math.floor(float(self.total_duration % 60))
        self.total_msec = math.floor((float(self.total_duration % 60 - self.total_sec) * 100))
        self.total_duration += duration

    def get_wave_lrc_time(self, path, name):
        with contextlib.closing(wave.open(path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = round(frames / float(rate), 2)
            return self.get_full_lrc(self.get_time_detail(duration), path, name)

    def get_time_detail(self, duration):
        if(self.total_duration != 0):
            self.add_total_time(0.2)
        self.add_total_time(duration)

        return self.lrc_format(self.total_min, self.total_sec, self.total_msec)

    def lrc_format(self, min, sec, msec):
        return ("[" + str(min) + ":" + str(sec) + "." + str(msec) + "]")

    def get_full_lrc(self, time, path, name):
        lis = []
        lis.append(time + os.path.basename(path).replace(".wav",""))
        lis.append(time + name)
        return lis
