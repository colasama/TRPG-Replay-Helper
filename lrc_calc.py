
import wave
import contextlib
import os

class LrcCalc:
    total_min = 0
    total_sec = 0
    total_msec = 0

    def get_wave_lrc_time(self, path):
        with contextlib.closing(wave.open(path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = round(frames / float(rate), 2)
            return self.get_full_lrc(self.get_time_detail(duration), path)

    def get_time_detail(self, duration):
        min = round(duration / 60)
        sec = round(duration % 60)
        msec = round((duration % 60 - sec) * 100)
        self.total_min += min
        self.total_sec += sec
        self.total_msec += msec

        if(self.total_msec > 100):
            self.total_sec += 1
            self.total_msec -= 100

        if(self.total_sec > 60):
            self.total_min += 1
            self.total_sec -= 60

        return self.lrc_format(self.total_min, self.total_sec, self.total_msec)

    def lrc_format(self, min, sec, msec):
        return ("[" + str(min) + ":" + str(sec) + "." + str(msec) + "]")

    def get_full_lrc(self, time, path):
        return time + os.path.basename(path).replace(".wav","")
