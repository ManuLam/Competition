x,s,c = int(input()), [x for x in input()], 0
m,w = 0,0

while len(s) > 0:
  if(abs(m-w) == x): break 
  if(s[0] == 'M'): m += 1
  elif(s[0] == 'W'): w += 1
  
  s.remove(s[0]); c += 1

  if(m-w == x and len(s) >= 1):
    if(s[0] == 'W'): w += 1; c+= 1; s.remove(s[0])
    elif(s[1] == 'W'): w += 1; c+= 1; s.remove(s[1])
    
  if(w-m == x and len(s) >= 1):
    if(s[0] == 'M'): m += 1; c+= 1; s.remove(s[0])
    elif(s[1] == 'M'): m += 1; c+= 1; s.remove(s[0])
  
print(c)