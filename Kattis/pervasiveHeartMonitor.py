import re
while True:
  try:
    s,b,c = input(), [], []
    a = list(map(str, s.split()))
    
    for x in range(len(a)):
      if(re.match(r"^[0-9]", a[x])):
        b.append(float(a[x]))
      elif(not re.match(r"^[0-9]", a[x])):
        c.append(str(a[x]))
      
    y = sum(b)/len(b)
    
    print(y,' '.join(c))
  except EOFError:
    break;