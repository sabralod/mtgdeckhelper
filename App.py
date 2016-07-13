# Flask is the rest framework
from flask import Flask
from flask import request
from flask import make_response

# json is an package which is able to decode/encode json objects
import json

# Here we import our DatabaseProvider as a variable db
import DatabaseProvider.DatabaseProvider as db
import RestProvider.RestProvider as rest

# Creating our Flask App
app = Flask(__name__)

@app.route("/user/<id>", methods=["GET"])
def showUser(id):
    print("Get user with id " + id)
    print(request.path)
    return "Ok",200

# Receive an POST request with form data request
@app.route("/user", methods=["POST"])
def hello():
    # Here we have am request object which holds information
    # about the request
    list = {"a": "hallo", "b": "Hello", "c": "bLa"}
    # Logging the form value name
    print(request.form["name"])
    # First parameter is the json string, second value is http code (200, OK)
    resp = make_response(json.dumps(list), 200)
    # Setting content headers to 'application/json'
    resp.headers["Content-Type"] = "application/json"
    # Overwriting server name
    resp.headers["Server"] = "UnserCoolerServer"
    # We can set other http header values here, like cache etc
    return resp
# Accessing functions and classes from other files:
db.helloDb()

# Run our flask app
# The run() function is not asynchronous!!! All code after that function isnt
# executed any more :(
app.run();
