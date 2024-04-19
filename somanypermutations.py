import itertools

def permutations(s):
    return set("".join(i) for i in itertools.permutations(s, len(s)))

print(permutations('a'))
print(permutations('ab'))
print(permutations('aabb'))