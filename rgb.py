def rgb(r, g, b):
    # convert to hexadecimal
    rstr = str(hex(r)[2:])
    gstr = str(hex(g)[2:])
    bstr = str(hex(b)[2:])
    
    # account for out of range values
    if r > 255:
        rstr = str(hex(255)[2:])
    if g > 255:
        gstr = str(hex(255)[2:])
    if b > 255:
        bstr = str(hex(255)[2:])

    # account for small values
    if r < 9:
        rstr = '0' + str(hex(r)[2:])
    if g < 9:
        gstr = '0' + str(hex(g)[2:])
    if b < 9:
        bstr = '0' + str(hex(b)[2:])

    # account for out of range values   
    if r < 0:
        rstr = '0' + str(hex(0)[2:])
    if g < 0:
        gstr = '0' + str(hex(0)[2:])
    if b < 0:
        bstr = '0' + str(hex(0)[2:])

    value = rstr + gstr + bstr
    return value.upper().zfill(6)

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))

print(rgb(1,2,3))
rgb(255, 255, 255) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(0,0,0)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3
print(hex(0))

