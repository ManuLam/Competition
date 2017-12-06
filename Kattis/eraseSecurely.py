import re
n,s1,s2 = int(input()),input(),input()

k = {'0':'1','1':'0'}
pattern = re.compile('|'.join(k.keys()))
r = pattern.sub(lambda x: k[x.group()], s1)

if(n % 2 == 0):
  if(s1 == s2):
    print("Deletion succeeded")
  else:
    print("Deletion failed")
  
else:
  if(s2 == r):
    print("Deletion succeeded")
  else:
    print("Deletion failed")