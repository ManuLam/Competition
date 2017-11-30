while True:
  try:
    vowels = ['a','e','i','o','u','y']
    s = list(map(str, input().split()))
    b = []
    
    for i in range(len(s)):
      for j in range(len(s[i])):
        if(s[i][0] in vowels):
          b.append(s[i]+"yay")
          break
        
        elif(s[i][j] in vowels):
          b.append(s[i][j:]+s[i][:j]+"ay")
          break
        
    print(" ".join(map(str, b)))
  except EOFError:
    break