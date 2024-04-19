def opposite(number):
    return -abs(number) if number != -abs(number) else abs(number)

print(opposite(1))
print(opposite(-25.6))
print(opposite(0))
print(opposite(1425.2222))
print(opposite(-3.1458))