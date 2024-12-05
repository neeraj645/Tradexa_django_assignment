
from home.models import User, Product, Order
from home.data import *
import threading


# Insert Users with Validation
def insert_users():
    for user in users_data:
        if not user["name"]:  # Name should not be empty
            print(f"Error: User ID {user['id']} has no name.")
            continue
        if User.objects.filter(email=user["email"]).exists():  # Check for duplicate emails
            print(f"Error: Email {user['email']} already exists.")
            continue
        User.objects.create(id=user["id"], name=user["name"], email=user["email"])
        print(f"User ID {user['id']} inserted successfully.")


# Insert Products with Validation
def insert_products():
    for product in products_data:
        if product["price"] <= 0:  # Price should be positive
            print(f"Error: Product ID {product['id']} has invalid price {product['price']}.")
            continue
        Product.objects.create(id=product["id"], name=product["name"], price=product["price"])
        print(f"Product ID {product['id']} inserted successfully.")


# Insert Orders with Validation
def insert_orders():
    for order in orders_data:
        if not User.objects.filter(id=order["user_id"]).exists():  # Check if User exists
            print(f"Error: User ID {order['user_id']} does not exist.")
            continue
        if not Product.objects.filter(id=order["product_id"]).exists():  # Check if Product exists
            print(f"Error: Product ID {order['product_id']} does not exist.")
            continue
        if order["quantity"] <= 0:  # Quantity should be positive
            print(f"Error: Order ID {order['id']} has invalid quantity {order['quantity']}.")
            continue
        Order.objects.create(
            id=order["id"],
            user_id=order["user_id"],
            product_id=order["product_id"],
            quantity=order["quantity"]
        )
        print(f"Order ID {order['id']} inserted successfully.")

# Create Threads
user_thread = threading.Thread(target=insert_users)
product_thread = threading.Thread(target=insert_products)
order_thread = threading.Thread(target=insert_orders)

# Start Threads
user_thread.start()
product_thread.start()
order_thread.start()

# Wait for Threads to Finish
user_thread.join()
product_thread.join()
order_thread.join()

print("All data insertion completed!")

