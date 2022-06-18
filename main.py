from time import localtime

import ntptime
from utime import sleep

from Network import enable_network
from rtc import set_time_for_rtc, read_time_from_rtc

enable_network()

ntptime.settime()
lt = localtime()

tm = {
    'year': lt[0],
    'month': lt[1],
    'day': lt[2],
    'hour': lt[3],
    'minutes': lt[4],
    'seconds': lt[5]
}

set_time_for_rtc(tm["year"], tm["month"], tm["day"], tm["hour"], tm["hour"], tm["seconds"], miliseconds=000)

while True:
    current_time = read_time_from_rtc()
    print(current_time)
    sleep(0.5)
