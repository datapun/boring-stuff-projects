dragonLoot = ['gold coin', 'rope', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventoryOrig = {'rope': 4, 'torch': 6, 'gold coin': 42, 'dagger': 5, 'arrow': 12}

def addToInventory(inventory, addedItems):
    print("Inventory:")
    item_total = 0
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i]+1
        else:
            inventory[i] = inventory.setdefault(i, 0) + 1
    for k,v in inventory.items():
        print(str(v)+ 'x '+ str(k))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

addToInventory(inventoryOrig,dragonLoot)


