# This provider is an interface to the glorious "deckbrew api". Visit their developers at: https://deckbrew.com/api/
# - F

import requests, json

class RestProvider:
    def __init__(self):
        self.urlBase = "http://api.deckbrew.com/mtg/cards"

    # search for card with certain arguments
    def query(self, args):
        # Build url with filter arguments
        url = self.urlBase + "?"
        for k,v in args.items():
            url += k + "=" + v + "&"

        # Send request and cut the last "&"
        response = requests.get(url[:-1])
        return response.text

    # search for card with certain name and arguments
    def queryByCardName(self, name, args):
        # Build url with name and filter arguments
        url = self.urlBase + "?name=" + name + "&"
        for k,v in args.items():
            url += k + "=" + v + "&"

        # Send request and cut the last "&"
        response = requests.get(url[:-1])
        return response.text
