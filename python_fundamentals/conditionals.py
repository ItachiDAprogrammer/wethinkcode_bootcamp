# A single if statement
name = "Zaid"

if name == "Zaid":
  print("Hello Zaid")

# An if else statement
friend = "Bob"

if friend == "Bob":
  print("Hi, Bob!")
else: 
  print("Hi, friend!")

# Multiple if else statements (with elif)
balance = 499

if balance < 500:
  print("Your balance is good, balance: R" + str(balance))
elif balance > 500: 
  print("Your balance is great, balance: R" + str(balance))
else:
  print("Your balance is running low, balance: R" + str(balance))