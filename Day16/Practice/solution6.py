coupons = [
    {"code": "SAVE10", "type": "percent", "value": 10, "min": 0},
    {"code": "SAVE25", "type": "percent", "value": 25, "min": 2000},
    {"code": "FLAT150", "type": "flat", "value": 150, "min": 800},
    {"code": "FLAT500", "type": "flat", "value": 500, "min": 3000}
]

def best_coupon(total):

    best_code = "No Coupon"
    best_discount = 0

    for coupon in coupons:
        if total < coupon["min"]:
            continue       
        if coupon["type"] == "percent":
            discount = total * coupon["value"] / 100
        else:
            discount = coupon["value"]

        if discount > total:
            discount = total
    
        if discount > best_discount:
            best_discount = discount
            best_code = coupon["code"]

    print("\nBest Coupon:", best_code)
    print(f"You Save: ₹{best_discount:.2f}")
    print(f"You Pay : ₹{total - best_discount:.2f}")

while True:
    try:
        total = float(input("\nEnter cart total: "))
        if total < 0:
            print("Total cannot be negative.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue
    best_coupon(total)
    again = input("\nCheck another total? (y/n): ").lower()
    if again == "n":
        print("Tata broh !")
        break