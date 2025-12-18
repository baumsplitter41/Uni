import mysql.connector

#-----------------------------------------------------------------------#
# Relevant System

conn = mysql.connector.connect(
    host="localhost",
    name="root",
    password=""
)
cursor = conn.cursor()

#cursor.execute("DROP DATABASE IF EXISTS Shop")
cursor.execute("CREATE DATABASE IF NOT EXISTS Shop")
conn.database = "Shop"

def add_to_stock():
    global cursor
    global conn
    trigger = "yes"

    print("Adding new products to the stock.")
    while trigger == "yes":
        
        add_product = input("What product do you want to add to your stock? ")
        add_price = input("Which price should the product have? ")
        add_quantity = input("How much products do you want to add? ")

        cursor.executemany("""
        INSERT INTO products (name, price, quantity)
        VALUES (%s, %s, %s)
        """, [
            (add_product, add_price, add_quantity)
        ])

        trigger = input("Do you want to add more Products to your range? (yes/no) ").strip().lower()
    
    print("Updated stock:")
    cursor.execute("SELECT name, price, quantity FROM products")
    products = cursor.fetchall()
    if not products:
        print("No products in stock.")
    else:
        print(f"{'Product':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for row in products:
            print(f"{str(row[0]):<20} {str(row[1]):<10} {str(row[2]):<10}")
    conn.commit()



def update_stock():
    global cursor
    global conn
    trigger2 = "yes"

    print("Adding existing products to the stock.")
    print("Available stock:")
    cursor.execute("SELECT name, price, quantity FROM products")
    products = cursor.fetchall()
    if not products:
        print("No products in stock.")
    else:
        print(f"{'Product':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for row in products:
            print(f"{str(row[0]):<20} {str(row[1]):<10} {str(row[2]):<10}")


    while trigger2 == "yes":
        update_product = input("For which product do want to update the quantity ")
        if not update_product:
            print("Please select a product.")
            continue
        
        cursor.execute("SELECT name FROM products")
        product_names = [row[0] for row in cursor.fetchall()]
        
        if update_product not in product_names:
            print("Product not found. Please select a valid product.")
            continue
        else:
            update_quantity = input("How many products do you want to add to the stock? ")
        
        cursor.execute("UPDATE products SET quantity = quantity + %s WHERE name = %s", (update_quantity, update_product))

        trigger2 = input("Do you want to update more products in your stock? (yes/no) ").strip().lower()

    print("Updated stock:")
    cursor.execute("SELECT name, price, quantity FROM products")
    products = cursor.fetchall()
    
    if not products:
        print("No products in stock.")
    else:
        print(f"{'Product':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for row in products:
            print(f"{str(row[0]):<20} {str(row[1]):<10} {str(row[2]):<10}")
    conn.commit()


def view_stock():
    global cursor
    global conn
    print("Current stock")
    print("")
    cursor.execute("SELECT name, price, quantity FROM products")
    products = cursor.fetchall()
    if not products:
        print("No products in stock.")
    else:
        print(f"{'Product':<20} {'Price':<10} {'Quantity':<10}")
        print("-" * 40)
        for row in products:
            print(f"{str(row[0]):<20} {str(row[1]):<10} {str(row[2]):<10}")

def view_purchases():
    global cursor
    print("All purchases")
    print("")
    cursor.execute("SELECT name, name, quantity, total_price, purchase_date FROM purchases ORDER BY purchase_date DESC")
    purchases = cursor.fetchall()
    if not purchases:
        print("No purchases found.")
    else:
        print(f"{'name':<15} {'Product':<15} {'Quantity':<10} {'Total Price':<15} {'Date':<25}")
        print("-" * 80)
        for row in purchases:
            print(f"{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<10} {str(row[3]):<15} {str(row[4]):<25}")

def view_carts():
    global cursor
    print("Aktive carts")
    print("")
    cursor.execute("SELECT name, name, quantity FROM cart ORDER BY name")
    purchases = cursor.fetchall()
    if not purchases:
        print("No carts found.")
    else:
        print(f"{'name':<15} {'Product':<15} {'Quantity':<10}")
        print("-" * 80)
        for row in purchases:
            print(f"{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<10}")


namename_db = "admin"
password_db = "admin"

#-----------------------------------------------------------------------#
# Seller System

print("Seller login")
print("")


namename = input("Enter your namename: ")
password = input("Enter your password: ")
action = ""

if namename == namename_db and password == password_db:
    while action != "logout":
        action = input("What do you want to do? (add, update, view stock, view purchases, view carts logout) ")
        print("")
        if action == "add":
            add_to_stock()
        elif action == "update":
            update_stock()
        elif action == "view stock":
            view_stock()
        elif action == "view purchases":
            view_purchases()
        elif action == "view carts":
            view_carts()
        elif action == "logout":
            print("Logout successfully!")
            break
        else:
            print("Use one of the displayed actions.")

else:
    print("namename oder pasword is wrong!")