#Used libraries:

##Flask for Restful Service
Creating a restful interface for our frontend application
http://flask.pocoo.org/docs/0.11/quickstart/

##Python Json
Encoding and decoding python objects and tuples to json
https://docs.python.org/2.7/library/json.html

##sqlite3
Save and load user's data with a database
https://docs.python.org/2/library/sqlite3.html

##Rest Routes
* GET /find - Find cards with optional filter arguments
* POST /user - Add user to database
* DELETE /user - Delete user in database
* POST /user/{username}/card - Add card to user's collection
* GET /user/{username}/cards - Get all cards from user's collection with optional filter arguments
* DELETE /user/{username}/card/{cardname} - Delete a card from user's collection
* GET /users - Get all users - mostly used for testing
