import math
a,c = [], 0
while True:
  try:
    c += 1
    n = int(input())
    a.append("Case %d: %d" % (c, int(1 + (n + 1) * math.log10(3) - n * math.log10(2))))

  except EOFError:
    print('\n'.join(map(str, a)))
    break