from cs50 import get_string

# Ask the user for a text
text = get_string("Text: ")

# Counters
letters = 0
words = 1
sentences = 0

# Count letters, words, and sentences
for char in text:
    if char.isalpha():
        letters += 1
    elif char == " ":
        words += 1
    elif char == "." or char == "!" or char == "?":
        sentences += 1

# Average number of letters and sentences per 100 words
L = (letters / words) * 100
S = (sentences / words) * 100

# Coleman-Liau index
index = round(0.0588 * L - 0.296 * S - 15.8)

# Print result
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
