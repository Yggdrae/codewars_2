# Given the string representations of two integers,
# return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
123456
123
def sum_strings(x, y):
    diff = max(len(x), len(y)) - min(len(x), len(y))
    r = ''
    resto = 0
    soma = 0
    if x == '' and y == '':
        return '0'
    for i in range(max(len(x), len(y))-1, diff-1, -1):
        soma = int(x[i])+int(y[i-diff])+resto if len(x) >= len(y) else int(x[i-diff])+int(y[i])+resto
        if soma >= 10:
            resto = 1
            soma = soma - 10 if i !=0 else "".join(s for s in str(soma)[::-1])
            r = str(soma) + r
            print(r)
        elif soma < 10:
            r = str(soma) + r
            resto = 0
            print(r)
    for i in range(diff-1, -1, -1):
        soma = int(x[i])+resto if len(x) > len(y) else int(y[i])+resto
        if soma >= 10:
                resto = 1
                soma = soma - 10 # if i !=0 else "".join(s for s in str(soma)[::-1])
                r = str(soma) + r
        elif int(soma) < 10:
             r = str(soma) + r
             resto = 0
    return r #"".join(s for s in r[::-1]) if r[len(r)-1] != "0" else "".join(s for s in r[len(r)-2::-1])


#print(sum_strings("99999999999999999", "1"))
#print(sum_strings("1001", "999"))
#print(sum_strings("11", "89"))
#print(sum_strings("1", "2"))
#print(sum_strings("123", "456789128"))
#print(sum_strings("456789128", "123"))
print(sum_strings("90", "10"))
