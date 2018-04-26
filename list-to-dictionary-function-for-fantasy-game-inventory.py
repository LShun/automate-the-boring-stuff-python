def addToInventory(inventory, addedItems):
    for i in addedItems:
      if i not in inventory:
        inventory.setdefault(i,1)
      else:
        inventory[i] = inventory[i] + 1
    return(inventory)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total = item_total + v
    print()
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)