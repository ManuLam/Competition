r,c,rx,cx = map(int, input().split())

for i in range(r):
  x = [str(p) for p in input()] 
  for i1 in range(rx):
    for j in range(c):
      for j1 in range(cx):
        print(x[j], end = "")
    print()      