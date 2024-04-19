import math

def beeramid(bonus, price):
    rng = bonus
    if bonus < price:
        return 0
    for i in range(0, int(rng)):
        if (bonus - (price*math.pow(i+1, 2))) >= 0:
            bonus = bonus - (price*math.pow(i+1, 2))
        else:
            return i

print(beeramid(9, 2)) #1
print(beeramid(10, 2)) #2
print(beeramid(11, 2)) #2
print(beeramid(21, 1.5)) #3
print(beeramid(454, 5)) #5
print(beeramid(455, 5)) #6
print(beeramid(4, 4)) #1
print(beeramid(3, 4)) #0
print(beeramid(0, 4)) #0
print(beeramid(-1, 4)) #0