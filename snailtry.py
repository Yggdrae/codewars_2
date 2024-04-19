
def snailsort(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results

arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]]

print(snailsort(arr))