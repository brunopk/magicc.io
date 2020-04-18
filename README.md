# strip.controller

Client/Server app to control W2812B led strips using a Raspberry Pi 3, [flask](https://flask.palletsprojects.com/en/1.1.x/) and socket.io

Tested with Python v3.6.4

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
