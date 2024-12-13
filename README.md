# pico-controller

This project is a wifi enabled controller module, and includes an uninterruptable power supply (UPS) and a custom PCB utilising the Raspberry Pi Pico. 
The controller is designed to be used in a variety of applications and the hardware includes an array of neopixels, connected in series to allow for a variety of lighting effects.

Note: This is in active development and is not yet ready for community adoption. Please be patient and check back for updates.

## Features

- Joystick control of neopixels
- Wifi integration
- UPS modules
- Custom PCB
- Neopixel array
- 18650 battery management

## Bill of Materials

| Part | Quantity | Description | Link |
| --- | --- | --- | --- |
| 18650 battery | 1 | 3.7V 18650 battery | - |
| 18650 UPS module | 1 | 18650 battery shield | [Link](https://www.wildware.net/products/18650-battery-shield) |
| Neopixel LED strip | 2 | 5V neopixel LED strip | - |
| Raspberry Pi Pico | 1 | Raspberry Pi Pico | [Link](https://www.raspberrypi.org/products/raspberry-pi-pico/) |
| Magnetic connectors (4 pin) | 3 pairs | Allows data and power connection between modules | - |
| Magnetic connectors (2 pin) | 1 pair | Allows power connection between power cell and base unit for charging | - |
| Toggle push switch with LED | 1 | Toggle push switch with LED | - |
| Wires | - | Various colours and lengths | - |
| Neopixel Ring | 1 | 8 LED neopixel ring | - |
| Neopixel Jewel | 1 | 7 LED neopixel jewel | - |
| Neopixel Module | 1 | 1 LED neopixel module | - |
| 3D printed parts | various | 3D printed parts | - |
| Joystick module | 1 | Joystick module | - |
| Microwave sensor | 1 | Microwave sensor | - |
| Momentary push button | 1 | Momentary push button | - |
| Custom PCB | 1 | Custom PCB | See PCB folder |

## UPS Wiring

![UPS WIRING DIAGRAM](https://github.com/makerforgetech/pico-controller/blob/main/ups_wiring.drawio.svg)

## Pico Controller PCB

[PCB Files - KiCad](https://github.com/makerforgetech/pico-controller/tree/main/PCB/PicoController)
