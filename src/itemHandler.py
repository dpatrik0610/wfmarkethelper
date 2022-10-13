from unicodedata import name
import jsonHandler

def getAllItems():
    return jsonHandler.getDataFromJsonFile("jsonData/items.json").get("payload").get("items")

# Searches for an item via "base_url" in the list.
# If true: Returns the items data.
def getItemData(itemList, itemUrl):
    for item in itemList:
        if item["url_name"] == itemUrl:
            return item
    return {}

# Returns the ID of an item via "base_url" from the list.
def getItemId(itemList, itemUrl):
    for item in itemList:
        if item["url_name"] == itemUrl:
            return item["id"]
    return {}

# Imports all item data from JSON. Returns a List<> of items.
def importItems():
    itemList = list(jsonHandler.getDataFromJson("./jsonData/items.json").get("payload").get("items"))
    return itemList

def formatName(itemName):
    itemName = itemName.strip().lower()
    replaceables = {
        " "  : "_",
        "neu": "neuroptics",
        "sys": "systems",
        "cha": "chassis",
        "bp" : "blueprint",
        "rec": "receiver",
    }
    for i, j in replaceables.items():
        itemName = itemName.replace(i, j)

    if len(itemName.split("_")) >= 2: itemName = replacePrimeName(itemName.split("_"))
    print(itemName)
    return itemName

# If you type a warframe or any item's name it replaces with its own name + prime
def replacePrimeName(nameParts):
    # It searches its name from the item list.
    allItems = getAllItems()
    for item in allItems:
        splittedName = item["url_name"].split("_")
        if nameParts[0] in splittedName and nameParts[1] in splittedName:
            if nameParts[0] == splittedName[0] and nameParts[1] != splittedName[1]:
                nameParts[0] = item["url_name"].split("_")[0] + "_" + item["url_name"].split("_")[1]
            break
    return "_".join(nameParts)