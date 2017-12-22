import collections
a = []
while True:
  s = input()
  if(s == "***"): break
  a.append(s)

c = collections.Counter(a).most_common(2)
  
if(c[0][1] == c[1][1]): 
  print("Runoff!")
else: 
  print(c[0][0])