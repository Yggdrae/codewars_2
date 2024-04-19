# In this little assignment you are given a string of space separated numbers, 
# and have to return the highest and lowest number.

def high_and_low(numbers):
    numbers_splited = numbers.split()
    numbers_int = []
    for s in numbers_splited:
        numbers_int.append(int(s))
    return f"{max(numbers_int)}, {min(numbers_int)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
