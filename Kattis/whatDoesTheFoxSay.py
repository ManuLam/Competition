for i in range(int(input())):
  a = []
  s = [x for x in input().split()]
  
  while True:
    s1 = input()

    if(s1 == "what does the fox say?"):
      for j in range(len(s)):
        if(s[j] not in a):
          print(s[j], end = " " if j < len(s)-2 else "\n")
      break
    
    else:
      v,k = s1.split(' goes ')
      a.append(k)