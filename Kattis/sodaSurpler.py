e,f,c = map(int, input().split())
k = 0
e += f

while True:
  k += int(e/c)
  e = int(e%c) + int(e/c)
  if(e < c):
    break
  
print(int(k))