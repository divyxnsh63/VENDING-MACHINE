# Vending Machine Project

items = {1: ["Tedhe Medhe Aloo Bhujiya",40,5],
    2: ["Pepsi",40,5],
    3: ["Dairy Milk Chocolate",50,5],
    4: ["Nescafe Coffee Latte",60,5],
    5: ["Lahori Jeera",40,5],
    6: ["Red Bull",125,5],
    7: ["Monster Energy - White",150,5],
    8: ["Doublemint",10,5]}

# admin section starts here
admin_id = "ZORO"
admin_pass = "26BAI"

sales = {"total_sales": 0,
    "total_items": 0,
    "items_sold": {}}

def admin_login():
    print("\nAdmin Login:")
    entered_id = input("Enter ID: ")
    entered_pass = input("Enter password: ")
    if entered_id == admin_id and entered_pass == admin_pass:
        print("Login successful!")
        return True
    print("Wrong ID or password!")
    return False


def show_items():
    print("\nItems available:")
    for key in items:
        item = items[key]
        print(key, item[0], "₹", item[1], "Stock:", item[2])


def find_item():
    print("\nSearch for an item:")
    search = input("Enter item name: ").lower()
    found = False
    for number, item in items.items():
        if search in item[0].lower():
            print("Item number:", number)
            print("Item:", item[0])
            print("Price: ₹", item[1])
            print("Stock:", item[2])
            found = True
    if found == False:
        print("Item not found.")


def buy_item():
    show_items()
    choice = int(input("\nEnter item number: "))

    if choice not in items:
        print("Invalid item number.")
        return
    item = items[choice]

    if item[2] <= 0:
        print("This item is out of stock.")
        return
    print("You selected:", item[0])
    print("Price: ₹", item[1])
    print("Stock:", item[2])

    money = float(input("Enter money: ₹"))

    if money < item[1]:
        print("Not enough money.")
        print("You need ₹", item[1] - money, "more.")
        return
    change = money - item[1]
    # reduce stock after buying

    item[2] = item[2] - 1
    sales["total_sales"] += item[1]
    sales["total_items"] += 1

    if item[0] in sales["items_sold"]:
        sales["items_sold"][item[0]] += 1
    else:
        sales["items_sold"][item[0]] = 1
    print("\nPurchase successful!")
    print("Item:", item[0])
    print("Price: ₹", item[1])
    print("Money: ₹", money)
    print("Change: ₹", change)
    print("Please collect your item.")

def add_stock():
    show_items()
    choice = int(input("\nEnter item number: "))

    if choice not in items:
        print("Invalid item number.")
        return
    quantity = int(input("Enter quantity to add: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    items[choice][2] += quantity
    print("Stock updated.")
    print("Item:", items[choice][0])
    print("New stock:", items[choice][2])

def edit_item():
    show_items()
    choice = int(input("\nEnter item number: "))

    if choice not in items:
        print("Invalid item number.")
        return
    print("\nCurrent details:")
    print("Name:", items[choice][0])
    print("Price:", items[choice][1])
    print("Stock:", items[choice][2])
    print("\n1. Change name")
    print("2. Change price")
    print("3. Change stock")
    print("4. Cancel")

    option = input("Enter choice: ")
    if option == "1":
        new_name = input("Enter new name: ")
        if new_name == "":
            print("Name cannot be empty.")
        else:
            items[choice][0] = new_name
            print("Name updated.")
    elif option == "2":
        new_price = float(input("Enter new price: ₹"))
        if new_price <= 0:
            print("Price must be greater than zero.")
        else:
            items[choice][1] = new_price
            print("Price updated.")
    elif option == "3":
        new_stock = int(input("Enter new stock: "))
        if new_stock < 0:
            print("Stock cannot be negative.")
        else:
            items[choice][2] = new_stock
            print("Stock updated.")
    elif option == "4":
        print("Edit cancelled.")
    else:
        print("Invalid choice.")

def add_item():
    print("\nAdd new item")
    new_number = max(items.keys()) + 1
    name = input("Enter item name: ")
    price = float(input("Enter price: ₹"))
    stock = int(input("Enter stock: "))
    items[new_number] = [name,price,stock]
    print("New item added.")
    print("Item number:", new_number)

def remove_item():
    show_items()
    choice = int(input("\nEnter item number to remove: "))
    if choice not in items:
        print("Invalid item number.")
        return
    print("You selected:", items[choice][0])
    confirm = input("Remove this item? (yes/no): ")
    if confirm.lower() == "yes":
        removed = items.pop(choice)
        print("Item removed:", removed[0])
    else:
        print("Item was not removed.")

def sales_report():
    print("\nSales report")
    print("Total items sold:", sales["total_items"])
    print("Total sales: ₹", sales["total_sales"])
    if len(sales["items_sold"]) == 0:
        print("No items sold yet.")
    else:
        for name, quantity in sales["items_sold"].items():
            print(name, ":", quantity)

def low_stock():
    print("\nLow stock items:")
    found = False
    for key in items:
        item = items[key]
        if item[2] <= 2:
            print(key, item[0], "Stock:", item[2])
            found = True
    if found == False:
        print("No low stock items.")


def customer_menu():
    while True:
        print("\nVending Machine")
        print("1. View items")
        print("2. Search item")
        print("3. Buy item")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            show_items()
        elif choice == "2":
            find_item()
        elif choice == "3":
            buy_item()
        elif choice == "4":
            print("Thank you for using the vending machine!")
            break
        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. View items")
        print("2. Add item")
        print("3. Edit item")
        print("4. Remove item")
        print("5. Add stock")
        print("6. Search item")
        print("7. Sales report")
        print("8. Low stock")
        print("9. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            show_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            edit_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            add_stock()
        elif choice == "6":
            find_item()
        elif choice == "7":
            sales_report()
        elif choice == "8":
            low_stock()
        elif choice == "9":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice.")

# main program

while True:
    print("\nWelcome to Vending Machine")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        customer_menu()
    elif choice == "2":
        if admin_login():
            admin_menu()
    elif choice == "3":
        print("Thank you for using the vending machine!")
        print("Have a great day!")
        break
    else:
        print("Invalid choice.")
