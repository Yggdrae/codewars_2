# Given two integers a and b, which can be positive or negative, 
# find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    if a == b:
        return a
    sum = 0
    for x in range(a if a < b else b, b+1 if a < b else a+1 ):
        sum += x
    return sum

print(get_sum(1, 5))
print(get_sum(0, -1))