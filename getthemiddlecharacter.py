# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character. If the word's length is even,
# return the middle 2 characters.

def get_middle(s):
    middle = int(len(s)/2)
    return "".join(s[middle-1:middle+1]) if len(s)%2==0 else s[int(len(s)/2)]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))