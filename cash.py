# Import get_float from CS50 library
# Ensures the user inputs a valid float value
from cs50 import get_float


# Keep asking the user for input until a non-negative value is provided
while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break  # Exit loop when input is valid


# Convert dollars to cents (to avoid floating-point precision issues)
cents = round(dollars * 100)

# Initialize coin counter
coins = 0


# Use as many quarters (25¢) as possible
coins += cents // 25
cents %= 25

# Use as many dimes (10¢) as possible
coins += cents // 10
cents %= 10

# Use as many nickels (5¢) as possible
coins += cents // 5
cents %= 5

# The remaining cents are pennies (1¢)
coins += cents


# Output the minimum number of coins
print(coins)
