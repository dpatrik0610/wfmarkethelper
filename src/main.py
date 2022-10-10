import itemHandler
import jsonHandler
import wfmarket
import specifications.priceChecker as priceChecker

class Main():
    def writeOutput(data):
        file = open("./output/output.json", "w", encoding="utf8")
        file.write(jsonHandler.JsonToStr(data))
        file.close()

    def main():
        # --- TESTING ---
        # JsonHandler, wfmarket, itemhandler
        while (itemName := input("Please give an item: ")) != "exit":
            priceChecker.getItemPrice(itemName)

    if __name__ == "__main__":
        main()