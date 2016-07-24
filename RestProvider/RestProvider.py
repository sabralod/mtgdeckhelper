# This provider is an interface to the glorious "deckbrew api". Visit their developers at: https://deckbrew.com/api/
# - F

import requests, FormattingUtility, json

class RestProvider:
    def __init__(self):
        self.urlBase = "http://api.deckbrew.com/mtg/cards"



    # search for card with certain name, return card object in json
    def queryName(self, query):
        response = requests.get(self.urlBase + "?name=" + query)
        return FormattingUtility.getDict(response)



    # get all data from IDs, return list of card objects
    def queryIDs(self, idList):
        result = []

        for id in idList:
            response = requests.get(self.urlBase + "/" + id)
            result.append(FormattingUtility.getDict(response.text))

        return result
