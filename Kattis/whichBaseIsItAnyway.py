for i in range(int(input())):
  a,b = input().split()
  try:
    print("%s %d %d %d" % (a, int(b,8), int(b), int(b,16)))
  except ValueError:
    print("%s %d %d %d" % (a, 0, int(b), int(b,16)))