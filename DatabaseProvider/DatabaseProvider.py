# This Python file uses the following encoding: utf-8

import sqlite3

class DatabaseProvider:
    connection = sqlite3.connect("magic.db")

    cursor = connection.cursor()

    sql_command = '''
    CREATE TABLE IF NOT EXISTS cards
    (id INTEGER PRIMARY KEY,
    cardId TEXT)'''

    cursor.execute(sql_command)


    def addToCollection(self, cardId):
        connection = sqlite3.connect("magic.db")
        cursor = connection.cursor()

        format_str = '''INSERT INTO cards (cardId)
            VALUES ("{cardId}")'''

        sql_command = format_str.format(cardId=cardId)

        cursor.execute(sql_command)

        #zum speichern
        connection.commit()
        connection.close()

    def getCollection(self):
        connection = sqlite3.connect("magic.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cards")
        result = cursor.fetchall()
        return result


