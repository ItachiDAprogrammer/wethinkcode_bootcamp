my_number = 42
your_guess = 0

# The while loop
while (your_guess != my_number):
  your_input = input("Guess my number:")
  your_guess = int(your_input)

  if your_guess < my_number:
    print("Guess higher!")
  elif your_guess > my_number:
    print("Guess lower!")

print("You got it my number is: " + str(my_number))

# Looping for a fixed number of times
print("Starting...")
count = 0

while count < 10: # Repeat 10 times, stopping at 9
  print(count)
  count += 1
print("Counting complete!")

# Looping using a for loop within a function
def example_1():
  for count in range(0, 10):
    print(count)

# Count with only one param specified in range
def example_2():
  for count in range(20): 
    print(count)

# Count in increments
def example_3():
  for count in range(0, 101, 10): 
    print(count)

# Count backwards
def example_4():
  for count in range(10, 0, -1):
    print(count)

print("Starting example_1")
example_1()
print("Starting example_2")
example_2()
print("Starting example_3")
example_3()
print("Starting example_4")
example_4()

# Looping through an array/list
wordList = ['box', 'fox', 'socks']

for word in wordList:
  print(word)

# The Do While loop (below code doesn't work, as do while loops non-existent)
# x = 1

# do:
#   print("Loop Running!")
#   x -= 1
# while (x > 0)

my_guess = 7

while True: 
  user_input = input("Guess my number:")
  user_guess = int(user_input)

  if user_guess == my_guess:
    break
  
  if user_guess < my_guess:
    print("Guess higher!")
  else: 
    print("Guess lower!")

print("You guessed right, my guess is: " + str(my_guess))