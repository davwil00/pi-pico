from machine import Pin
import utime

led = Pin('LED', Pin.OUT)
led.high()
pins = [
    Pin(15, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(16, Pin.OUT),
    Pin(17, Pin.OUT)
]

full_step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

while True:
    for step in full_step_sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.001)
