s,w,l,u,sy = input(),0,0,0,0
k = len(s)
for i in s:
  if(i == "_"):
    w += 1
  elif(i.islower()):
    l += 1
  elif(i.isupper()):
    u += 1
  else:
    sy += 1

print("%f\n%f\n%f\n%f" % (w/k,l/k,u/k,sy/k))