from time import sleep

from display import set_display
from rtc import read_time_from_rtc

while True:
    current_time = read_time_from_rtc()
    set_display(current_time)
    sleep(0.5)
