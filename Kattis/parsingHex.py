import re
while True:
  try:
    s = [x for x in input()]

    for i in range(len(s)-2):
      ns = ""
      if(s[i] == "0" and (s[i+1] == "x" or s[i+1] == "X")):
        ns += s[i] + s[i+1]
        for j in range(i+2, len(s)):
          if(re.match("[0-9]|[a-f]|[A-F]", s[j]) and j < len(s)-1):  ns += s[j]
          elif(re.match("[0-9]|[a-f]|[A-F]", s[j]) and j == len(s)-1): 
            ns += s[j] 
            print(ns, int(ns, 16))
            i = j
            break
          else:
            print(ns, int(ns, 16))
            i = j
            break
            
  except EOFError:
    break