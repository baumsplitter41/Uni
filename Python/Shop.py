import mysql.connector

#-----------------------------------------------------------------------#
# Relevant System

conn = mysql.connector.connect(
    host="localhost",
    user="root",
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
    user VARCHAR(100),
    name VARCHAR(100),
    quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(100),
    name VARCHAR(100),
    quantity INT,
    purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2)
    
)
""")

def buy_products():

    global trigger
    global user
    global cursor
    global conn
    global select_quantity
    global selection

    print("Available Products:")
    cursor.execute("SELECT name, price, quantity FROM products")
    for row in cursor.fetchall():
        print(row)

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
            select_quantity = input("How many product do you want to buy? ")

        cursor.executemany("""
        INSERT INTO cart (user, name, quantity)
        VALUES (%s, %s, %s)
        """, [
            (user, selection, select_quantity)
        ])

        cursor.execute("UPDATE products SET quantity = quantity - %s WHERE name = %s", (select_quantity, selection))

        trigger = input("Do you want to buy another product? (yes/no) ").strip().lower()
        cart_func()
    conn.commit()
  


def cart_func():
    global user
    global cursor
    global trigger
    global select_quantity
    global selection

    cursor.execute("SELECT name, quantity FROM cart WHERE user = %s", (user,))
    print("Your Cart:")
    for row in cursor.fetchall():
        print(row)

    buy = input("Do you want to proceed to buy the products in your cart? (yes/no) ").strip().lower()
    if buy == "yes":
        cursor.execute("""
        INSERT INTO purchases (user, name, quantity, purchase_date, total_price)
        SELECT c.user, c.name, c.quantity, NOW(), p.price * c.quantity
        FROM cart c
        JOIN products p ON c.name = p.name
        WHERE c.user = %s
        """, (user,))
        print("Thank you for your Purchase")
        cursor.execute("DELETE FROM cart WHERE user = %s", (user,))
        conn.commit()
    else:
        trigger2 = input("Do you want to buy another product? (yes/no) ").strip().lower()
        if trigger2 == "yes":
            trigger = "yes"
            buy_products()
        else:
            print("Purchase cancelled.")
            cursor.execute("UPDATE products SET quantity = quantity + %s WHERE name = %s", (select_quantity, selection))
            cursor.execute("DELETE FROM cart WHERE user = %s", (user,))
            conn.commit()


#-----------------------------------------------------------------------#
# User Interaction

trigger = "yes"
user = input("Enter your username: ")

buy_products()







