from machine import I2C, Pin

import urtc_driver

i2c = I2C(scl=Pin(5), sda=Pin(4))
rtc = urtc_driver.DS1307(i2c)


def read_time_from_rtc():
    datetime = rtc.datetime()

    seconds = add_leading_zero_if_required(datetime.second)
    minutes = add_leading_zero_if_required(datetime.minute)
    hours = add_leading_zero_if_required(datetime.hour)

    return "{}:{}.{}".format(hours, minutes, seconds)


def set_time_for_rtc(year=None, month=None, day=None, weekday=None, hour=None, minutes=None, seconds=None, miliseconds=None):
    rtc.datetime((year, month, day, weekday, hour, minutes, seconds, miliseconds))  # set a specific date and time


def add_leading_zero_if_required(datetime):
    if datetime < 10:
        return "0" + str(datetime)
    else:
        return datetime
