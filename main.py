import itemHandler
import jsonHandler
import wfmarket
import specifications.priceChecker as priceChecker

def writeOutput(data):
    file = open("./output/output.json", "w", encoding="utf8")
    file.write(jsonHandler.JsonToStr(data))
    file.close()

def main():
    # --- TESTING ---
    # JsonHandler, wfmarket, itemhandler
    #print("High noon's ID: ", itemHandler.getItemId(wfmarket.getItemList(), "high_noon"))

    priceChecker.getItemPrice("equilibrium")

if __name__ == "__main__":
    main()