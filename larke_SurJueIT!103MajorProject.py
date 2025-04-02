def display_items(items, stock):
    """Displays available items, prices, and stock levels."""
    print("\nAvailable items:")
    print("\n" + "=" * 30)
    print(" Best Buy Store ")
    print("=" * 30)

    for item, price in items.items():
        stock_level = stock[item]
        low_stock_warning = " (Low Stock!)" if stock_level < 5 else ""
        print(f"{item.capitalize()}: ${price} | Stock: {stock_level}{low_stock_warning}")

def calculate_total(cart, items):
    """Calculates subtotal, tax, and applies discounts if necessary."""
    subtotal = sum(items[item] * qty for item, qty in cart.items())
    tax = subtotal * 0.10  
    discount = 0.05 * subtotal if subtotal > 50 else 0  
    total_due = subtotal + tax - discount
    return subtotal, tax, discount, total_due

def generate_receipt(cart, items, payment, total_due):
    """Prints a formatted receipt."""
    print("\n" + "=" * 30)
    print(" Best Buy Store ")
    print("=" * 30)
    print("{:<15} {:<10} {:<10}".format("Item", "Qty", "Total"))
    for item, qty in cart.items():
        print(f"{item.capitalize():<15} {qty:<10} ${items[item] * qty:.2f}")
    
    subtotal, tax, discount, _ = calculate_total(cart, items)
    print("\nSubtotal: ${:.2f}".format(subtotal))
    print("Tax (10%): ${:.2f}".format(tax))
    if discount > 0:
        print("Discount (5%): -${:.2f}".format(discount))
    print("Total: ${:.2f}".format(total_due))
    print("Paid: ${:.2f}".format(payment))
    print("Change: ${:.2f}".format(payment - total_due))
    print("=" * 30)
    print("Thank you for shopping with us!\n")

def pos_system():
   
    items = {
          "bun": 10.0, 
          "cheese": 10.0,
          "biscuit": 2.0, 
          "lays": 5.0, 
          "ruffles": 4.0, 
          "cranberry_juice": 9.0, 
          "red_bull": 13.0, 
          "tropical_rythmn": 16.0,
          "garlic": 15.0, 
          "apple": 7.0,
          "ripe Banana": 8.0,
          "green Banana": 4.0
    } 
    stock = { 
          "bun": 20, 
          "cheese": 20,
          "biscuit": 20, 
          "lays": 20, 
          "ruffles": 20, 
          "cranberry_juice": 20, 
          "red_bull": 13.0, 
          "tropical_rythmn": 20,
          "garlic": 20, 
          "apple": 20,
          "ripe Banana": 20,
          "green Banana": 20 
    }

    while True:
        cart = {}  
        while True:
            display_items(items, stock)
            print("\nOptions: 1. Add Item  2. View Cart  3. Remove Item  4. Checkout")
            choice = input("Enter option: ")

            if choice == "1":
                item_choice = input("Enter item name: ").lower()
                if item_choice in items and stock[item_choice] > 0:
                    try:
                        qty = int(input(f"Enter quantity for {item_choice}: "))
                        if qty > 0 and qty <= stock[item_choice]:
                            cart[item_choice] = cart.get(item_choice, 0) + qty
                            stock[item_choice] -= qty
                            print(f"{qty} {item_choice}(s) added to cart.")
                        else:
                            print("Invalid quantity!")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Item not available or out of stock!")

            elif choice == "2":
                if cart:
                    print("\nYour cart:")
                    for item, qty in cart.items():
                        print(f"{item.capitalize()} x{qty}")
                else:
                    print("Cart is empty!")

            elif choice == "3":
                if cart:
                    remove_item = input("Enter item to remove: ").lower()
                    if remove_item in cart:
                        stock[remove_item] += cart.pop(remove_item)  
                        print(f"{remove_item.capitalize()} removed from cart.")
                    else:
                        print("Item not found in cart.")
                else:
                    print("Cart is empty!")

            elif choice == "4":
                if cart:
                    break
                else:
                    print("Your cart is empty!")

        
        subtotal, tax, discount, total_due = calculate_total(cart, items)
        print(f"\nTotal Amount Due: ${total_due:.2f}")
        while True:
            try:
                payment = float(input("Enter payment amount: $"))
                if payment >= total_due:
                    break
                else:
                    print("Insufficient payment!")
            except ValueError:
                print("Invalid input! Please enter a valid amount.")

        generate_receipt(cart, items, payment, total_due)

        another = input("Process another customer? (yes/no): ").lower()
        if another != "yes":
            print("Closing POS System.")
            break


pos_system()
