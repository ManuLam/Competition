from fractions import Fraction
import collections

n = int(input())
k = collections.Counter([Fraction(input()) for _ in range(n)]).most_common(1)[0]

print("%d/%d" % (k[0].numerator,k[0].denominator))