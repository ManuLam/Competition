while True:
  a,b = map(int, input().split())
  if a == 0 and b == 0:
    break
  m = int(a/b)
  n = int(a%b)
  print(m, n, "/", b)