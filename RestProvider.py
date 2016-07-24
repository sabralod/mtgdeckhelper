# This provider is an interface to the glorious "deckbrew api". Visit their developers at: https://deckbrew.com/api/
# - F

import requests, json

class RestProvider:
    def __init__(self):
        self.urlBase = "http://api.deckbrew.com/mtg/cards"



    # search for card with certain name, return card object in json
    def query(self, args):
        uri = self.urlBase + "?"

        for k,v in args.items():
            uri += k + "=" + v + "&"

        print uri[:-1]

        response = requests.get(uri[:-1])
        return response.text

    # # get all data from IDs, return list of card objects
    # def queryIDs(self, idList):
    #     result = []
    #
    #     for id in idList:
    #         response = requests.get(self.urlBase + "/" + id)
    #         result.append(FormattingUtility.getFormattedJSON(response.text))
    #
    #     return result
