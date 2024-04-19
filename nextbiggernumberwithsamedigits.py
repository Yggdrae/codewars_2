# 4 KYU
# Create a function that takes a positive integer and returns the
# next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
import itertools

def next_bigger(n):
    num = str(n)
    listOfNums = sorted(list(set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])))
    try:
        return listOfNums[listOfNums.index(n)+1]
    except Exception:
        return 0

print(next_bigger(12))
print(next_bigger(21))
print(next_bigger(513))
print(next_bigger(2017))