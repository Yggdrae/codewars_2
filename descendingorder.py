# Your task is to make a function that can take any non-negative integer as an 
# argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# Example:
# 42145 --> 54421

def descending_order(num):
    numlist = [x for x in str(num)]
    return int("".join(s for s in reversed(sorted(numlist))))

print(descending_order(134265))