# strip.controller

strip.controller makes possible to control W2812B led strips using a Raspberry Pi 3. It's conformed by two modules (programs): 
**m1** and **m2**.  m1 provides an interface to send specific PWM (pulse-width modulation) signals to the strip. m2 provides a 
GUI created with [flask](https://flask.palletsprojects.com/en/1.1.x/) (client/server application) which receive orders from the user 
(e.g. turning the strip on blue color) and sends them to m1. m1 and m2 interacts with commands represented as JSON objects 
sent by TCP.


## Python versions

Tested with :

- 3.6.4
- 3.7.3

## Software requirements

- virtualenv

## Running strip.controller

First, m1 must be run:

1. `cd m1/`
2. `chmod +x server.py`
3. `sudo ./server.py`

> Root privileges are needed in order to gain access to the GPIO and other hardware components.

Then m2 :

1. `cd m2/`
2. `mkdir m2/static/css`
3. `export FLASK_APP=main.py`
4. `export FLASK_ENV=development`
5. `export PYTHONPATH=../`
6. `flask run --host=0.0.0.0`

> The FLASK_ENV environment variable allows flask to run on development mode and compile SCSS files automatically (hot reloading)
> generating CSS files on `m2/static/css` directory.

## Building the circuit

1. With level shifter conversor:

![GitHub Logo](/doc/Raspberry-Pi-WS2812-Steckplatine-600x361.png)

More information: https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/

2. Without level shifter conversor: 
![GitHub Logo](/doc/raspberry-pi-updated-schematic.png)
More information: https://core-electronics.com.au/tutorials/ws2812-addressable-leds-raspberry-pi-quickstart-guide.html


## Links

- https://github.com/rpi-ws281x/rpi-ws281x-python 
- http://github.com/richardghirst/rpi_ws281x