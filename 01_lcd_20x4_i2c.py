from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep

i2c = I2C(
    0,
    sda=Pin(21),
    scl=Pin(22),
    freq=400000
)

lcd = I2cLcd(i2c, 0x27, 4, 20)

lcd.putstr("ESP32 + MicroPython")

lcd.move_to(0, 1)
lcd.putstr("LCD 20x4")

lcd.move_to(0, 2)
lcd.putstr("I2C funcionando")

lcd.move_to(0, 3)
lcd.putstr("Wokwi")

while True:
    sleep(1)
