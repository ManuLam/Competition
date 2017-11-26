import math
while True:
  try:
    n = int(input())
    val = 1
    x = int(math.sqrt(n))

    for i in range(2, x+1):
      if (n % i == 0):
        m = n/i
        if(i != m):
          val += m
        val += i
    
    if(val == n):
      print(n, "perfect")
      
    elif  int(abs(val-n)) < 3:
      print(n, "almost perfect")
      
    else:
      print(n, "not perfect")
      
  except EOFError:
    break