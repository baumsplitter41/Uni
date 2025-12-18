#cursor.execute("DROP DATABASE IF EXISTS Shop")
#cursor.execute("CREATE DATABASE Shop")
#conn.database = "Shop"

cursor.execute("""
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT
)
""")

cursor.execute("""
CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    name VARCHAR(100),
    quantity INT
)
""")

#-----------------------------------------------------------------------#
# Seed Data 

cursor.executemany("""
INSERT INTO products (name, price, quantity)
VALUES (%s, %s, %s)
""", [
    ("Laptop", 1000.00, 10),
    ("Smartphone", 500.00, 25),
    ("Tablet", 300.00, 15),
    ("Headphones", 90.00, 50),
    ("Smartwatch", 200.00, 30)
])

#-----------------------------------------------------------------------#