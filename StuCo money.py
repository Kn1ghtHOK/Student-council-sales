import time
drinks = ["sprite", "coke", "bubblr"]
snacks = ["pretzels", "chips", "popcorn"]
filename = "data.txt"

def main():
    open(filename, 'a').close()

    while True:
        sales = LoadFromFile()
        choice = input("Please choose:\n  1. Drink\n  2. Snack\n\n Enter your choice (1 or 2): \n\n")

        if choice == '1':
            drinkIndex = int(input(f"{GetPrompt(drinks)}\n"))-1
            if drinkIndex == -1:
                print("\n\nResetting Now!\n\n")
                ResetScreen()
                continue
            print(f"You chose {drinks[drinkIndex]}!\n")
            sales.drinkSales[drinkIndex] = int(sales.drinkSales[drinkIndex]) + 1
        if choice == '2':
            snackIndex = int(input(f"{GetPrompt(snacks)}\n"))-1
            if snackIndex == -1:
                print("\n\nResetting Now!\n\n")
                ResetScreen()
                continue
            print(f"You chose {snacks[snackIndex]}!\n")
            sales.snackSales[snackIndex] = int(sales.snackSales[snackIndex]) + 1
        SaveToFile(sales)
        ResetScreen()
def GetPrompt(itemList = []):
    prompt = "\n\nSelect an Item:\n\n"
    for item in itemList:
        prompt = prompt + f"  {int(itemList.index(item))+1}: {item}\n"

    prompt = prompt + "  (0 to reset)\n"
    return prompt

class Sales:
    drinkSales = [0] * 50
    snackSales = [0] * 50

def ResetScreen():
    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def LoadFromFile():
    inDrinks = True
    file = open(filename, "r")
    s = Sales
    for line in file:
        if line.startswith("DRINKS"):
            continue
        if line.startswith("SNACKS"):
            inDrinks = False
            continue

        rec = line.strip().split(" ")
        if inDrinks:
            index = drinks.index(rec[0])
            s.drinkSales[index] = rec[1].strip()
        else:
            index = snacks.index(rec[0])
            s.snackSales[index] = rec[1].strip()
    return s

def SaveToFile(sales):
    f = open(filename, "w")

    f.write("DRINKS\n")
    for idx, x in enumerate(sales.drinkSales):
        if idx < len(drinks):
            f.write(f"  {drinks[idx]} {x}\n")

    f.write("SNACKS\n")
    for idx, x in enumerate(sales.snackSales):
        if idx < len(snacks):
            f.write(f"  {snacks[idx]} {x}\n")

    f.close()

if __name__ == "__main__":
    main()
