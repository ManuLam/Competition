import sys
c = 0
a = []
for x in sys.stdin:
  if x == '\n': 
    a.append("\n")
    c = 0
    
  else:
    k = x.count('*')
    a.append('.' * (len(x)-k-c-1) + '*' * k + '.' * c)
    c += k
print('\n'.join(a))