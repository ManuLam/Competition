def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

for i in range(int(input())):
  a = input().split()
  print(a[0], sum([int(x, 16)*int(x, 16) for x in [x for x in baseN(int(a[2]), int(a[1]))]]))