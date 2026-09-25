# ==========================================================
#                 VENDING MACHINE PROJECT
# ==========================================================

# All items are stored as:
# item number : [item name, price, stock]
# ==========================================================

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


# ==========================================================
#                    ADMIN LOGIN
# ==========================================================

admin_id = "admin"
admin_password = "1234"


def admin_login():

    print("\n================================")
    print("          ADMIN LOGIN")
    print("================================")

    user_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")

    if user_id == admin_id and password == admin_password:
        print("\nLogin successful!")
        return True

    else:
        print("\nWrong ID or Password!")
        return False


# ==========================================================
#                    VIEW ITEMS
# ==========================================================

def view_items():

    print("\n==============================================")
    print("              AVAILABLE ITEMS")
    print("==============================================")

    print("No.\tItem\t\t\t\tPrice\tStock")
    print("----------------------------------------------")

    for number, item in items.items():

        name = item[0]
        price = item[1]
        stock = item[2]

        print(number, "\t", name, "\t₹", price, "\t", stock)

    print("----------------------------------------------")


# ==========================================================
#                    SEARCH ITEM
# ==========================================================

def search_item():

    print("\n================================")
    print("          SEARCH ITEM")
    print("================================")

    search = input("Enter item name to search: ").lower()

    found = False

    for number, item in items.items():

        name = item[0]

        if search in name.lower():

            print("\nItem Found!")
            print("Item Number :", number)
            print("Item Name   :", name)
            print("Price       : ₹", item[1])
            print("Stock       :", item[2])

            found = True

    if found == False:
        print("\nItem not found.")


# ==========================================================
#                    BUY ITEM
# ==========================================================

def buy_item():

    view_items()

    try:
        choice = int(input("\nEnter item number: "))

    except ValueError:
        print("Please enter a number.")
        return

    if choice not in items:

        print("Invalid item number.")
        return

    name = items[choice][0]
    price = items[choice][1]
    stock = items[choice][2]

    if stock <= 0:

        print("\nSorry! This item is out of stock.")
        return

    print("\nYou selected:", name)
    print("Price: ₹", price)
    print("Available stock:", stock)

    try:
        money = float(input("Enter money: ₹"))

    except ValueError:
        print("Please enter a valid amount.")
        return

    if money < price:

        remaining = price - money

        print("\nNot enough money!")
        print("You need ₹", remaining, "more.")

        return

    # Calculate change
    change = money - price

    # Reduce stock
    items[choice][2] -= 1

    # Increase sales information
    sales["total_sales"] += price
    sales["total_items"] += 1

    if name in sales["items_sold"]:
        sales["items_sold"][name] += 1

    else:
        sales["items_sold"][name] = 1

    print("\n================================")
    print("       PURCHASE SUCCESSFUL")
    print("================================")

    print("Item      :", name)
    print("Price     : ₹", price)
    print("Money     : ₹", money)
    print("Change    : ₹", change)

    print("\nThank you for your purchase!")
    print("Please collect your item.")


# ==========================================================
#                    ADD STOCK
# ==========================================================

def add_stock():

    view_items()

    try:
        choice = int(input("\nEnter item number: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice not in items:

        print("Invalid item number.")
        return

    try:
        quantity = int(input("Enter quantity to add: "))

    except ValueError:
        print("Please enter a valid quantity.")
        return

    if quantity <= 0:

        print("Quantity must be greater than zero.")
        return

    items[choice][2] += quantity

    print("\nStock updated successfully!")
    print("Item:", items[choice][0])
    print("New Stock:", items[choice][2])


# ==========================================================
#                    EDIT ITEM
# ==========================================================

def edit_item():

    view_items()

    try:
        choice = int(input("\nEnter item number to edit: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice not in items:

        print("Invalid item number.")
        return

    print("\nCurrent item details:")
    print("Name :", items[choice][0])
    print("Price:", items[choice][1])
    print("Stock:", items[choice][2])

    print("\nWhat do you want to edit?")
    print("1. Item Name")
    print("2. Item Price")
    print("3. Item Stock")
    print("4. Cancel")

    option = input("Enter your choice: ")

    if option == "1":

        new_name = input("Enter new item name: ")

        if new_name == "":
            print("Item name cannot be empty.")

        else:
            items[choice][0] = new_name
            print("Item name updated successfully.")

    elif option == "2":

        try:
            new_price = float(input("Enter new price: ₹"))

            if new_price <= 0:
                print("Price must be greater than zero.")

            else:
                items[choice][1] = new_price
                print("Price updated successfully.")

        except ValueError:
            print("Please enter a valid price.")

    elif option == "3":

        try:
            new_stock = int(input("Enter new stock: "))

            if new_stock < 0:
                print("Stock cannot be negative.")

            else:
                items[choice][2] = new_stock
                print("Stock updated successfully.")

        except ValueError:
            print("Please enter a valid number.")

    elif option == "4":

        print("Edit cancelled.")

    else:

        print("Invalid choice.")


# ==========================================================
#                    ADD NEW ITEM
# ==========================================================

def add_item():

    print("\n================================")
    print("           ADD NEW ITEM")
    print("================================")

    new_number = max(items.keys()) + 1

    name = input("Enter item name: ")

    if name == "":
        print("Item name cannot be empty.")
        return

    try:
        price = float(input("Enter item price: ₹"))
        stock = int(input("Enter item stock: "))

    except ValueError:
        print("Please enter valid values.")
        return

    if price <= 0:

        print("Price must be greater than zero.")
        return

    if stock < 0:

        print("Stock cannot be negative.")
        return

    items[new_number] = [name, price, stock]

    print("\nNew item added successfully!")
    print("Item Number:", new_number)
    print("Item Name:", name)
    print("Price: ₹", price)
    print("Stock:", stock)


# ==========================================================
#                    REMOVE ITEM
# ==========================================================

def remove_item():

    view_items()

    try:
        choice = int(input("\nEnter item number to remove: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice not in items:

        print("Invalid item number.")
        return

    print("\nYou selected:", items[choice][0])

    confirm = input("Are you sure you want to remove this item? (yes/no): ")

    if confirm.lower() == "yes":

        removed_item = items.pop(choice)

        print("\nItem removed successfully!")
        print("Removed:", removed_item[0])

    else:

        print("Item was not removed.")


# ==========================================================
#                    SALES INFORMATION
# ==========================================================

sales = {
    "total_sales": 0,
    "total_items": 0,
    "items_sold": {}
}


# ==========================================================
#                    SALES REPORT
# ==========================================================

def sales_report():

    print("\n================================")
    print("           SALES REPORT")
    print("================================")

    print("Total Items Sold :", sales["total_items"])
    print("Total Sales      : ₹", sales["total_sales"])

    print("\nItems Sold:")

    if len(sales["items_sold"]) == 0:

        print("No items have been sold yet.")

    else:

        for name, quantity in sales["items_sold"].items():

            print(name, ":", quantity)


# ==========================================================
#                    LOW STOCK REPORT
# ==========================================================

def low_stock_report():

    print("\n================================")
    print("         LOW STOCK ITEMS")
    print("================================")

    found = False

    for number, item in items.items():

        if item[2] <= 2:

            print(number, "-", item[0],
                  "| Stock:", item[2])

            found = True

    if found == False:

        print("There are no low-stock items.")


# ==========================================================
#                    USER MENU
# ==========================================================

def user_menu():

    while True:

        print("\n================================")
        print("         VENDING MACHINE")
        print("================================")

        print("1. View Items")
        print("2. Search Item")
        print("3. Buy Item")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            view_items()

        elif choice == "2":

            search_item()

        elif choice == "3":

            buy_item()

        elif choice == "4":

            print("\nThank you for using the vending machine!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================================
#                    ADMIN MENU
# ==========================================================

def admin_menu():

    while True:

        print("\n================================")
        print("            ADMIN MENU")
        print("================================")

        print("1. View Items")
        print("2. Add New Item")
        print("3. Edit Item")
        print("4. Remove Item")
        print("5. Add Stock")
        print("6. Search Item")
        print("7. Sales Report")
        print("8. Low Stock Report")
        print("9. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            view_items()

        elif choice == "2":

            add_item()

        elif choice == "3":

            edit_item()

        elif choice == "4":

            remove_item()

        elif choice == "5":

            add_stock()

        elif choice == "6":

            search_item()

        elif choice == "7":

            sales_report()

        elif choice == "8":

            low_stock_report()

        elif choice == "9":

            print("\nAdmin logged out.")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================================
#                    MAIN PROGRAM
# ==========================================================

while True:

    print("\n==========================================")
    print("           WELCOME TO VENDING MACHINE")
    print("==========================================")

    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        user_menu()

    elif choice == "2":

        if admin_login():

            admin_menu()

    elif choice == "3":

        print("\nThank you for using our vending machine!")
        print("Have a great day!")
        break

    else:

        print("\nInvalid choice. Please select 1, 2 or 3.")
