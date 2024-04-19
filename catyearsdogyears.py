# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

def human_years_cat_years_dog_years(human_years):
    i = range(1, human_years+1)
    cat = 0
    dog = 0
    for x in i:
        if x == 1:
            cat += 15
            dog +=15
        elif x == 2:
            cat += 9
            dog += 9
        else:
            cat += 4
            dog += 5
    return [human_years, cat, dog]

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(10))