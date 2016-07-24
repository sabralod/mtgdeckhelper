import json

#### Static utility functions for processing json information
#### -F
def getDict(jsonString):
    return json.loads(jsonString)

def getFormattedJSON(data):
    # return format(json.dumps(jsonString))
    return json.dumps(data)

def format(string):
    return string.decode('string_escape')
