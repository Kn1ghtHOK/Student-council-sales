drink1 = "Caprisun"
drink2 = "Sprite"
drink3 = "Juice"
drink4 = "Horse Urine"
drink5 = "Pond Water"
drink6 = "Blood of my Enemies"

snack1 = "Cheetoes"
snack2 = "Red Doritoes (the worse flavor)"
snack3 = "Blue Doritoes (the better flavor)"
snack4 = "Horse Poop"
snack5 = "Salt Chunks"
snack6 = "Dried Blood of my Enemies"

def main():

    file = open('data.txt', 'w+')
    file.close()

    while True:
        currentSales = loadsales()

        choice = input("Please choose:\n1. Drink\n2. Snack\nEnter your choice (1 or 2): ")

        if choice == '1':
            choiceD = input(f"Select a Drink:\n 1={drink1}\n 2={drink2}\n 3={drink3}\n 4={drink4} \n 5={drink5}\n 6={drink6}\n")
            if choiceD == '1':
                print(f"You Chose {drink1}!")
                currentSales.d1 = int(currentSales.d1) + 1

            if choiceD == '2':
                print(f"You chose {drink2}!")
                currentSales.d2 = int(currentSales.d2) + 1

            if choiceD == '3':
                print(f"You chose {drink3}!")
                currentSales.d3 = int(currentSales.d3) + 1

            if choiceD == '4':
                print(f"You chose {drink4}!")
                currentSales.d4 = int(currentSales.d4) + 1

            if choiceD == '5':
                print(f"You chose {drink5}!")
                currentSales.d5 = int(currentSales.d5) + 1

            if choiceD == '6':
                print(f"You chose {drink6}!")
                currentSales.d6 = int(currentSales.d6) + 1



        elif choice == '2':
            choiceS = input(f"Select a Snack:\n 1={snack1}\n 2={snack2}\n 3={snack3}\n 4={snack4} \n 5={snack5}\n 6={snack6}\n")

            if choiceS == '1':
                print(f"You Chose {snack1}!")
                currentSales.s1 = int(currentSales.s1) + 1

            if choiceS == '2':
                print(f"You Chose {snack2}!")
                currentSales.s2 = int(currentSales.s2) + 1

            if choiceS == '3':
                print(f"You Chose {snack3}!")
                currentSales.s3 = int(currentSales.s3) + 1

            if choiceS == '4':
                print(f"You Chose {snack4}!")
                currentSales.s4 = int(currentSales.s4) + 1

            if choiceS == '5':
                print(f"You Chose {snack5}!")
                currentSales.s5 = int(currentSales.s5) + 1

            if choiceS == '6':
                print(f"You Chose {snack6}!")
                currentSales.s6 = int(currentSales.s6) + 1



        else:
            print("Invalid choice. Please enter 1 or 2.")

        store(currentSales)

def loadsales():
    f = open('data.txt', "r")
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    for x in f:
        if x.startswith("d1"):
            d1 = x.split(" ")[1]

        if x.startswith("d2"):
            d2 = x.split(" ")[1]

        if x.startswith("d3"):
            d3 = x.split(" ")[1]

        if x.startswith("d4"):
            d4 = x.split(" ")[1]

        if x.startswith("d5"):
            d5 = x.split(" ")[1]

        if x.startswith("d6"):
            d6 = x.split(" ")[1]

    #Snacks now!!
        if x.startswith("s1"):
            s1 = x.split(" ")[1]

        if x.startswith("s2"):
            s2 = x.split(" ")[1]

        if x.startswith("s3"):
            s3 = x.split(" ")[1]

        if x.startswith("s4"):
            s4 = x.split(" ")[1]

        if x.startswith("s5"):
            s5 = x.split(" ")[1]

        if x.startswith("s6"):
            s6 = x.split(" ")[1]

    f.close()
    s = Sales
    s.d1 = d1
    s.d2 = d2
    s.d3 = d3
    s.d4 = d4
    s.d5 = d5
    s.d6 = d6
    #SNACKS!!
    s.s1 = s1
    s.s2 = s2
    s.s3 = s3
    s.s4 = s4
    s.s5 = s5
    s.s6 = s6

    return s

def store(x):
    f = open('data.txt', "w")
    f.write(f"d1 {x.d1} {drink1}\n")
    f.write(f"d2 {x.d2} {drink2}\n")
    f.write(f"d3 {x.d3} {drink3}\n")
    f.write(f"d4 {x.d4} {drink4}\n")
    f.write(f"d5 {x.d5} {drink5}\n")
    f.write(f"d6 {x.d6} {drink6}\n")
    #SNACKS!!
    f.write(f"s1 {x.s1} {snack1}\n")
    f.write(f"s2 {x.s2} {snack2}\n")
    f.write(f"s3 {x.s3} {snack3}\n")
    f.write(f"s4 {x.s4} {snack4}\n")
    f.write(f"s5 {x.s5} {snack5}\n")
    f.write(f"s6 {x.s6} {snack6}\n")

    f.close()

class Sales:
    d1 = 0


if __name__ == "__main__":
    main()
