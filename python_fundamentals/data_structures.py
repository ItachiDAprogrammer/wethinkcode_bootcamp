# The Tuple data structure
student_record = (1, "Charles", 23)

print(student_record[0])
print(student_record[1])
print(student_record[2])

veggies = ("mielie", "carrot")
veggies + ("potato",)

print(veggies)

tuple_constructor = tuple('I am a string in a tuple')

print(type(tuple_constructor))

cleaning_products = ("dettol", "handy andy")
# cleaning_products[1] = "jik" | Tuples do not support item assigment

# Lists
groceries = ["milk", "bread", "eggs"]

print(groceries[0])
print(groceries[1])
print(groceries[2])

print("oats" in groceries)
print("eggs" in groceries)

for item in groceries:
  print(item)


groceries[0] = "inkomazi"
print(groceries)

price_list = [
  ("bread", 17.95),
  ("eggs", 24.50),
  ("milk", 22.35)
]

for name, price in price_list:
  print(f"- Item: {name}")
  print("  Price: R{}".format(price))


# List functions(or methods)

# Append() - adds an object at the end of list
a = ["a", "b"]
x = a.append(123)
print(a)
print(x) # Returns None

a.append([1, 2, 3])
print(a)

a.append("foo")
print(a)

# Extend() - adds to end of list(args == <iterable>)
a = ["a", "b"]
a.extend([1, 2, 3]) # adds items individually
print(a)

# Insert - adds object at speccified index 
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
a.insert(3, 3.14159)
print(a)

# Remove - removes object from a list
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
a.remove("baz")
print(a)

# a.remove("Bark!")
# print(a)

# Pop - remove object from list(args <index>)
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
x = a.pop(2) # Returns item at index
y = a.pop() # Returns last items

print(x)
print(y)

a.pop(-3) # Default to -1 == .pop()
print(a)

# 