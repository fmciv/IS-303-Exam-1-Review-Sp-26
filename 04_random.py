# RANDOM NUMBERS

# Python uses the random module to generate random values

import random   # imports the random library


#randint(start, end)
# Generates a random integer between the two numbers
# BOTH numbers are included

number = random.randint(1, 10)

print(number)   # Could print 1-10
print(random.randint(1,10))


# randrange(start, stop, step)
# Similar to range() - Inclusive on the left, but exclusive on the right. 
# This means it includes the starting number but stops just before the ending number.

num = random.randrange(1, 10)

print(num)
print(random.randrange(1,10)) # Could print 1-9
