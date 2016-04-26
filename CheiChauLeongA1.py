#import modules
import os
import re


def main():
    # print opening statement
    print("Items for Hire - by Leong Chei Chau")

    try:
        # define list and variables
        NoOfItems = 0
        ItemList = []
        # open file fore reading
        if os.path.exists("inventory.csv"):
            InventoryFile = open("inventory.csv", 'r')
            # get elements from inventory.csv
            for Item in InventoryFile:
                Item = str(Item)
                print(Item)
                Item = Item.split(",") # split
                print(Item)
                ItemList.append(Item)
                NoOfItems += 1
                Item[-1] = Item[-1].strip()

        else:
            InventoryFile = open("inventory.csv", 'w')

        print(NoOfItems, "items loaded from inventory.csv")
        ItemList = tuple(ItemList)
        InventoryFile.close()

        UserQuit = False
        while not UserQuit:
            print("Menu:")
            UserOption = input("(L)ist all items\n"
                               "(H)ire an item\n"
                               "(R)eturn an item\n"
                               "(A)dd new item to stock\n"
                               "(Q)uit\n")

            UserOption = UserOption.upper()

            if UserOption == "L":
                LoadItem(ItemList)

            elif UserOption == "H":
                ItemList = HireItem(ItemList)

            elif UserOption == "R":
                ItemList = ReturnItem(ItemList)

            elif UserOption == "A":
                ItemList = AddItem(ItemList)

            elif UserOption == "Q":
                UserQuit = True
                Quit(ItemList)

            else:
                print("Invalid Option")

    except IOError:
        print("Error creating or writing to file.")


def LoadItem(ItemList):
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

        ItemAvailability = Object[3]
        ItemAvailability = str(ItemAvailability)
        ItemAvailability = ItemAvailability.strip(" ']")

        ItemJoint = "{} ({})".format(ItemName, ItemDescription)

        ItemCost = float(ItemCost)
        ItemCost = "{:.2f}".format(ItemCost)

        if ItemAvailability == "in":
            ItemSign = ""
        else:
            ItemSign = "*"

        print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
        ItemNo += 1


def HireItem(ItemList):
    ItemNo = 0
    NoOfHireItems = 0
    ItemNoList = []
    HireItemList = []

    try:

        for Object in ItemList:
            Object = str(Object)
            Object = Object.split(",")
            Object[-1] = Object[-1].strip()

            ItemName = Object[0]
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")

            ItemDescription = Object[1]
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")

            ItemCost = Object[2]
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")

            ItemAvailability = Object[3]
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)

            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)

            if ItemAvailability == "in":
                ItemSign = ""
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
                ItemNoList.append(ItemNo)
                HireItemList.append(Object)
                ItemNo += 1
                NoOfHireItems += 1
            else:
                ItemNo += 1

        if NoOfHireItems == 0:
            print("There are no items available for hire.")
            return ItemList

        else:
            ValidHireOption = False
            while not ValidHireOption:
                HireOption = input("Enter the number of an item to hire: ")

                if len(HireOption) == 0:
                    print("Empty input. Try again.")

                elif not HireOption.isdigit():
                    print("Hire option must be a integer larger than or equal to zero. Try again.")

                elif int(HireOption) > (ItemNo - 1):
                    print("Invalid item number. Try again.")

                elif int(HireOption) in ItemNoList:
                    ValidHireOption = True
                    HiredItem = ItemList[int(HireOption)]

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

                    ItemList = list(ItemList)
                    ItemList[int(HireOption)] = HiredItem
                    ItemList = tuple(ItemList)

                    print("{} hired for {}".format(HiredItemName, HiredItemCost))
                    return ItemList

                else:
                    print("That item is currently on hire. Try again.")

    except IOError:
        print("Error creating or writing to file.")


def ReturnItem(ItemList):
    ItemNo = 0
    NoOfReturnItems = 0
    ItemNoList = []
    ReturnItemList = []

    try:

        for Object in ItemList:
            Object = str(Object)
            Object = Object.split(",")
            Object[-1] = Object[-1].strip()

            ItemName = Object[0]
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")

            ItemDescription = Object[1]
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")

            ItemCost = Object[2]
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")

            ItemAvailability = Object[3]
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)

            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)

            if ItemAvailability == "out":
                ItemSign = "*"
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))
                ItemNoList.append(ItemNo)
                ReturnItemList.append(Object)
                ItemNo += 1
                NoOfReturnItems += 1
            else:
                ItemNo += 1

        if NoOfReturnItems == 0:
            print("No items are currently on hire.")
            return ItemList

        else:
            ValidReturnOption = False
            while not ValidReturnOption:
                ReturnOption = input("Enter the number of an item to return: ")

                if len(ReturnOption) == 0:
                    print("Empty input. Try again.")

                elif not ReturnOption.isdigit():
                    print("Return option must be an integer larger than or equal to zero. Try again.")

                elif int(ReturnOption) > (ItemNo - 1):
                    print("Invalid item number. Try again.")

                elif int(ReturnOption) in ItemNoList:
                    ValidReturnOption = True
                    ReturnItem = ItemList[int(ReturnOption)]

                    ReturnItemName = ReturnItem[0]
                    ReturnItemName = str(ReturnItemName)
                    ReturnItemName = ReturnItemName.strip("['")

                    del ReturnItem[-1]
                    NewItemAvailability = "in"
                    ReturnItem.append(NewItemAvailability)

                    ItemList = list(ItemList)
                    ItemList[int(ReturnOption)] = ReturnItem
                    ItemList = tuple(ItemList)

                    print("{} returned".format(ReturnItemName))
                    return ItemList

                else:
                    print("That item is not on hire. Try again.")

    except IOError:
        print("Error creating or writing to file.")


def AddItem(ItemList):
    AddItemList = []

    try:
        ValidItemName = False
        while not ValidItemName:
            AddItemName = input("Item Name: ")
            if len(AddItemName) == 0:
                print("Empty input. Try again.")
            else:
                ValidItemName = True
                AddItemName = AddItemName.capitalize()

        ValidItemDescription = False
        while not ValidItemDescription:
            AddItemDescription = input("Description: ")
            if len(AddItemDescription) == 0:
                print("Empty input. Try again.")
            else:
                ValidItemDescription = True
                AddItemDescription = AddItemDescription.capitalize()

        ValidItemCost = False
        ItemCostPattern = re.compile("[1-9][0-9]*\.?[0-9]*")
        while not ValidItemCost:
            AddItemCost = input("Price per day: $")
            if len(AddItemCost) == 0:
                print("Empty input. Try again.")
            elif not ItemCostPattern.match(AddItemCost):
                print("Price per day must be a number larger than or equal to zero. Try again.")
            else:
                try:
                    AddItemCost = float(AddItemCost)
                    AddItemCost = "{:.2f}".format(AddItemCost)
                    ValidItemCost = True
                except ValueError:
                    print("Invalid input. Try again.")

        AddItemAvailability = "in"

        print("{}({}), ${} now available for hire.".format(AddItemName, AddItemDescription, AddItemCost))

        AddItemList.append(AddItemName)
        AddItemList.append(AddItemDescription)
        AddItemList.append(AddItemCost)
        AddItemList.append(AddItemAvailability)

        ItemList = list(ItemList)
        ItemList.append(AddItemList)
        ItemList = tuple(ItemList)

        return ItemList

    except IOError:
        print("Error creating or writing to file.")


def Quit(ItemList):
    WriteNoOfItem = 0
    WriteData = ""

    try:
        WriteFile = open("inventory.csv", 'w')

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

            ItemAvailability = Object[3]
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")
            ItemAvailability += "\n"

            ItemData = "{},{},{},{}".format(ItemName, ItemDescription, ItemCost, ItemAvailability)

            WriteData += ItemData
            WriteNoOfItem += 1

        WriteFile.write(WriteData)
        print(WriteNoOfItem, "items saved to inventory.csv")
        print("Have a nice day :)")
        WriteFile.close()

    except IOError:
        print("Error updating file.")


if __name__ == "__main__":
    main()
