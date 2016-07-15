import json

#### Static utility functions for processing json information
#### -F

def getFormattedJSON(jsonString):
    return format(json.dumps(jsonString, indent=4, separators=(',', ': ')))

def format(string):
    return string.decode('string_escape')
