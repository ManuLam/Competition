aR = []
k = {'entry':'entered','exit':'exited'}

for i in range(int(input())):
  s = input()
  a,n = s.split()
  
  if(n in aR and a!= 'exit'):
    print("%s %s (ANOMALY)" % (n, k.get(a)))
  elif(s not in aR and a != 'exit'):
    aR.append(n)
    print("%s %s" % (n, k.get(a)))
    
  if(n in aR and a == 'exit'):
    print("%s %s" % (n, k.get(a)))
    aR.remove(n)
  elif(n not in aR and a == 'exit'):
    print("%s %s (ANOMALY)" % (n, k.get(a)))