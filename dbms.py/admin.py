import sqlite3


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

        if price < 0:
            print("Price cannot be negative!")
            return

        if stock < 0:
            print("Stock cannot be negative!")
            return

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

        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

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

        product_name = input("Enter new product name: ")

        if not product_name:
            print("Product name cannot be empty!")
            conn.close()
            return

        price = float(input("Enter new price: "))
        stock = int(input("Enter new stock: "))
        category_id = int(input("Enter new category id: "))

        if price < 0:
            print("Price cannot be negative!")
            conn.close()
            return

        if stock < 0:
            print("Stock cannot be negative!")
            conn.close()
            return

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

    try:
        product_id = int(input("Enter product id: "))

        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

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

        ch = input("Are you sure you want to delete this product? (Y/N): ").lower()

        if ch == "y":
            cursor.execute('''
                            DELETE FROM products
                            WHERE id = ?
                           ''', (product_id,))

            conn.commit()
            print("Product deleted successfully!")

        else:
            print("Product not deleted!")

        conn.close()

    except ValueError:
        print("Please enter a valid product id!")

    except sqlite3.Error as e:
        print("Database error:", e)


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
            print(f"Total: Rs.{order[4]}")
            print("-------------------")
    else:
        print("No orders available.")


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
