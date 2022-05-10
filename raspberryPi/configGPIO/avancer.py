#pin STM: PC6
from gpiozero import LED
from time import sleep

led = LED(6)


led.on()
print("led on")
sleep(5)

led.off()
print("led off")
