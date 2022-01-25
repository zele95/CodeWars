def xo(s):
    # check if a string has the same number of x and o
    countx = 0
    counto = 0
    for c in s.lower():
        if c == 'x':
            countx += 1
        elif c == 'o':
            counto += 1
    return True if counto == countx else False
    # return s.count('x') == s.count('o')


print(xo('xxoo'))