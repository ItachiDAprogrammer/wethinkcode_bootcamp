name = input("What is your name?")
age = int(input("What is your age?"))
age = age + 20

print(f"My name is {name}. In 20 years time I will be {age} years old.")

# A simple calculator
a = int(input("Input value A:"))
b = int(input("Input value B:"))

total = a + b
product = a * b
difference = a - b
result = a / b

print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Result: {result}")

# User defined functions
def hello():
  print("Howdy!")
  print("Howdy!!!")
  print("Hello there.")


hello()
hello()
hello()

# Def statements & parameters
def greeting(name):
  print(f"Hello {name}")


greeting("Alice")
greeting("Bob")

# Return values and return statements
import random


def getAnswer(answerNumber):
  if answerNumber == 1:
    return "It is certain"
  elif answerNumber == 2:
    return "It is decidedly so"
  elif answerNumber == 3:
    return "Yes"
  elif answerNumber == 4:
    return "Reply hazy try again"
  elif answerNumber == 5:
    return "Try again later"
  elif answerNumber == 6:
    return "Concentrate and ask again"
  elif answerNumber == 7:
    return "My reply is no"
  elif answerNumber == 8:
    return "Outlook not so good"
  elif answerNumber == 9:
    return "Very doubtful"


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1, 9)))  # Shorter version(passing function return values to another function)
