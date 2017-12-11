a,k = [],0
while True:
  try:
    a.append(len(input()))
    
  except EOFError:
    for i in range(len(a)-1):
      k += (max(a) - a[i])**2
    print(k)
    
    break