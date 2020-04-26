# strip.controller

Client/Server app to control W2812B led strips using a Raspberry Pi 3, [flask](https://flask.palletsprojects.com/en/1.1.x/) and socket.io. 
Signals for the leds are generated with the [rpi-ws281x](https://github.com/rpi-ws281x/rpi-ws281x-python) module which is 
the official Python distribution of the [ws281x library](http://github.com/richardghirst/rpi_ws281x).

## Python versions

Tested with :

- 3.6.4
- 3.7.3

## Requirements

- virtualenv

## Running the server (debug mode)

1. Create the Python environment:
 
    `virtualenv -p path/to/python/interpreter env`
2. Activate the environment: 

    `source env/bin/activate`
3. Tell your terminal the application to work with by exporting the FLASK_APP environment variable: 

    `export FLASK_APP=main.py`
4. Set the environment variable to run flask on debug mode:

   `export FLASK_ENV=development`
5. Run the server : 
    
    `flask run`
    
    or 
    
    `python -m flask run`

> - `FLASK_ENV=development` enables hot reloading 
> - Parameter `--host=0.0.0.0` tells flask to publish server on any IP address
> - Root privileges are needed to use GPIO ports so flask must be run with `sudo` : `sudo env/bin/python flask run`

## Building the circuit

1. With level shifter conversor: 
![GitHub Logo](/doc/Raspberry-Pi-WS2812-Steckplatine-600x361.png)

More information: https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/

2. Without level shifter conversor: 
![GitHub Logo](/doc/raspberry-pi-updated-schematic.png)
More information: https://core-electronics.com.au/tutorials/ws2812-addressable-leds-raspberry-pi-quickstart-guide.html
