k,o = {}, ['+','-','*','//']

for x1 in o:
  for x2 in o:
    for x3 in o:
      x = eval("4{:s}4{:s}4{:s}4".format(x1, x2, x3))
      k[x] = "%s = %d" % ("4 {:s} 4 {:s} 4 {:s} 4".format(x1, x2, x3).replace('//','/'), x)

for _ in range(int(input())): print(k.get(int(input()),"no solution"))