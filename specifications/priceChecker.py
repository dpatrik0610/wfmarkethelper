import wfmarket
# Gets item orders from market.
def getItemPrice(itemName):
    itemName = itemName.lower()
    orders = wfmarket.getItemOrders(itemName).get('payload').get('orders')

    lowSeller = lowestSeller(orders)
    highBuyer = highestBuyer(orders)
    print("Lowest price Seller:", lowSeller["user"]["ingame_name"], "(", str(lowSeller["user"]["id"]), "):", str(lowSeller["platinum"]), "platinum")
    print("Highest price Buyer:", highBuyer["user"]["ingame_name"], "(", str(highBuyer["user"]["id"]), "):", str(highBuyer["platinum"]), "platinum")
    print("\n")
    print(itemName.replace("_", " ").title(), ":")
    print("/w", lowSeller["user"]["ingame_name"], "Hi! I want to buy your \"" + itemName.replace("_", " ").title() + "\", for:", str(lowSeller["platinum"]), "platinum :)" )
    print("/w", highBuyer["user"]["ingame_name"], "Hi! I want to sell \"" + itemName.replace("_", " ").title() + "\" to YOU, for:", str(highBuyer["platinum"]), "platinum :)" )
    print("\n")
    # TODO: return just a price, others go away.

# Returns the order of the lowest price for Sellers on the market
def lowestSeller(orders):
    lowest = 9999999
    order = {}
    for o in orders:
        if(         ( o["order_type"] == "sell")
                and ( bool(o["visible"]) ) 
                and ( o["region"] == "en" ) 
                and ( o["user"]["status"] == "ingame" )
                and ( int(o["platinum"]) < lowest )
            ):
            lowest = o["platinum"]
            order = o
    return order

# Returns the order of the highest price for Buyers on the market
def highestBuyer(orders):
    highest = 0
    order = {}
    for o in orders:
        if(         ( o["order_type"] == "buy" )
                and ( bool(o["visible"]) ) 
                and ( o["region"] == "en" ) 
                and ( o["user"]["status"] == "ingame" )
                and ( int(o["platinum"]) > highest )
            ):
            highest = o["platinum"]
            order = o
    return order