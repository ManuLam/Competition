a,b = int(input()), int(input())
if (1 <= a <= 1000) and (1 <= b <= 1000):
  print(1)
elif (-1000 <= a < 0) and (1 <= b <= 1000):
  print(2)
elif (-1000 <= a < 0) and (-1000 <= b < 0):
  print(3)
else:
  print(4)