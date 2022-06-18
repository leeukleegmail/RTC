import ntptime
from utime import sleep

from Network import enable_network
from rtc import set_time_for_rtc, read_time_from_rtc
from util import get_time_json

enable_network()

ntptime.settime()

tm = get_time_json()

set_time_for_rtc(tm["year"], tm["month"], tm["day"], tm["hour"], tm["minutes"], tm["seconds"], 123)

while True:
    current_time = read_time_from_rtc()
    print(current_time)
    sleep(0.5)
