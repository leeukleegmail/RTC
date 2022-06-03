from rtc import read_time_from_rtc
from display import set_display


while True:
    current_time = read_time_from_rtc()
    set_display(current_time)

