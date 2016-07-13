#Used libraries:

##Flask for Restful Service

Creating a restful interface for our frontend application
http://flask.pocoo.org/docs/0.11/quickstart/

##Python Json
Encoding and decoding python objects and tuples to json
https://docs.python.org/2.7/library/json.html

##Rest Routes
* POST /user with data username and returns the new user id
* GET /user/<id> returns user data
* POST /user/<id>/collection creates new collection with data collection name and retusn collection id
* GET /user/<id>/collections returns all collections of the user
* POST /collection/<id>/card adds a new card to the collection
* GET /collection/<id>/cards gets all cards in the collection
