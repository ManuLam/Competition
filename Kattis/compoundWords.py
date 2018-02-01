a,b = [], set()

while True:
  try:
    a.extend(input().split())
    
  except EOFError:
    for i in range(len(a)):
      for j in range(len(a)):
        if(i != j):
          b.add(a[i]+a[j])
    b = sorted(b)
    print('\n'.join(b))
    break