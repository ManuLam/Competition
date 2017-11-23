for i in range(int(input())):
  n,m = map(int, input().split())
  c = []
  for j in range(n):
    c.append(input()[::-1])
    
  c.reverse()
  print("Test %d" % (i+1))
  print("\n".join(c))