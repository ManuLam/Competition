fname,names = {}, []

while True:
  try:
    s = input()
    if(s.split()[0] not in  fname):  fname[s.split()[0]] = False
    else: fname[s.split()[0]] = True
    names.append(s)
    
  except EOFError:
    names.sort(key = lambda x: x.split()[1] + x.split()[0])
    
    for i in names:
      if(fname.get(i.split()[0]) == True):
        print(i)
            
      else:
        print(i.split()[0])
        
    break