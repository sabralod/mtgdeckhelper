# This Python file uses the following encoding: utf-8

import sqlite3

class DatabaseProvider:
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

    def addUser(name):
        sql = "INSERT INTO user(name) VALUES (?)"

        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql, name)

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()

    def addCard(cardName, userName):
        sql = "INSERT INTO cards(cardId, userId) VALUES (?, ?)"
        sql_inner = "SELECT id FROM user WHERE name = ?"
        try:
            con = sqlite3.connect("magic.db")
            c = con.cursor()

            c.execute(sql, (cardName, c.execute(sql_inner, userName)))

            con.commit()
        except sqlite3.Error, e:
            print "sqlite error: %s" % e.args[0]
        finally:
            if con:
                con.close()
