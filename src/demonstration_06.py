"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    vowels = "aeiouAEIOU"
    counter = 0

    for letter in input_str:
        if letter in vowels:
            counter += 1

    return counter

print(get_count("Hello crazy world"))
print(get_count("Harry Potter and the order or the Phoenix"))