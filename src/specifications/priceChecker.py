import wfmarket
import itemHandler
import offer
# Gets item orders from market.

def getItemPrice(itemName):
    itemName = itemHandler.formatName(itemName)
    orders = wfmarket.getItemOrders(itemName).get('payload').get('orders')
    seller = lowestSeller(orders, itemName)
    buyer = highestBuyer(orders, itemName)

    print("Lowest price Seller:", seller.username, "(", seller.userID, "):", seller.platinum, "platinum")
    print("Highest price Buyer:", buyer.username, "(", buyer.userID, "):", buyer.platinum, "platinum")
    print("\n")
    print(itemName.replace("_", " ").title(), ":")
    print("/w", seller.username, "Hi! I want to buy your \"" + seller.itemname + "\", for:", seller.platinum, "platinum :)" )
    print("/w", seller.username, "Hi! I want to sell \"" + seller.itemname + "\" to YOU, for:", seller.platinum, "platinum :)" )
    print("\n")

# Returns the order of the lowest price for Sellers on the market
def lowestSeller(orders, itemName):
    lowest = 9999999
    order = {}
    for o in orders:
        if(         ( o["order_type"] == "sell")
                and ( o["visible"] ) 
                and ( o["region"] == "en" ) 
                and ( o["user"]["status"] == "ingame" )
                and ( int(o["platinum"]) < lowest )
            ):
            lowest = o["platinum"]
            order = o
    seller = offer.Offer(order["user"]["ingame_name"], str(order["user"]["id"]), itemName.replace("_", " ").title(), str(order["platinum"]))
    return seller

# Returns the order of the highest price for Buyers on the market
def highestBuyer(orders, itemName):
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
    buyer = offer.Offer(order["user"]["ingame_name"], str(order["user"]["id"]), itemName.replace("_", " ").title(), str(order["platinum"]))
    return buyer