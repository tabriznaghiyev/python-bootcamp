cart = []

catalog = {'apple': 0.5, 'banana': 0.3, 'milk': 1.2, 'bread': 1.0, 'eggs': 2.5}


def add_item(item_name, quantity):
    if item_name in catalog:
        price = catalog[item_name]
        item = {'name': item_name, 'price': price, 'quantity': quantity, 'total': round(price * quantity, 2)}
        cart.append(item)
        print(f"Added {quantity} x {item_name} to the cart.")
    else:
        print(f"Item '{item_name}' not found in catalog")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\n--- Cart Items ---")
    for item in cart:
        print(f"{item['quantity']} x {item['name']} @ {item['price']} = {item['total']}")
    print("------------------")

def checkout():
    total=sum(item['total']for item in cart)
    print(f"\nTotal amount: ${round(total, 2)}")
    print("Thanks for shopping!")

while True:
    print("\n1. View Catalog\n2. Add to Cart\n3. View Cart\n4. Checkout & Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print("\n--- Catalog ---")
        for name, price in catalog.items():
            print(f"{name}: ${price}")
    elif choice == '2':
        item_name = input("Enter item name: ").strip().lower()
        qty = input("Enter quantity: ")
        if qty.isdigit():
            add_item(item_name, int(qty))
        else:
            print("Invalid quantity.")
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
        break
    else:
        print("Invalid option.")




