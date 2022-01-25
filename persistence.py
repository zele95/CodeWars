def persistence(n):
    # returns a multiplicative persistence of n 
    count = 0
    while len(str(n)) != 1:
        count += 1
        prod = 1
        for i in str(n):
            prod = prod*int(i)
        n = prod
    return count

print(persistence(999))