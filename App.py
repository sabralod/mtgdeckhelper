# Flask is the rest framework
from flask import Flask
from flask import request
from flask import make_response

# json is an package which is able to decode/encode json objects
import json
# Here we import our DatabaseProvider as a variable db
import DatabaseProvider as db
import RestProvider as rest

# Creating our Flask App
app = Flask(__name__)

# Instantiate RestProvider for deckbrew
deckbrew = rest.RestProvider()
database = db.DatabaseProvider()

# Find cards with optional filter arguments
@app.route("/find", methods=['GET'])
def searchCard():
    resp = None
    result = None

    try:
        result = json.loads(deckbrew.query(request.args))
        resp = make_response(json.dumps(result), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Add user to database
@app.route("/user", methods=['POST'])
def addUser():
    resp = None

    try:
        database.addUser(request.form['name'])
        resp = make_response(json.dumps({'success':True}), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Delete user in database
@app.route("/user", methods=['DELETE'])
def deleteUser():
    resp = None

    try:
        database.deleteUser(request.form['name'])
        resp = make_response(json.dumps({'success':True}), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Add card to user's collection
@app.route("/user/<username>/card", methods=['POST'])
def addCard(username):
    resp = None

    try:
        database.addCard(request.form['name'], username)
        resp = make_response(json.dumps({'success':True}), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Get all cards from user's collection with optional filter arguments
@app.route("/user/<username>/cards", methods=['GET'])
def getCollection(username):
    resp = None
    result = []

    try:
        # First get all cards from user's collection
        collection = database.getCollection(username)

        # Request card from API and apply filter arguments
        for c in collection:
            print c
            result.append(json.loads(deckbrew.queryByCardName(c[1], request.args)))

        resp = make_response(json.dumps(result), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        print e
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Delete a card from user's collection
@app.route("/user/<username>/card/<cardname>", methods=['DELETE'])
def deleteCard(username, cardname):
    resp = None

    try:
        database.deleteCard(cardname, username)
        resp = make_response(json.dumps({'success':True}), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        print e
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

# Get all users - mostly used for testing
@app.route("/users", methods=['GET'])
def getUsers():
    resp = None
    result = None

    try:
        result = database.getUsers()
        resp = make_response(json.dumps(result), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        print e
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp
# Run our flask app
# The run() function is not asynchronous!!! All code after that function isnt
# executed any more :(
app.run();
