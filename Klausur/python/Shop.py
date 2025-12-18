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

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    name VARCHAR(100),
    quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    name VARCHAR(100),
    quantity INT,
    purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2)
    
)
""")

def buy_products():

    global trigger
    global name
    global cursor
    global conn
    global select_quantity
    global selection

    print("Available Products:")
    cursor.execute("SELECT name, price, quantity FROM products")
    purchases = cursor.fetchall()
    if not purchases:
        print("No purchases found.")
    else:
        print(f"{'Product':<15}  {'Price':<15} {'Quantity':<10}")
        print("-" * 50)
        for row in purchases:
            print(f"{str(row[0]):<15} {str(row[1]):<15} {str(row[2]):<10}")

    while trigger.lower() == "yes":
        
        selection = input("Which Product do you want to buy? ")
        if not selection:
            print("Please select a product.")
            continue
        
        cursor.execute("SELECT name FROM products")
        product_names = [row[0] for row in cursor.fetchall()]
        
        if selection not in product_names:
            print("Product not found. Please select a valid product.")
            continue
        else:
            select_quantity = input("How many products do you want to buy? ")

        cursor.executemany("""
        INSERT INTO cart (name, name, quantity)
        VALUES (%s, %s, %s)
        """, [
            (name, selection, select_quantity)
        ])

        cursor.execute("UPDATE products SET quantity = quantity - %s WHERE name = %s", (select_quantity, selection))

        trigger = input("Do you want to buy another product? (yes/no) ").strip().lower()
        cart_func()
    conn.commit()
  


def cart_func():
    global name
    global cursor
    global trigger
    global select_quantity
    global selection

    cursor.execute("SELECT name, quantity FROM cart WHERE name = %s", (name,))
    print("Your Cart:")
    cart2 = cursor.fetchall()

    print(f"{'Product':<15} {'Quantity':<10}")
    print("-" * 30)
    for row in cart2:
        print(f"{str(row[0]):<15} {str(row[1]):<10}")

    buy = input("Do you want to proceed to buy the products in your cart? (yes/no) ").strip().lower()
    if buy == "yes":
        cursor.execute("""
        INSERT INTO purchases (name, name, quantity, purchase_date, total_price)
        SELECT c.name, c.name, c.quantity, NOW(), p.price * c.quantity
        FROM cart c
        JOIN products p ON c.name = p.name
        WHERE c.name = %s
        """, (name,))
        print("Thank you for your Purchase")
        cursor.execute("DELETE FROM cart WHERE name = %s", (name,))
        conn.commit()
    else:
        trigger2 = input("Do you want to buy another product? (yes/no) ").strip().lower()
        if trigger2 == "yes":
            trigger = "yes"
            buy_products()
        else:
            print("Purchase cancelled.")
            cursor.execute("UPDATE products SET quantity = quantity + %s WHERE name = %s", (select_quantity, selection))
            cursor.execute("DELETE FROM cart WHERE name = %s", (name,))
            conn.commit()

#-----------------------------------------------------------------------#
# name Interaction

trigger = "yes"

name = input("Enter your namename: ")
buy_products()