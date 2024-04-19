# Your function takes two arguments:

# 1. current father's age (years)
# 2.current age of his son (years)
# Сalculate how many years ago the father was twice as old as 
# his son (or in how many years he will be twice as old).
# The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

def twice_as_old(dad, son):
    years = 0
    if dad > son * 2:
        while dad != son*2:
            dad -= 1
            years += 1
    else:
        while dad != son*2:
            dad += 1
            years += 1
    return years

print(twice_as_old(36, 7))
print(twice_as_old(55, 30))
print(twice_as_old(42, 21))
print(twice_as_old(22, 1))
print(twice_as_old(29, 0))