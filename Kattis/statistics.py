c = 1
while True:
  try:
    n = list(map(int, input().split()))
    m = [int(x) for x in n[1:]]
    m.sort()
    print("Case %d:" % c, m[0], m[len(m)-1], (m[len(m)-1]-m[0]))
    c += 1
    
  except EOFError:
    break