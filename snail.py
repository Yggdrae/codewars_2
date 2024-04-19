def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]]

print(snail(arr))