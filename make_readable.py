def make_readable(seconds):
    # takes a non-negative integer (seconds) as input and returns
    # the time in a human-readable format (HH:MM:SS)
    HMS = [seconds//3600]
    HMS.append( (seconds%3600)//60)
    HMS.append((seconds%3600)%60)
    return ':'.join(['0'+ str(i) if i<10 else str(i)  for i in HMS ])


print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

# better solution
def make_readable1(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)

print(make_readable1(60))
print(make_readable1(86399))
print(make_readable1(359999))