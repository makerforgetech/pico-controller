from machine import Pin, Timer, ADC
led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=.5, mode=Timer.PERIODIC, callback=blink)

import time
import utime
from neopixel import Neopixel
 
numpix = 45
pin = 1

motion = Pin(0, machine.Pin.IN, Pin.PULL_DOWN)
xthumb = ADC(Pin(27))
ythumb = ADC(Pin(26))
swthumb = Pin(2, machine.Pin.IN, Pin.PULL_UP)
input_cooldown = False
input_threshold_upper = 40000
input_threshold_lower = 30000

pixels = Neopixel(numpix, 0, pin, "GRB")

# Primary colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Secondary colors
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# Tertiary colors
amber = (255, 191, 0)
vermilion = (227, 66, 52)
chartreuse = (127, 255, 0)
spring_green = (0, 255, 127)
azure = (0, 127, 255)
violet = (127, 0, 255)
rose = (255, 0, 127)

# Update the colors list
colors = (
    red, green, blue, white, yellow, cyan, magenta,
    amber, vermilion, chartreuse, spring_green, azure, violet, rose
)

current = 6
 
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
    global input_cooldown
    global input_threshold_upper, input_threshold_lower
    if input_cooldown:
        if xthumb.read_u16() < input_threshold_upper and xthumb.read_u16() > input_threshold_lower and ythumb.read_u16() < input_threshold_upper and ythumb.read_u16() > input_threshold_lower:
            input_cooldown = False
        return
    # Change brightness
    if xthumb.read_u16() > input_threshold_upper:
        brightness = brightness + 1
        if brightness > 255:
            brightness = 255
    elif xthumb.read_u16() < input_threshold_lower:
        brightness = brightness - 1
        if brightness < 0:
            brightness = 0

    # Change colour
    if ythumb.read_u16() > input_threshold_upper:
        current = current + 1
        if current >= len(colors):
            current = len(colors)-1
        input_cooldown = True
    elif ythumb.read_u16() < input_threshold_lower:
        current = current - 1
        if current < 0:
            current = 0
        input_cooldown = True
    
 
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
        #pixels.set_pixel_advanced(8, colors[current], brightness + 20)
    else:
        pixels.fill(white)
        #pixels.set_pixel_advanced(8, white, brightness + 20)
    
    # Turn off neopixels if idle
    if motion.value() == 1:
        last_motion = utime.ticks_ms()
    elif utime.ticks_ms() - last_motion > sleep_timeout:
        pixels.fill((0,0,0))
    
    pixels.show()
    time.sleep(.1)

