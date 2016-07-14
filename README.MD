#Used libraries:

##Flask for Restful Service

Creating a restful interface for our frontend application
http://flask.pocoo.org/docs/0.11/quickstart/

##Python Json
Encoding and decoding python objects and tuples to json
https://docs.python.org/2.7/library/json.html

##Rest Routes
* POST /user with data username and returns the new user id
* GET /user/_id_ returns user data
* POST /user/_id_/collection creates new collection with data collection name and return collection id
* GET /user/_id_/collections returns all collections of the user

* POST /collection/_id_/card adds a new card to the collection and returns card id
* GET /collection/_id_/cards gets all cards in the collection
* DELETE /collection/_id_ removes collection by id
* DELETE /collection/_id_/_cardId_ removes card from collection

* GET /find searches for card by given params
