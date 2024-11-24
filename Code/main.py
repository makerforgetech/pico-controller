from machine import Pin, Timer, ADC
led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=.5, mode=Timer.PERIODIC, callback=blink)

import time
import utime
from neopixel import Neopixel
 
numpix = 30
pin = 1

motion = Pin(0, machine.Pin.IN, Pin.PULL_DOWN)
xthumb = ADC(Pin(27))
ythumb = ADC(Pin(26))
swthumb = Pin(2, machine.Pin.IN, Pin.PULL_UP)


pixels = Neopixel(numpix, 0, pin, "GRB")

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (255, 255, 255)
colors = (red, orange, yellow, green, blue, indigo, violet, white)

current = 5
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color0 = red
 
brightness = 6
pixels.brightness(brightness)

sleep_timeout = 30000

pixels.fill(colors[current])
#pixels.set_pixel_line_gradient(0, 13, green, blue)
#pixels.set_pixel_line(14, 16, red)
#pixels.set_pixel(20, (255, 255, 255))
last_motion = utime.ticks_ms()

direction = -1
def glimmer(min_brightness, max_brightness, step):
    global direction
    global brightness
    if direction > 0:
        brightness += step
        if brightness >= max_brightness:
            direction = -1
    if direction < 0:
        brightness -= step
        if brightness <= min_brightness:
            direction = 1

def fade(min_brightness, max_brightness, step):
    global direction
    global brightness
    print(brightness)
    if direction > 0:
        brightness += step
        if brightness >= max_brightness:
            brightness = max_brightness
            return 0
    if direction < 0:
        brightness -= step
        if brightness <= min_brightness:
            brightness = min_brightness
            return 0
    return 1

def thumbstick_input():
    global brightness
    global current
    # Change brightness
    if xthumb.read_u16() > 40000:
        brightness = brightness + 1
        if brightness > 255:
            brightness = 255
    elif xthumb.read_u16() < 30000:
        brightness = brightness - 1
        if brightness < 0:
            brightness = 0
    # Change colour
    if ythumb.read_u16() > 40000:
        current = current + 1
        if current >= len(colors):
            current = len(colors)-1
    elif ythumb.read_u16() < 30000:
        current = current - 1
        if current < 0:
            current = 0
    
 
while True:
    thumbstick_input()
            
    glimmer(2, 20, .1)
    
    pixels.brightness(brightness)
    #print(ythumb.read_u16())
    #print(xthumb.read_u16())
    #print(current)
    #print(brightness)
    
    if swthumb.value() == 1:
        pixels.fill(colors[current])
        pixels.set_pixel_advanced(8, colors[current], brightness + 20)
    else:
        pixels.fill(white)
        pixels.set_pixel_advanced(8, white, brightness + 20)

        
    
    
    # Turn off neopixels if idle
    if motion.value() == 1:
        last_motion = utime.ticks_ms()
    elif utime.ticks_ms() - last_motion > sleep_timeout:
        pixels.fill((0,0,0))
    
    pixels.show()
    time.sleep(.1)

