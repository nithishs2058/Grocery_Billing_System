print(" Welcome to EASY MART ")

n = int(input("Enter number of items: "))
total = 0

print("Enter Item Details")

for i in range(1, n + 1):

    print(f"Item {i}")

    item = input("Item Name: ")
    price = float(input("Price(₹): "))
    qty = int(input("Quantity: "))

    amount = price * qty
    total += amount

    print(f"{item} Total = ₹{amount:.2f}")

print(" BILL ")

print(f"Sub Total: ₹{total:.2f}")


discount = 0

if total >= 5000:
    discount = total * 0.15   
elif total >= 3000:
    discount = total * 0.10   
elif total >= 1000:
    discount = total * 0.05  

final_amount = total - discount

print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")

print("-" * 40)
print(" Thank You for Shopping at EASY MART ")
print(" Visit Again! ")