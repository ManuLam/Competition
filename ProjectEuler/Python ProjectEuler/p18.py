MAX = 0

def flood(a,r,c,s):
  global MAX
  if r > len(a)-1: return MAX

  s +=  int(a[r][c])
  if s > MAX: MAX = s

  return flood(a,r+1,c,s) and flood(a,r+1,c+1,s)

a = [x.split() for x in open('p18.txt')]
print(flood(a,0,0,0))