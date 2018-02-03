import sys
a = {}

for x in sys.stdin:
    if(x == '\n'): break
    b = x.split()
    a[b[1]] = b[0]

print('\n'.join([a.get(x[:-1], "eh") for x in sys.stdin]))