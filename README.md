# Vending Machine

## Project Description

This project is a simple command-line based **Vending Machine Management System** developed in Python.

The program allows customers to view available products, search for products, and purchase items. It also provides an admin section where the administrator can add, edit, remove, and restock products.

The project is designed as a beginner-friendly Python project and demonstrates the use of dictionaries, lists, functions, loops, conditional statements, input/output, exception handling, and basic data management.

## Features

### Customer Features
- View all available items
- Search for an item
- Buy an item
- Check item price and stock
- Enter payment amount
- Calculate change automatically
- Reduce stock after a successful purchase

### Admin Features
- Admin login
- View all products
- Add a new product
- Edit product name, price, or stock
- Remove a product
- Add stock to an existing product
- Search for products
- View sales report
- View low-stock report
- Logout

## Technologies Used

- Python 3
- Command Line / Terminal
- No external Python libraries are required

## Requirements

Install **Python 3** on your computer.

You can check whether Python is installed by opening Terminal and running:

```bash
python3 --version
```

## How to Run the Project

1. Download or clone this repository.
2. Open Terminal.
3. Move into the project folder.

Example:

```bash
cd VENDING-MACHINE
```

4. Run the Python program:

```bash
python3 vending_machine.py
```

## Admin Login

Use the following details to enter the admin section:

- **Admin ID:** `admin`
- **Password:** `1234`

These credentials are included only for demonstration purposes.

## Main Menu

The main menu contains:

```text
1. Customer
2. Admin
3. Exit
```

### Customer

The customer can:

```text
1. View Items
2. Search Item
3. Buy Item
4. Exit
```

### Admin

After successful login, the admin can:

```text
1. View Items
2. Add New Item
3. Edit Item
4. Remove Item
5. Add Stock
6. Search Item
7. Sales Report
8. Low Stock Report
9. Logout
```

## Initial Products

The program starts with these products:

| No. | Product | Price | Stock |
|---:|---|---:|---:|
| 1 | Tedhe Medhe Aloo Bhujiya | ₹40 | 5 |
| 2 | Pepsi | ₹40 | 5 |
| 3 | Dairy Milk Chocolate | ₹50 | 5 |
| 4 | Nescafe Coffee Latte | ₹60 | 5 |
| 5 | Lahori Jeera | ₹40 | 5 |
| 6 | Red Bull | ₹125 | 5 |
| 7 | Monster Energy - White | ₹150 | 5 |
| 8 | Doublemint | ₹10 | 5 |

## Example Purchase

If the customer selects an item costing ₹50 and enters ₹100, the program calculates:

```text
Price  : ₹50
Money  : ₹100
Change : ₹50
```

The stock of the selected item is then reduced by one.

## Python Concepts Used

This project demonstrates:

- Variables
- Dictionaries
- Lists
- Functions
- `if`, `elif`, and `else`
- `for` and `while` loops
- `input()` and `print()`
- String formatting
- Exception handling using `try` and `except`
- Dictionary methods
- Functions with return values
- Menu-driven programming

## Project Structure

```text
VENDING-MACHINE/
│
├── vending_machine.py
└── README.md
```

## Limitations

This is a basic command-line project. The data is stored in memory, so product changes and sales information are reset when the program is closed.

A future version could use a database such as SQLite to permanently store products, users, stock, and sales.

## Future Improvements

Possible improvements include:

- SQLite database integration
- Customer accounts
- Payment gateway integration
- Receipt generation
- Date and time for transactions
- Graphical user interface
- Web-based interface
- Password hashing
- Permanent sales history

## STUDENT

**Divyansh Pal**

Python Essentials - Evaluated Course Project
