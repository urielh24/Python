# Variables that dont change
taxRate = 0.1025
NVShip = 9.99
NYShip = 14.99
shipping = NVShip
fees = 0.08

# Enter the amount
amount = input("Enter the amount: ")

# Total Amount Calculated
tax = float(amount) * taxRate
total = round(float(amount) + tax + shipping, 2)
print("Subtotal: " + str(total))

# 8 Percent Calculated
ebayFee = round(total * fees, 2)
print("Ebay Fees: " + str(ebayFee))

# My Payout
print("Payout: " + str(float(amount) + shipping))
payout = round(float(amount) + NYShip - ebayFee, 2)
print("Total Payout: " + str(payout))
payout = round(payout - NYShip,2)
print("Total Payout - Shipping: " + str(payout))
