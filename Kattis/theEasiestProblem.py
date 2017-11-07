while True:
  y = int(input())
  x = list(map(int, str(y)))
  if(y == 0):
    break
  k,c = sum(x),10
  
  while True:
    c += 1
    v = y*c
    s = list(map(int, str(v)))
    if(sum(s) == k):
      print(c)
      break