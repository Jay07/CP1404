import os


def main():
    print("Items for Hire - by Leong Chei Chau")
    NoOfItems = 0
    ItemList = []

    try:
        if os.path.exists("inventory.csv"):
            InventoryFile = open("inventory.csv", 'r')

            for Item in InventoryFile:
                Item = str(Item)
                Item = Item.split(",")
                Item[-1] = Item[-1].strip()
                ItemList.append(Item)
                NoOfItems += 1

        else:
            InventoryFile = open("inventory.csv", 'w')

        print(NoOfItems, "items loaded from inventory.csv")
        ItemList = tuple(ItemList)

        UserQuit = False
        while not UserQuit:
            print("Menu:")
            UserOption = input('''(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit
''')

            UserOption = UserOption.upper()

            if UserOption == "L":
                InventoryFile.close()
                ListItem(ItemList)

            elif UserOption == "H":
                InventoryFile.close()
                HireItem(ItemList)

            elif UserOption == "R":
                InventoryFile.close()
                ReturnItem(ItemList)

            elif UserOption == "A":
                InventoryFile.close()
                AddItem()

            elif UserOption == "Q":
                UserQuit = True
                print(NoOfItems, "items saved to inventory.csv")
                print("Have a nice day :)")
                InventoryFile.close()
                break

            else:
                print("Invalid Option")

    except IOError:
        print("Error creating or writing to file.")

def ListItem(ItemList):
    print("All items on file (* indicates item is currently out)")

    ItemNo = 0

    for Object in ItemList:
        Object = str(Object)
        Object = Object.split(",")

        ItemName = Object[0]
        ItemName = str(ItemName)
        ItemName = ItemName.strip("['")

        ItemDescription = Object[1]
        ItemDescription = str(ItemDescription)
        ItemDescription = ItemDescription.strip(" '")

        ItemCost = Object[2]
        ItemCost = str(ItemCost)
        ItemCost = ItemCost.strip(" '")

        ItemAvailbility = Object[3]
        ItemAvailbility = str(ItemAvailbility)
        ItemAvailbility = ItemAvailbility.strip(" ']")

        ItemJoint = "{} ({})".format(ItemName, ItemDescription)

        ItemCost = float(ItemCost)
        ItemCost = "{:.2f}".format(ItemCost)

        if ItemAvailbility == "in":
            ItemSign = ""
        else:
            ItemSign = "*"

        print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
        ItemNo += 1



def HireItem(ItemList):
    ItemNo = 0
    ItemNoList = []
    HireItemList = []

    try:

        for Object in ItemList:
            Object = str(Object)
            Object = Object.split(",")

            ItemName = Object[0]
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")

            ItemDescription = Object[1]
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")

            ItemCost = Object[2]
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")

            ItemAvailbility = Object[3]
            ItemAvailbility = str(ItemAvailbility)
            ItemAvailbility = ItemAvailbility.strip(" ']")

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)

            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)

            if ItemAvailbility == "in":
                ItemSign = ""
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
                ItemNoList.append(ItemNo)
                HireItemList.append(Object)
                ItemNo = ItemNo + 1
            else:
                ItemSign = "*"
                ItemNo = ItemNo + 1

        ValidHireOption = False
        while not ValidHireOption:
            HireOption = int(input("Enter the number of an item to hire: "))

            if len(HireOption) == 0:
                print("Empty input. Try again.")

            elif not HireOption.isdigit():
                print("Hire option must be a number. Try again.")

            elif not HireOption > 0:
                print("Hire option must be not be negative. Try again.")

            elif HireOption in ItemNoList:
                HiredItem = ItemList[HireOption]

                HiredItemName = HiredItem[0]
                HiredItemName = str(HiredItemName)
                HiredItemName = HiredItemName.strip("['")

                HiredItemCost = HiredItem[2]
                HiredItemCost = str(HiredItemCost)
                HiredItemCost = HiredItemCost.strip(" '")
                HiredItemCost = float(HiredItemCost)
                HiredItemCost = "{:.2f}".format(HiredItemCost)

                del HiredItem[-1]
                NewItemAvailability = "out"
                HiredItem.append(NewItemAvailability)
                print(HiredItem)

                ItemList = list(ItemList)
                ItemList[HireOption] = HiredItem
                ItemList = tuple(ItemList)

                print(ItemList)

                print("{} hired for {}".format(HiredItemName, HiredItemCost))

            else:
                print("That item is not available for hire. Try again.")

    except IOError:
        print("Error creating or writing to file.")

def ReturnItem(ItemList):
    ItemNo = 0
    ItemNoList = []
    ReturnItemList = []

    try:

        for Object in ItemList:
            Object = str(Object)
            Object = Object.split(",")

            ItemName = Object[0]
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")

            ItemDescription = Object[1]
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")

            ItemCost = Object[2]
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")

            ItemAvailbility = Object[3]
            ItemAvailbility = str(ItemAvailbility)
            ItemAvailbility = ItemAvailbility.strip(" ']")

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)

            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)

            if ItemAvailbility == "out":
                ItemSign = "*"
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
                ItemNoList.append(ItemNo)
                ReturnItemList.append(Object)
                ItemNo = ItemNo + 1
            else:
                ItemSign = ""
                ItemNo = ItemNo + 1

        ReturnOption = int(input("Enter the number of an item to hire: "))

        if ReturnOption in ItemNoList:
            ReturnItem = ItemList[ReturnOption]

            ReturnItemName = ReturnItem[0]
            ReturnItemName = str(ReturnItemName)
            ReturnItemName = ReturnItemName.strip("['")

            ReturnItemCost = ReturnItem[2]
            ReturnItemCost = str(ReturnItemCost)
            ReturnItemCost = ReturnItemCost.strip(" '")
            ReturnItemCost = float(ReturnItemCost)
            ReturnItemCost = "{:.2f}".format(ReturnItemCost)

            del ReturnItem[-1]
            NewItemAvailability = "in"
            ReturnItem.append(NewItemAvailability)
            print(ReturnItem)

            ItemList = list(ItemList)
            ItemList[ReturnOption] = ReturnItem
            ItemList = tuple(ItemList)

            print(ItemList)

            print("{} returned".format(ReturnItemName))

    except IOError:
        print("Error creating or writing to file.")

def AddItem():
    try:
        if os.path.exists("inventory.csv"):
            InventoryFile = open("inventory.csv", 'w+')
        else:
            InventoryFile = open("inventory.csv", 'w')

    except IOError:
        print("Error creating or writing to file.")

if __name__ == "__main__":
    main()