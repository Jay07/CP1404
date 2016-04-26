"""Name: Leong Chei Chau
Date: 26/04/2016
Brief program details: Program to open inventory.csv for reading. From the menu, user can choose to load the list of
items from the file, hire an item, return an item or add an item. When the user quits, all updates are updated into
inventory.csv
Link to GitHub: https://github.com/Jay07/CP1404
"""

# import modules
import os
import re


def main():
    """main menu function"""
    # print opening statement
    print("Items for Hire - by Leong Chei Chau")

    try:
        # initialize list and item count
        NoOfItems = 0
        ItemList = []

        if os.path.exists("inventory.csv"):  # open file for reading
            InventoryFile = open("inventory.csv", 'r')

            for Item in InventoryFile:  # get elements from inventory.csv
                Item = str(Item)
                Item = Item.split(",")  # convert each item into a list, splitting the data
                Item[-1] = Item[-1].strip()  # remove '\n'
                ItemList.append(Item)  # append each individual item list into a overall list to contain all items
                NoOfItems += 1  # increase item count

        else:  # open file for writing if it does not exist
            InventoryFile = open("inventory.csv", 'w')

        print(NoOfItems, "items loaded from inventory.csv")  # print statement
        ItemList = tuple(ItemList)  # convert list of items into a tuple
        InventoryFile.close()  # close file

        # loop for returning to menu
        UserQuit = False
        while not UserQuit:
            print("Menu:")
            # get user input
            UserOption = input("(L)ist all items\n"
                               "(H)ire an item\n"
                               "(R)eturn an item\n"
                               "(A)dd new item to stock\n"
                               "(Q)uit\n")

            try:
                UserOption = UserOption.upper()  # convert user input into uppercase

            except ValueError:  # user input is not an alphabet
                print("Input must be an alphabet. Try again.")

            if UserOption == "L":  # load item list
                LoadItem(ItemList)

            elif UserOption == "H":  # hire item
                ItemList = HireItem(ItemList)

            elif UserOption == "R":  # return item
                ItemList = ReturnItem(ItemList)

            elif UserOption == "A":  # add item
                ItemList = AddItem(ItemList)

            elif UserOption == "Q":  # quit program
                UserQuit = True
                Quit(ItemList)

            else:  # input is not valid
                print("Invalid menu choice")

    except IOError:
        print("Error creating or writing to file.")


"""
print opening statement
ItemNo = 0
for Object in ItemList
    get ItemName, ItemDescription, ItemCost, ItemAvailability
    format print statement
    ItemNo += 1
"""


def LoadItem(ItemList):
    """load item function"""
    # print opening statement
    print("All items on file (* indicates item is currently out)")

    try:
        # initialize item number
        ItemNo = 0

        for Object in ItemList:  # get individual items from list of items
            Object = str(Object)
            Object = Object.split(",")  # convert each item into a list, splitting the data

            ItemName = Object[0]  # get item name
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")  # format item name

            ItemDescription = Object[1]  # get item description
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")  # format item description

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)  # format item name and description together

            ItemCost = Object[2]  # get item cost
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")
            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)  # format item cost

            ItemAvailability = Object[3]  # get item availability
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")
            # format item availability
            if ItemAvailability == "in":
                ItemSign = ""
            else:
                ItemSign = "*"

            print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost, ItemSign))  # format print results
            ItemNo += 1  # increase item number for next item

    except IOError:
        print("Error reading or writing to file.")


"""
ItemNo = 0
NoOfHireItem = 0
ItemNoList = []
HireItemList = []
for Object in ItemList
    get ItemName, ItemDescription, ItemCost and ItemAvailability
    if ItemAvailability == 'in'
        append ItemNo to ItemNoList
        append Object to HireItemList
        ItemNo += 1
        NoOfHireItem += 1
    else
        ItemNo += 1
if NoOfHireItem = 0
    return ItemList
    print error statement
else
    get and validate HireOption
    if HireOption in ItemNoList
        HiredItem = ItemList[int(HireOption)]
        get HiredItemName and HiredItemCost
        change HiredItemAvailability from 'in' to 'out'
        update ItemList
        format print statement
        return ItemList
"""


def HireItem(ItemList):
    """hire item function"""
    try:
        # initialize list, item number and item count
        ItemNo = 0
        NoOfHireItems = 0
        ItemNoList = []
        HireItemList = []

        for Object in ItemList:  # get individual items from list of items
            Object = str(Object)
            Object = Object.split(",")
            Object[-1] = Object[-1].strip()  # convert each item into a list, splitting the data

            ItemName = Object[0]  # get item name
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")  # format item name

            ItemDescription = Object[1]  # get item description
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")  # format item description

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)  # format item name and description together

            ItemCost = Object[2]  # get item cost
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")
            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)  # format item cost

            ItemAvailability = Object[3]  # get item availability
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")
            # format item availability
            if ItemAvailability == "in":
                ItemSign = ""
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost,
                                                        ItemSign))  # print items which can be hired
                ItemNoList.append(ItemNo)  # get item numbers of items available for hire
                HireItemList.append(Object)  # get list of items available for hire
                ItemNo += 1  # increase item number for next item
                NoOfHireItems += 1  # show that there are items available for hire
            else:
                ItemNo += 1  # increase item number for next item

        if NoOfHireItems == 0:  # going back to menu when no items are available for hire
            print("There are no items available for hire.")
            return ItemList

        else:  # there are items available for hire
            # loop for error checking of hire option
            ValidHireOption = False
            while not ValidHireOption:
                HireOption = input("Enter the number of an item to hire: ")

                if len(HireOption) == 0:  # presence check
                    print("Input can not be blank.")

                elif not HireOption.isdigit():  # value check
                    print("Hire option must be a integer larger than or equal to zero. Try again.")

                elif int(HireOption) > (ItemNo - 1):  # range check
                    print("Invalid item number. Try again.")

                elif int(HireOption) in ItemNoList:  # check hire option is available for hire
                    ValidHireOption = True
                    HiredItem = ItemList[int(HireOption)]  # get item to hire

                    HiredItemName = HiredItem[0]  # get name of item to hire
                    HiredItemName = str(HiredItemName)
                    HiredItemName = HiredItemName.strip("['")  # format name of item to hire

                    HiredItemCost = HiredItem[2]  # get cost of item to hire
                    HiredItemCost = str(HiredItemCost)
                    HiredItemCost = HiredItemCost.strip(" '")
                    HiredItemCost = float(HiredItemCost)
                    HiredItemCost = "{:.2f}".format(HiredItemCost)  # format cost of item to hire

                    # change item availability from 'in' to 'out'
                    del HiredItem[-1]
                    NewItemAvailability = "out"
                    HiredItem.append(NewItemAvailability)

                    # update item in the list of items
                    ItemList = list(ItemList)
                    ItemList[int(HireOption)] = HiredItem
                    ItemList = tuple(ItemList)

                    # format print statement
                    print("{} hired for {}".format(HiredItemName, HiredItemCost))
                    # output updated list of items
                    return ItemList

                else:  # hire option is valid but item is unavailable
                    print("That item is not available for hire.")

    except IOError:
        print("Error creating or writing to file.")


def ReturnItem(ItemList):
    """return item function"""
    try:
        # initialize list, item number and item count
        ItemNo = 0
        NoOfReturnItems = 0
        ItemNoList = []
        ReturnItemList = []

        for Object in ItemList:  # get individual items from list of items
            Object = str(Object)
            Object = Object.split(",")
            Object[-1] = Object[-1].strip()  # convert each item into a list, splitting the data

            ItemName = Object[0]  # get item name
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")  # format item name

            ItemDescription = Object[1]  # get item description
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")  # format item description

            ItemJoint = "{} ({})".format(ItemName, ItemDescription)  # format item name and description together

            ItemCost = Object[2]  # get item cost
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")
            ItemCost = float(ItemCost)
            ItemCost = "{:.2f}".format(ItemCost)  # format item cost

            ItemAvailability = Object[3]  # get item availability
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")
            # format item availability
            if ItemAvailability == "out":
                ItemSign = "*"
                print("{} - {:43} = ${:>7}{:>2}".format(ItemNo, ItemJoint, ItemCost,
                                                        ItemSign))  # print items which are hired
                ItemNoList.append(ItemNo)  # get item numbers of items on hire
                ReturnItemList.append(Object)  # get list of items on hire
                ItemNo += 1  # increase item number for next item
                NoOfReturnItems += 1  # show that there are items on hire
            else:
                ItemNo += 1  # increase item number for next item

        if NoOfReturnItems == 0:  # going back to menu when there are no items on hire
            print("No items are currently on hire.")
            return ItemList

        else:  # there are items on hire
            # loop for error checking of return option
            ValidReturnOption = False
            while not ValidReturnOption:
                ReturnOption = input("Enter the number of an item to return: ")

                if len(ReturnOption) == 0:  # presence check
                    print("Input can not be blank.")

                elif not ReturnOption.isdigit():  # value check
                    print("Return option must be an integer larger than or equal to zero. Try again.")

                elif int(ReturnOption) > (ItemNo - 1):  # range check
                    print("Invalid item number. Try again.")

                elif int(ReturnOption) in ItemNoList:  # check return option is on hire
                    ValidReturnOption = True
                    ReturnItem = ItemList[int(ReturnOption)]  # get item to return

                    ReturnItemName = ReturnItem[0]  # get name of item to return
                    ReturnItemName = str(ReturnItemName)
                    ReturnItemName = ReturnItemName.strip("['")  # format name of item to return

                    # change item availability from 'out' to 'in'
                    del ReturnItem[-1]
                    NewItemAvailability = "in"
                    ReturnItem.append(NewItemAvailability)

                    # update item in the list of items
                    ItemList = list(ItemList)
                    ItemList[int(ReturnOption)] = ReturnItem
                    ItemList = tuple(ItemList)

                    # format print statement
                    print("{} returned".format(ReturnItemName))
                    # output updated list of items
                    return ItemList

                else:  # return option is valid but item is not on hire
                    print("That item is not on hire.")

    except IOError:
        print("Error creating or writing to file.")


def AddItem(ItemList):
    """add item function"""
    try:
        # initialize list
        AddItemList = []

        # loop for error checking of item name
        ValidItemName = False
        while not ValidItemName:
            AddItemName = input("Item Name: ")
            if len(AddItemName) == 0:  # presence check
                print("Input can not be blank.")
            else:
                ValidItemName = True
                AddItemName = AddItemName.capitalize()  # format item name

        # loop for error checking of item description
        ValidItemDescription = False
        while not ValidItemDescription:
            AddItemDescription = input("Description: ")
            if len(AddItemDescription) == 0:  # presence check
                print("Input can not be blank.")
            else:
                ValidItemDescription = True
                AddItemDescription = AddItemDescription.capitalize()  # format item description

        # loop for error checking of item cost
        ValidItemCost = False
        # compile pattern of item cost
        ItemCostPattern = re.compile("[1-9][0-9]*\.?[0-9]*")
        while not ValidItemCost:
            AddItemCost = input("Price per day: $")
            if len(AddItemCost) == 0:  # presence check
                print("Input can not be blank.")
            elif not ItemCostPattern.match(AddItemCost):  # validation check
                print("Price per day must be a number larger than or equal to zero. Try again.")
            else:
                try:
                    AddItemCost = float(AddItemCost)
                    AddItemCost = "{:.2f}".format(AddItemCost)  # format item cost
                    ValidItemCost = True
                except ValueError:
                    print("Invalid input. Try again.")

        # auto update of item availability
        AddItemAvailability = "in"

        # format print statement
        print("{}({}), ${} now available for hire.".format(AddItemName, AddItemDescription, AddItemCost))

        # create an individual item list composing of its data
        AddItemList.append(AddItemName)
        AddItemList.append(AddItemDescription)
        AddItemList.append(AddItemCost)
        AddItemList.append(AddItemAvailability)

        # append individual item list to the list of all items
        ItemList = list(ItemList)
        ItemList.append(AddItemList)
        ItemList = tuple(ItemList)

        # output updated list of items
        return ItemList

    except IOError:
        print("Error creating or writing to file.")


def Quit(ItemList):
    """quit program and update function"""
    try:
        # initialize item count and output format
        WriteNoOfItem = 0
        WriteData = ""

        # open and clear file for writing
        WriteFile = open("inventory.csv", 'w')

        for Object in ItemList:  # get individual items from list of items
            Object = str(Object)
            Object = Object.split(",")  # convert each item into a list, splitting the data

            ItemName = Object[0]  # get item name
            ItemName = str(ItemName)
            ItemName = ItemName.strip("['")  # format item name

            ItemDescription = Object[1]  # get item description
            ItemDescription = str(ItemDescription)
            ItemDescription = ItemDescription.strip(" '")  # format item description

            ItemCost = Object[2]  # get item cost
            ItemCost = str(ItemCost)
            ItemCost = ItemCost.strip(" '")  # format item cost

            ItemAvailability = Object[3]  # get item availability
            ItemAvailability = str(ItemAvailability)
            ItemAvailability = ItemAvailability.strip(" ']")
            ItemAvailability += "\n"  # format item availability

            ItemData = "{},{},{},{}".format(ItemName, ItemDescription, ItemCost,
                                            ItemAvailability)  # format item as a string

            WriteData += ItemData  # add all items for output into a single string
            WriteNoOfItem += 1  # increase item count

        WriteFile.write(WriteData)  # write data to file
        print(WriteNoOfItem, "items saved to inventory.csv")  # print number of items saved
        print("Have a nice day :)")  # print statement
        WriteFile.close()  # close file

    except IOError:
        print("Error updating file.")


# main
if __name__ == "__main__":
    main()
