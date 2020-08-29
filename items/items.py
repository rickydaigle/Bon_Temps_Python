#!/usr/bin/env python3

class Items:

    ITEMS = {
        "Cracklins":{"itemClass":"health", "value":10, "desc":"Restores a small amount of health.", "effect":0.15},
        "Boudin":{"itemClass":"health", "value":30, "desc":"Restores a large amount of health.", "effect":0.50},
        "Plate Lunch":{"itemClass":"health", "value":50, "desc":"Restores health to maximum value.", "effect":1}
        }

    def get_real_name(itemName):
        for each in Items.ITEMS:
            if each.lower() == itemName.lower():
                return each
        return False

    def print_desc(item):
        desc = Items.ITEMS[item]["desc"]
        return desc

    def get_class(item):
        itemClass = Items.ITEMS[item]["itemClass"]
        return itemClass
    
    def get_all_class(itemClass):
        itemNames = []
        for each in Items.ITEMS:
            if Items.ITEMS[each]["itemClass"] == itemClass:
                itemNames.append(each)
        return itemNames

    def get_shop_data(items):
        shopData = []
        if isinstance(items, list):
            for each in items:
                itemIndex = []
                itemIndex.append(each)
                itemIndex.append(Items.ITEMS[each]["value"])
                itemIndex.append(Items.ITEMS[each]["desc"])
                shopData.append(itemIndex)
        else:
            shopData.append(items)
            shopData.append(Items.ITEMS[items]["value"])
            shopData.append(Items.ITEMS[items]["desc"])
        return shopData

    def use_item(item, player):
        if Items.get_class(item) == "health":
            healFactor = Items.ITEMS[item]["effect"]
            healing = int(player.get_max_health() * healFactor)
            player.gain_health(healing)
            print("\nYou regained {} health!".format(healing))

    def get_max_lengths(shopData):
        """
        Returns the length of the longest values of name and value in the shop data list.
        @param shopData - the shop data (list of lists)
        @returns maxNameLen - the number of characters in the longest name
        @returns maxValueLen - the number of characters in the longest value
        """
        maxNameLen = 0
        maxValueLen = 0
        for each in shopData:
            if len(each[0]) > maxNameLen:
                maxNameLen = len(each[0])
            if len(str(each[1])) > maxValueLen:
                maxValueLen = len(str(each[1]))
        return maxNameLen, maxValueLen

def unit_test():

    def print_shop_format(shopData, itemJust, nameJust, valueJust):
        maxNameLen, maxValueLen = Items.get_max_lengths(shopData)
        print("#".ljust(itemJust) + "Name".ljust(maxNameLen + nameJust) + "Cost".ljust(maxValueLen + valueJust) + "Description")
        for i, each in enumerate(shopData):
            print(str(i+1).ljust(itemJust) + str(each[0]).ljust(maxNameLen + nameJust) + str(each[1]).ljust(maxValueLen + valueJust) + str(each[2]))
    
    print("Current item list:")
    for each in Items.ITEMS:
        print()
        print(str(each))
        shopData = Items.get_shop_data(each)
        print("   Name: {} | Value: {} | Description: {}".format(shopData[0], shopData[1], shopData[2]))
        print("   Item Class: {}".format(Items.get_class(each)))
        print("   Is this a health item? {}".format("health" == str(Items.get_class(each))))
    health = Items.get_all_class("health")
    itemJust = 4
    nameJust = 2
    valueJust = 4
    print("\nHealth Items:")
    for each in health:
        print(each)
    shopData = Items.get_shop_data(health)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print()
    input("Press Enter to exit test...")
             
if __name__ == "__main__":
    unit_test()
