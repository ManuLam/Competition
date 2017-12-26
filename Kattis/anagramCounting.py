import math, collections
while True:
  try:
    s = input()
    c = collections.Counter(s).most_common()
    s1,p1 = 0,1
    
    for (x,y) in c:
      s1 += y
      p1 *= math.factorial(y)
    
    print(int(math.factorial(s1)//p1))

  except EOFError:
    break