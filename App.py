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

# Instantiate RestProvider for deckbrew
deckbrew = rest.RestProvider()

@app.route("/collection/<id>/<cardId>")
def deleteCard(id, cardId):
    print("Deleted: " + cardId +" from collection " + id)
    return "Deleted: " + cardId +" from collection " + id, 200

@app.route("/collection/<id>", methods=["DELETE"])
def removeCollection(id):
    print("Removing collection " + id)
    return "Deleted: " + id, 200

@app.route("/find", methods=["GET"])
def searchCard():
    phrase = ""
    phrase += request.args.get("text")
    resp = make_response(deckbrew.queryName(phrase), 200)
    resp.headers["Content-Type"] = "application/json"
    return resp

@app.route("/collection/<id>/cards", methods=["GET"])
def getAllCards(id):
    print("Returning all cards of collection " + id)
    return "Cards of collection " + id, 200

@app.route("/collection/<id>/card", methods=["POST"])
def addCard(id):
    cardId = request.form["cardId"]
    print("Adding card to collection " + id)
    return "Added card " + id, 200

# Get all collection of user
@app.route("/user/<id>/collections", methods=["GET"])
def getUserCollection(id):
    print("Getting all collections of user " + id)
    return "Collections of user " + id, 200

# Get user information
@app.route("/user/<id>", methods=["GET"])
def getUser(id):
    print("Get user with id " + id)
    print(request.path)
    return "Getting user " + id,200

# Create collection
@app.route("/user/<id>/collection", methods=["POST"])
def addCollection(id):
    print("Creating collection for user " + id)
    collectionName = request.form["collectionName"]
    print("CollectionName: "+collectionName)
    return "Created collection: "+collectionName, 200

# Create new user with name
@app.route("/user", methods=["POST"])
def addUser():
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
