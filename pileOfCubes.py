def find_nb(m):
    # find the number of cubes n that have a total volume of m
    # where volume is n^3 + (n-1)^3 + ... + 1^3 = m
    volume = m
    n = 0
#      reduce volume starting from the top cube
    while volume > 0:     
        volume -= (1+n)**3
        n += 1
    if volume == 0:
        return n
    else:
        return -1
        
        
print(find_nb(36))