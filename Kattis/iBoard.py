a = []
while True:
  try:
    s = input()
    t1,t2 = 0,0
    for c in s:
      s1 = ''.join(format(ord(c), 'b')).zfill(7)
      t1 += sum([1 for cc in s1 if cc == '1'])
      t2 += sum([1 for cc in s1 if cc != '1'])
      
    a.append("free" if(t1%2 == 0 and t2%2 == 0) else "trapped")
    
  except EOFError:
    print('\n'.join(a))
    break