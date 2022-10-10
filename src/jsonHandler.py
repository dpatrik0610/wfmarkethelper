import json

# input: request BODY from web.
# Return: parsed variant of the JSON.
def getDataFromRequest(reqBody):
    parsedJson = json.loads(reqBody)
    return parsedJson

# input: name of the JSON file. 
# Returns: parsed variant of the JSON.
def getDataFromJsonFile(fileName):
    file = open(fileName, "r", encoding="utf8")
    raw = file.read()
    file.close()

    parsedJson = json.loads(raw)
    return parsedJson


# Riven's attributes
#def getAttrAt(pureData, i, attributeName):
    #return pureData[i][attributeName]