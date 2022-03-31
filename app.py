# print("Hello World!")

# age = 20
# price = 19.95
# print(age + price)

# first_name = "Uriel"
# print(first_name)

# # name = input("What is your name? ")
# # print("Hello " + name)

# birthYear = input("Enter your birth year: ")
# age = 2022 - int(birthYear)
# print(age)

#Conversion Types
int()
float()
bool()
str()

#or can use float(input("First: "))
# firstNumber = input("First: ")
# secondNumber = input("Second: ")

# #sum = firstNumber + secondNumber
# sum = float(firstNumber) + float(secondNumber)
# print("Sum: " + str(sum))

# #Python has a in operation return bool true or false
# course = 'Python is fun'
# print('Python' in course)
# # This looks like it is case sensitive

# #Python uses word for logical operator && = and || = or
# one = 2
# two = 4
# print(one > two and one < 5)

# If statements
# Python doesnt use {} just use indentation
# temperature = 25
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink lots of water")
# elif temperature > 20:
#     print("It's a nice day")
# else:
#     print("It's cold outside")
# print("Done")

#Exercise
weight = float(input("Weight: "))
option = input("(K)g or (L)bs: ")
if option.upper() == 'K':
    ans = weight / 0.45
    print("Weight in Lbs: " + str(ans))
else:
    ans = weight * 0.45
    print("Weight in Kgs: " + str(ans))