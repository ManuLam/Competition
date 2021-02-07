y = int(input())

d = (2018*12)+3

ar = []

while d <= 10002*12:
  ar.append(d)
  d += 26

print('yes' if y in [int(x/12) for x in ar] else 'no')
