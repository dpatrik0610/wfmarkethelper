import jsonHandler

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