import requests
import jsonHandler

def baseURL():
    return "https://api.warframe.market/v1/"

# Constructs any URL with a custom path, parameters and heads.
def constructURL(path, item, path2, headers, parameters):
    link = baseURL() + path
    if (item != ""):
        link += "/" + item
    if(path2 != ""):
        link += "/" + path2
    return [link, parameters, headers]

# This connects to wfmarket's orders and searches for the given "item" in param.
# ex: https://api.warframe.market/v1/items/mirage_prime_systems/orders
def getItemOrders(itemName):
    url = constructURL("items", itemName, "orders", {'accept' : 'application.json', 'Platform': 'pc'}, {})
    req = getRequest(url)
    res = getBodyJSON(req)
    # TODO: Wrong item name handler.
    return res

# Gets the whole list of items on the site. 
def getItemList():
    myRequest = getRequest(constructURL("items", "", "", {'accept' : 'application.json', 'Platform': 'pc'}, {}))
    if getStatusCode(myRequest) != 200:
        print(myRequest.status_code)
    
    itemList = list(jsonHandler.getDataFromRequest(myRequest.text).get("payload").get("items"))
    return itemList

# Returns the response from the basic request types.
def getRequest(constructedURL):
    return requests.get(constructedURL[0], params=constructedURL[1], headers=constructedURL[2])

def postRequest(link):
    return requests.post(link)
    # TODO
    
def putRequest(link):
    return requests.put(link)
    # TODO

# Gets the status code from the response.
def getStatusCode(response):
    return response.status_code

# Gives back the JSON / Text from of the response
def getBodyJSON(response):
    return response.json()

def getBodyText(response):
    return response.text