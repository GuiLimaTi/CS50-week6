# Import get_int from CS50 library
# It ensures the user inputs a valid integer
from cs50 import get_int


# Keep asking for input until a valid height is provided
while True:
    height = get_int("Height: ")

    # Accept only values between 1 and 8 (inclusive)
    if 1 <= height <= 8:
        break  # Exit loop when input is valid


# Loop through each row of the pyramid
# Starts at 1 and goes up to the given height
for i in range(1, height + 1):

    # Calculate the number of spaces on the left
    # Example: height = 4, row = 1 → 3 spaces
    spaces = " " * (height - i)

    # Calculate the number of blocks (#)
    # Example: row 1 → 1 block, row 2 → 2 blocks
    blocks = "#" * i

    # Print the full row:
    # left spaces + left blocks + two spaces + right blocks
    print(spaces + blocks + "  " + blocks)
