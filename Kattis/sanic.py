from math import pi

R = float(input())
r = 1
# size of big circle R minus small circle r
D = (2 * pi) * (R - r)

# dividing the difference into the smaller circle = revolutions
print(D / (2 * pi * r))

# or simply print(R-1)
