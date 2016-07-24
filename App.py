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

@app.route("/find", methods=["GET"])
def searchCard():
    for arg in request.args:
        print arg

    data = json.loads(deckbrew.query(request.args))

    # for d in data:
    #     print d['id']

    resp = make_response(json.dumps(data), 200)
    resp.headers["Content-Type"] = "application/json"
    return resp

@app.route("/user", methods=["POST"])
def addUser():
    print request.form['name']

    resp = None

    try:
        database.addUser(request.form['name'])
        resp = make_response(json.dumps({'success':True}), 200)
        resp.headers["Content-Type"] = "application/json"
    except Exception as e:
        resp = make_response(json.dumps({'success':False}), 404)
        resp.headers["Content-Type"] = "application/json"

    return resp

@app.route("/user/<id>/card", methods=["POST"])
def addCard():
    

# Run our flask app
# The run() function is not asynchronous!!! All code after that function isnt
# executed any more :(
app.run();
