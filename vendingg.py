# ==========================================
#          VENDING MACHINE
# ==========================================

items = {
    1: ["Tedhe Medhe Aloo Bhujiya", 40, 5],
    2: ["Pepsi", 40, 5],
    3: ["Dairy Milk Chocolate", 50, 5],
    4: ["Nescafe Coffee Latte", 60, 5],
    5: ["Lahori Jeera", 40, 5],
    6: ["Red Bull", 125, 5],
    7: ["Monster Energy - White", 150, 5],
    8: ["Doublemint", 10, 5]
}


def view_items():
    print("\n----- AVAILABLE ITEMS -----")

    for number, item in items.items():
        print(number, ".", item[0])
        print("   Price: ₹", item[1])
        print("   Stock:", item[2])
        print()


def buy_item():
    view_items()

    choice = int(input("Enter item number: "))

    if choice not in items:
        print("Invalid item number!")
        return

    if items[choice][2] == 0:
        print("Sorry, this item is out of stock!")
        return

    print("You selected:", items[choice][0])
    print("Price: ₹", items[choice][1])

    money = int(input("Enter money: ₹"))

    if money < items[choice][1]:
        print("Not enough money!")
        return

    change = money - items[choice][1]

    items[choice][2] -= 1

    print("\nYour item:", items[choice][0])
    print("Change: ₹", change)
    print("Thank you!")


def edit_item():
    view_items()

    choice = int(input("Enter item number to edit: "))

    if choice not in items:
        print("Invalid item number!")
        return

    print("\n1. Change Name")
    print("2. Change Price")
    print("3. Change Stock")

    option = int(input("Enter choice: "))

    if option == 1:
        items[choice][0] = input("Enter new name: ")

    elif option == 2:
        items[choice][1] = int(input("Enter new price: ₹"))

    elif option == 3:
        items[choice][2] = int(input("Enter new stock: "))

    else:
        print("Invalid choice!")
        return

    print("Item updated successfully!")


def vending_machine():

    while True:

        print("\n===== VENDING MACHINE =====")
        print("1. View Items")
        print("2. Buy Item")
        print("3. Edit Item")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_items()

        elif choice == 2:
            buy_item()

        elif choice == 3:
            edit_item()

        elif choice == 4:
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice!")


vending_machine()