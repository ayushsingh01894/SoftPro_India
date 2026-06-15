print_queue =[]
print_queue.append("Report.pdf")
print_queue.append("invoice.pdf")
print_queue.append("photo.png")
print(f"{len(print_queue)} Jobs waiting ")

while print_queue:
    file = print_queue.pop(0)   # Remove first item from queue beacuse sir give as instrutio its done form beg
    print(f"Now printing: {file}......   ({len(print_queue)})")

print("Queue Empty")

# for file in print_queue:
#     print(f"Now print  : ",file)

# print("Empty queue")


# def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
#     subtotal = 0

#     print("===== RECEIPT =====")

#     for name, price in items:
#         print(f"{name}: {currency}{price:.2f}")
#         subtotal += price

#     gst = subtotal * gst_percent / 100
#     grand_total = subtotal + gst

#     print("-------------------")
#     print(f"Subtotal: {currency}{subtotal:.2f}")
#     print(f"GST ({gst_percent}%): {currency}{gst:.2f}")
#     print(f"Grand Total: {currency}{grand_total:.2f}")

#     if extra:
#         print("\n--- Extra Details ---")
#         for key, value in extra.items():
#             print(f"{key}: {value}")


# # Example calls
# build_receipt(
#     ("Notebook", 120),
#     ("Pen", 20),
#     ("Bag", 850),
#     customer="Asha",
#     payment="UPI"
# )

# print()

# build_receipt(
#     ("Laptop", 55000),
#     ("Mouse", 1200),
#     gst_percent=12,
#     currency="₹",
#     customer="Rahul",
#     city="Lucknow"
# )

#task - create the total bill

# prices = {
#     "coffee": 120,
#     "juice": 100,
#     "sanwich": 150
# }

# # Order items
# order = ["coffee", "juice"]

# total_bill = 0
# print("Ordered Items:")
# for item in order:
#     if item in prices:
#         print(f"{item}: ₹{prices[item]}")
#         total_bill += prices[item]
#     else:
#         print(f"{item}: Item not found")

# print(f"\nTotal bill: ₹{total_bill}")

prices = {
    "coffee": 120,
    "juice": 100,
    "sanwich": 150
}

order = ["coffee", "juice"]

total_bill = 0

for item in order:
    total_bill += prices[item]

print("Total bill: ₹", total_bill)