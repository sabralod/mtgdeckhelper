# This Python file uses the following encoding: utf-8
# This provider handle the database query's

import sqlite3

class DatabaseProvider:
    # On initialize create the database if it not exists
    def __init__(self):

        sql_user = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT)"

        sql_cards = "CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY, cardId TEXT, userId INTEGER, FOREIGN KEY(userId) REFERENCES user(id))"

        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql_user)
            con.commit()

            c.execute(sql_cards)
            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    # Add user to database
    def addUser(self, name):
        sql = "INSERT INTO user(name) VALUES (?)"

        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql, (name,))

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    # Add card to user's collection
    def addCard(self, cardName, userName):
        sql = "INSERT INTO cards(cardId, userId) VALUES (?, (SELECT id FROM user WHERE name = ?))"
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql, (cardName, userName))

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    # First delete all cards from user's collection, then delete the user itself
    def deleteUser(self, name):
        sql_cards = "DELETE FROM cards WHERE userId = (SELECT id FROM user WHERE name = ?)"
        sql_user = "DELETE FROM user WHERE name = ?"
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql_cards, (name,))

            con.commit()

            c.execute(sql_user, (name,))

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    # Delete a card from user's collection
    def deleteCard(self, cardName, userName):
        sql = "DELETE FROM cards WHERE cardId=? AND userId = (SELECT id FROM user WHERE name = ?)"
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql, (cardName, userName))

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    # Get all user's
    def getUsers(self):
        sql = "SELECT * FROM user"
        result = None
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql)
            result = c.fetchall()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

        return result

    # Get all card's from user's collection
    def getCollection(self, userName):
        sql = "SELECT c.id, c.cardId FROM user AS u JOIN cards as c ON u.id = c.userId WHERE u.name = ?"
        # sql = "SELECT c.id, c.cardId FROM cards AS c JOIN user as u ON u.id = c.userId WHERE u.name = ?"
        result = None
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()
            c.execute(sql, (userName,))
            result = c.fetchall()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

        return result
