import json

#### Static utility functions for processing json information
#### -F
def getDict(jsonString):
    return json.loads(jsonString)

def getFormattedJSON(jsonString):
    return format(json.dumps(jsonString))

def format(string):
    return string.decode('string_escape')
