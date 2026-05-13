# LISTS

# Lists store multiple values

fruits = ["apple", "banana", "orange"]

print(fruits)


# Accessing items
# Indexes start at 0

print(fruits[0])   # apple
print(fruits[1])   # banana


# Changing a value

fruits[1] = "grape"

print(fruits)


# Adding to a list

fruits.append("kiwi")

print(fruits)


# Length of a list

print(len(fruits))


# Looping through a list

for fruit in fruits:
    print(fruit)