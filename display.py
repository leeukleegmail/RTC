from machine import Pin, I2C

import ssd1306_driver

i2c = I2C(scl=Pin(5), sda=Pin(4))
display = ssd1306_driver.SSD1306_I2C(128, 64, i2c)  # addr 60


def set_display(message):
    display.fill(0)
    display.text(message, 10, 26)
    display.show()
