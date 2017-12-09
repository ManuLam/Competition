while True:
  try:
    s = [x for x in input().split("\n")]
    
    for i in range(len(s)):
      if("problem" in s[i].lower()):
        print("yes")
      else:
        print("no")
  

  except EOFError:
    break