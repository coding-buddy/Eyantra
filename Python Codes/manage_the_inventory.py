def add_item(item, quantity):
    if item in items:
        ind = items.index(item)
        q = quantities[ind]
        q = q+quantity
        quantities[ind] = q
        print(f"UPDATED Item {item}")
    else:
        items.append(item)
        quantities.append(quantity)
        print(f"ADDED Item {item}")

def delete_item(item, quantity):
    if item not in items:
        print(f"Item {item} does not exist")
    else:
        ind = items.index(item)
        q = quantities[ind]
        if int(q)<quantity:
            print(f"Item {item} could not be DELETED")
        else:
            q = q-quantity
            quantities[ind] = q
            print(f"DELETED Item {item}")


test_cases = int(input())
for case in range(test_cases):

    items = []
    quantities = []

    no_of_items = int(input())
    for i in range(no_of_items):
        item, quantity = input().split(" ")
        items.append(item)
        quantities.append(int(quantity))
    
    no_of_operations = int(input())
    for i in range(no_of_operations):
        query = input()
        operation, item, quantity = query.split(" ")
        if operation == "ADD":
            add_item(item, int(quantity))
        elif operation == "DELETE":
            delete_item(item, int(quantity))

    print("Total Items in Inventory:", sum(quantities))