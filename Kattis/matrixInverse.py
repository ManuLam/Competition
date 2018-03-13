up = 1
while True:
  try:
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    det = 1/(a*d-b*c)
    input()
    
    print("Case %d:\n%d %d\n%d %d" % (up,det*d,det*(-b),det*(-c),det*a))
    up += 1
    
  except EOFError:
    break