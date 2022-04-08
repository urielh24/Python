# Gonna use this to help with shop info
months = ("January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December")

print("Please select an option: ")
print("1. Enter Deposits")
option = int(input("2. Enter Withdrawls\n"))

print(option)

if option == 1:
    amount = float(input("Enter -1 to exit\n" +
    "Enter amount: "))
    print("You entered: " + str(amount))
    while amount > 0:
        amount = float(input("Enter amount: "))
        print("Entered: " + str(amount))