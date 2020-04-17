# magicc.io

Server app to control W2812B led strips using socket.io and [flask](https://flask.palletsprojects.com/en/1.1.x/)

## Running the server (development mode)

1. Create the Python environment:
 
    `virtualenv env`
2. Activate the environment: 

    `source env/bin/activate`
3. Tell your terminal the application to work with by exporting the FLASK_APP environment variable: 

    `export FLASK_APP=main.py`
4. Run the server : 
    
    `flask run`
    
    or 
    
    `python -m flask run`
