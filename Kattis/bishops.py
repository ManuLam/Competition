while True:
  try:
    n = int(input())
    
    if(n >= 1):
      print(2*(n-1) if(n > 1) else 1)
    else:
      print(0)
  
  except EOFError:
    break