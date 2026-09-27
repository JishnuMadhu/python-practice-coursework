
import sqlite3

conn = sqlite3.connect('shopping.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(20) UNIQUE,
                password TEXT,
                role VARCHAR(20)
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name VARCHAR(50) UNIQUE
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name VARCHAR(50),
                price REAL,
                stock INTEGER,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                order_date TEXT,
                status VARCHAR(20),
                total_amount REAL,
                FOREIGN KEY (user_id) REFERENCES user(id)
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS order_items(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
                )
                ''')

conn.commit()
conn.close()

print("Database created successfully")

def register():
    print("\n--- Registration ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    try:
        cursor.execute('''
                        INSERT INTO user(username, password, role)
                        VALUES(?,?,?)
                       ''', (username, password, "customer"))

        conn.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    finally:
        conn.close()


def login():
    print("\n--- Login ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT * FROM user
                    WHERE username = ? AND password = ?
                   ''', (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login successful!")
        print(f"Welcome {user[1]}")

        if user[3] == "admin":
            admin_menu()

        elif user[3] == "customer":
            customer_menu(user)

        return user

    else:
        print("Invalid username or password!")
        return None

def create_admin():
    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    try:
        cursor.execute('''
                        INSERT INTO user(username, password, role)
                        VALUES(?,?,?)
                       ''', ("admin", "admin123", "admin"))

        conn.commit()
        print("Admin account created!")

    except sqlite3.IntegrityError:
        print("Admin account already exists!")

    finally:
        conn.close()

def add_product():
    print("\n--- Add Product ---")

    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    category_id = int(input("Enter category id: "))

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    INSERT INTO products(product_name, price, stock, category_id)
                    VALUES(?,?,?,?)
                   ''',
                   (product_name, price, stock, category_id))

    conn.commit()
    conn.close()

    print("Product added successfully!")


def create_categories():
    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    INSERT OR IGNORE INTO categories(category_name)
                    VALUES(?)
                   ''', ("Electronics",))

    cursor.execute('''
                    INSERT OR IGNORE INTO categories(category_name)
                    VALUES(?)
                   ''', ("Clothing",))

    conn.commit()
    conn.close()

    print("Categories created!")


def view_products():
    print("\n--- Products ---")

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT products.id,
                           products.product_name,
                           products.price,
                           products.stock,
                           categories.category_name
                    FROM products
                    JOIN categories
                    ON products.category_id = categories.id
                   ''')

    products = cursor.fetchall()

    conn.close()

    if products:
        for product in products:
            print(f"ID: {product[0]}")
            print(f"Name: {product[1]}")
            print(f"Price: {product[2]}")
            print(f"Stock: {product[3]}")
            print(f"Category: {product[4]}")
            print("-------------------")
    else:
        print("No products available.")


def add_product():
    print("\n--- Add Product ---")

    try:
        product_name = input("Enter product name: ")

        if not product_name:
            print("Product name cannot be empty!")
            return

        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        category_id = int(input("Enter category id: "))
        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT id
                        FROM categories
                        WHERE id = ?
                       ''', (category_id,))

        category = cursor.fetchone()

        if category is None:
            print("Invalid category id!")
            conn.close()
            return
        if price < 0:
            print("Price cannot be negative!")
            return

        if stock < 0:
            print("Stock cannot be negative!")
            return

        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

        cursor.execute('''
                        INSERT INTO products(product_name, price, stock, category_id)
                        VALUES(?,?,?,?)
                       ''',
                       (product_name, price, stock, category_id))

        conn.commit()
        conn.close()

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as e:
        print("Database error:", e)

def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter product id: "))
        product_name = input("Enter new product name: ")

        if not product_name:
            print("Product name cannot be empty!")
            return

        price = float(input("Enter new price: "))
        stock = int(input("Enter new stock: "))
        category_id = int(input("Enter new category id: "))

        if price < 0:
            print("Price cannot be negative!")
            return

        if stock < 0:
            print("Stock cannot be negative!")
            return

        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

        # Check whether product exists
        cursor.execute('''
                        SELECT id
                        FROM products
                        WHERE id = ?
                       ''', (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found!")
            conn.close()
            return

        # Check whether category exists
        cursor.execute('''
                        SELECT id
                        FROM categories
                        WHERE id = ?
                       ''', (category_id,))

        category = cursor.fetchone()

        if category is None:
            print("Invalid category id!")
            conn.close()
            return

        cursor.execute('''
                        UPDATE products
                        SET product_name = ?,
                            price = ?,
                            stock = ?,
                            category_id = ?
                        WHERE id = ?
                       ''',
                       (product_name, price, stock, category_id, product_id))

        conn.commit()
        conn.close()

        print("Product updated successfully!")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_product():
    print("\n--- Delete Product ---")

    product_id = int(input("Enter product id: "))

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    DELETE FROM products
                    WHERE id = ?
                   ''', (product_id,))

    conn.commit()
    conn.close()

    print("Product deleted successfully!")



def customer_menu(user):
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Products")
        print("2. Place Order")
        print("3. View My Orders")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            place_order(user)

        elif choice == "3":
            view_my_orders(user)

        elif choice == "4":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. View All Orders")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            view_all_orders()

        elif choice == "6":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice!")



def place_order(user):
    print("\n--- Place Order ---")

    view_products()

    product_id = int(input("Enter product id: "))
    quantity = int(input("Enter quantity: "))

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT id, product_name, price, stock
                    FROM products
                    WHERE id = ?
                   ''', (product_id,))

    product = cursor.fetchone()

    if product is None:
        print("Product not found!")
        conn.close()
        return

    if quantity > product[3]:
        print("Not enough stock!")
        conn.close()
        return

    total_amount = product[2] * quantity

    cursor.execute('''
                    INSERT INTO orders(user_id, order_date, status, total_amount)
                    VALUES(?, date('now'), ?, ?)
                   ''',
                   (user[0], "Placed", total_amount))

    order_id = cursor.lastrowid

    cursor.execute('''
                    INSERT INTO order_items(order_id, product_id, quantity, price)
                    VALUES(?,?,?,?)
                   ''',
                   (order_id, product_id, quantity, product[2]))

    cursor.execute('''
                    UPDATE products
                    SET stock = stock - ?
                    WHERE id = ?
                   ''',
                   (quantity, product_id))

    conn.commit()
    conn.close()

    print("Order placed successfully!")
    print(f"Total amount: ₹{total_amount}")



def view_my_orders(user):
    print("\n--- My Orders ---")

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT id, order_date, status, total_amount
                    FROM orders
                    WHERE user_id = ?
                   ''', (user[0],))

    orders = cursor.fetchall()

    conn.close()

    if orders:
        for order in orders:
            print(f"Order ID: {order[0]}")
            print(f"Date: {order[1]}")
            print(f"Status: {order[2]}")
            print(f"Total: ₹{order[3]}")
            print("-------------------")
    else:
        print("You have no orders.")

def view_all_orders():
    print("\n--- All Orders ---")

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT orders.id,
                           user.username,
                           orders.order_date,
                           orders.status,
                           orders.total_amount
                    FROM orders
                    JOIN user
                    ON orders.user_id = user.id
                   ''')

    orders = cursor.fetchall()

    conn.close()

    if orders:
        for order in orders:
            print(f"Order ID: {order[0]}")
            print(f"Customer: {order[1]}")
            print(f"Date: {order[2]}")
            print(f"Status: {order[3]}")
            print(f"Total: ₹{order[4]}")
            print("-------------------")
    else:
        print("No orders available.")



def main():
    while True:
        print("\n==============================")
        print("   ONLINE SHOPPING SYSTEM")
        print("==============================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


main()


#test
# register()

# user = login()

# print(user)
# create_admin()
# create_categories()
# add_product()
# view_products()
# update_product()
# delete_product()
# view_products()
# customer_menu(None)
# login()
# view_all_orders()
# add_product()

