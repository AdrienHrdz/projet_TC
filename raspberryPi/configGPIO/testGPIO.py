from gpiozero import LED
from time import sleep

led = LED(6)

while True:
    led.on()
    print("led on")
    sleep(5)
    
    led.off()
    print("led off")
    sleep(10)
