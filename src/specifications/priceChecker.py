import wfmarket
import itemHandler
import offer
# Gets item orders from market.

def getItemPrice(itemName):
    itemName = itemHandler.formatName(itemName)
    orders = wfmarket.getItemOrders(itemName)
    if orders is None:
        print("No item found.")
        return
    orders = orders.get('payload').get('orders')
    seller = lowestSeller(orders, itemName)
    buyer = highestBuyer(orders, itemName)

    #print("Lowest price Seller:", seller.username, "(", seller.userID, "):", seller.platinum, "platinum")
    #print("Highest price Buyer:", buyer.username, "(", buyer.userID, "):", buyer.platinum, "platinum")
    print("\n")
    itemName = itemName.replace("_", " ").title()
    print(itemName, ":")
    if seller is not None:
        print("/w", seller.username, "Hi! I want to buy your \"" + itemName + "\", for:", seller.platinum, "platinum :)" )
    else:    
        print("No user found to Buy from.")
    if buyer is not None:
        print("/w", buyer.username, "Hi! I want to sell \"" + itemName + "\" to YOU, for:", buyer.platinum, "platinum :)" )
    else:
        print("No user found to Sell to.")
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
    if len(order) == 0:
        seller = None
    else:
        seller = offer.Offer(order["user"]["ingame_name"], str(order["user"]["id"]), str(order["platinum"]))
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
    if len(order) == 0:
        buyer = None
    else:
        buyer = offer.Offer(order["user"]["ingame_name"], str(order["user"]["id"]), str(order["platinum"]))
    return buyer