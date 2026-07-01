cart = {}

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")

    choice = input("Choice: ").strip()

    if choice == "1":

        while True:
            name = input("Item name: ").strip()
            if name:
                break
            print("Item name cannot be empty.")

        while True:
            try:
                price = float(input("Price: ").strip())
                if price > 0:
                    break
                print("Price must be positive.")
            except ValueError:
                print("Enter a valid price.")

        while True:
            try:
                qty = int(input("Quantity: ").strip())
                if qty > 0:
                    break
                print("Quantity must be positive.")
            except ValueError:
                print("Enter a valid quantity.")

        if name in cart:
            cart[name]["qty"] += qty
        else:
            cart[name] = {
                "price": price,
                "qty": qty
            }

        print("Item added.")

    elif choice == "2":

        name = input("Item to remove: ").strip()

        if name in cart:
            del cart[name]
            print("Item removed.")
        else:
            print("Not in cart.")

    elif choice == "3":

        if not cart:
            print("Cart is empty.")
        else:
            print("\nCart:")
            for name, item in cart.items():
                amount = item["price"] * item["qty"]
                print(f"{name} x {item['qty']} = ₹{amount:.2f}")

    elif choice == "4":

        if not cart:
            print("Cart is empty.")
            continue

        subtotal = 0

        for item in cart.values():
            subtotal += item["price"] * item["qty"]

        coupon = input("Coupon (blank for none): ").strip()

        discount = 0

        if coupon == "SAVE10":
            discount = subtotal * 0.10
        elif coupon == "FLAT100" and subtotal >= 500:
            discount = 100

        taxable = subtotal - discount
        gst = taxable * 0.18
        total = taxable + gst

        print("\n BILL")
        print(f"Subtotal : ₹{subtotal:.2f}")
        print(f"Discount : ₹{discount:.2f}")
        print(f"GST 18%  : ₹{gst:.2f}")
        print(f"TOTAL    : ₹{total:.2f}")

        break

    else:
        print("Invalid choice.")
