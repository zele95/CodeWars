

def count_bits(n):
    # convert to binary
    b = bin(n)
    count = 0 
    # check each digit and count ones
    for d in str(b):
        if d == '1':
            count += 1
    return count


print(count_bits(4))