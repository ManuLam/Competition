def numToWord(x,i):
  k =['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  kt = ['0','0','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
  if(len(x) == 1 or x[0] == '1'):
    return k[int(x)] if i != 0 else k[int(x)][0].upper() + k[int(x)][1:]
  else:
    if(x[1] == '0'): return kt[int(x[0])] if i != 0 else kt[int(x[0])][0].upper() + kt[int(x[0])][1:]
    return kt[int(x[0])] + "-" + k[int(x[1])] if i != 0 else kt[int(x[0])][0].upper() + kt[int(x[0])][1:] + "-" + k[int(x[1])]
  
while True:
  try:
    s = input().split()
    for i in range(len(s)):
      if(s[i].isdigit()):
        s[i] = numToWord(s[i],i)
        
    print(' '.join(s))

  except EOFError:
    break