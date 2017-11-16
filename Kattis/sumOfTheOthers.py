while True:
  try:
    a = list(map(int, input().split()))
    
    for x in range(0, len(a)):
      if(sum(a) - a[x] == a[x]):
        print(a[x])
        break
    
  except EOFError:
    break