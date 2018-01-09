k = []
def check(s):
  for i in s.split():
    if(i in k): return False
    k.append(i)
  return True
    
print("yes" if check(input()) else "no")